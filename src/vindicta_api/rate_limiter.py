"""
Rate limiting middleware for Vindicta-API.

Implements per-user rate limiting per Issue #3.
"""

from datetime import datetime, timedelta
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class RateLimitConfig:
    """Rate limit configuration."""
    requests_per_minute: int = 10  # Free tier default
    burst_limit: int = 5


@dataclass 
class RateLimitState:
    """Current rate limit state for a user."""
    user_id: str
    request_count: int = 0
    window_start: datetime = field(default_factory=datetime.utcnow)
    
    def is_limited(self, config: RateLimitConfig) -> bool:
        """Check if user is rate limited."""
        if self._window_expired():
            self._reset_window()
            return False
        return self.request_count >= config.requests_per_minute
    
    def record_request(self) -> None:
        """Record a request."""
        if self._window_expired():
            self._reset_window()
        self.request_count += 1
    
    def _window_expired(self) -> bool:
        return datetime.utcnow() - self.window_start > timedelta(minutes=1)
    
    def _reset_window(self) -> None:
        self.window_start = datetime.utcnow()
        self.request_count = 0
    
    def retry_after(self) -> int:
        """Seconds until rate limit resets."""
        elapsed = (datetime.utcnow() - self.window_start).seconds
        return max(0, 60 - elapsed)
