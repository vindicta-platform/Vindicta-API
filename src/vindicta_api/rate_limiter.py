"""
Rate limiting implementation for Vindicta API.

Implements token bucket algorithm with per-user limits.
Free tier: 10 requests per minute with burst capacity.
"""

import time
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from threading import Lock
from typing import Optional

from fastapi import Request, Response
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware


@dataclass
class RateLimitConfig:
    """Rate limit configuration for a tier."""
    
    requests_per_minute: int = 10  # Free tier default
    burst_capacity: int = 15  # Allow short bursts
    
    @property
    def tokens_per_second(self) -> float:
        """Token refill rate."""
        return self.requests_per_minute / 60.0


@dataclass
class TokenBucket:
    """Token bucket for rate limiting."""
    
    capacity: float
    tokens: float
    last_refill: float = field(default_factory=time.time)
    refill_rate: float = 1.0  # tokens per second
    
    def consume(self, tokens: int = 1) -> bool:
        """
        Attempt to consume tokens.
        
        Returns:
            True if tokens were consumed, False if insufficient.
        """
        self._refill()
        
        if self.tokens >= tokens:
            self.tokens -= tokens
            return True
        return False
    
    def _refill(self) -> None:
        """Refill tokens based on elapsed time."""
        now = time.time()
        elapsed = now - self.last_refill
        
        # Add tokens based on refill rate
        self.tokens = min(
            self.capacity,
            self.tokens + (elapsed * self.refill_rate)
        )
        self.last_refill = now
    
    def time_until_available(self, tokens: int = 1) -> float:
        """
        Calculate seconds until tokens are available.
        
        Returns:
            Seconds to wait, or 0 if tokens available now.
        """
        self._refill()
        
        if self.tokens >= tokens:
            return 0.0
        
        deficit = tokens - self.tokens
        return deficit / self.refill_rate


class RateLimiter:
    """
    In-memory rate limiter using token bucket algorithm.
    
    Thread-safe implementation for concurrent requests.
    """
    
    def __init__(self, config: Optional[RateLimitConfig] = None):
        """
        Initialize rate limiter.
        
        Args:
            config: Rate limit configuration. Defaults to free tier.
        """
        self.config = config or RateLimitConfig()
        self._buckets: dict[str, TokenBucket] = {}
        self._lock = Lock()
    
    def is_allowed(self, user_id: str) -> tuple[bool, Optional[float]]:
        """
        Check if request is allowed for user.
        
        Args:
            user_id: User identifier (e.g., Firebase UID)
            
        Returns:
            Tuple of (is_allowed, retry_after_seconds)
        """
        with self._lock:
            bucket = self._get_bucket(user_id)
            
            if bucket.consume():
                return True, None
            else:
                retry_after = bucket.time_until_available()
                return False, retry_after
    
    def _get_bucket(self, user_id: str) -> TokenBucket:
        """Get or create token bucket for user."""
        if user_id not in self._buckets:
            self._buckets[user_id] = TokenBucket(
                capacity=self.config.burst_capacity,
                tokens=self.config.burst_capacity,
                refill_rate=self.config.tokens_per_second
            )
        return self._buckets[user_id]
    
    def get_remaining(self, user_id: str) -> int:
        """Get remaining tokens for user."""
        with self._lock:
            bucket = self._get_bucket(user_id)
            bucket._refill()
            return int(bucket.tokens)
    
    def reset(self, user_id: str) -> None:
        """Reset rate limit for user (admin function)."""
        with self._lock:
            if user_id in self._buckets:
                del self._buckets[user_id]


class RateLimitMiddleware(BaseHTTPMiddleware):
    """
    FastAPI middleware for rate limiting.
    
    Adds rate limit headers to all responses and returns 429 when exceeded.
    """
    
    def __init__(self, app, limiter: Optional[RateLimiter] = None):
        super().__init__(app)
        self.limiter = limiter or RateLimiter()
    
    async def dispatch(self, request: Request, call_next):
        """Process request with rate limiting."""
        
        # Extract user ID from request
        # TODO: Integrate with Firebase Auth to get real user_id
        user_id = self._get_user_id(request)
        
        # Check rate limit
        is_allowed, retry_after = self.limiter.is_allowed(user_id)
        
        if not is_allowed:
            return JSONResponse(
                status_code=429,
                content={
                    "error": "Rate limit exceeded",
                    "message": f"Too many requests. Try again in {int(retry_after)} seconds.",
                    "retry_after": int(retry_after)
                },
                headers={
                    "Retry-After": str(int(retry_after)),
                    "X-RateLimit-Limit": str(self.limiter.config.requests_per_minute),
                    "X-RateLimit-Remaining": "0",
                    "X-RateLimit-Reset": str(int(time.time() + retry_after))
                }
            )
        
        # Process request
        response = await call_next(request)
        
        # Add rate limit headers
        remaining = self.limiter.get_remaining(user_id)
        response.headers["X-RateLimit-Limit"] = str(self.limiter.config.requests_per_minute)
        response.headers["X-RateLimit-Remaining"] = str(remaining)
        response.headers["X-RateLimit-Reset"] = str(int(time.time() + 60))
        
        return response
    
    def _get_user_id(self, request: Request) -> str:
        """
        Extract user ID from request.
        
        For now, uses IP address. Will be replaced with Firebase UID.
        """
        # TODO: Extract from Firebase JWT token
        client_host = request.client.host if request.client else "unknown"
        return f"ip:{client_host}"
