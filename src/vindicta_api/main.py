"""Vindicta API - Async-First FastAPI Application.

Constitution Compliance:
- XVI. Async-First Mandate: All handlers use async/await
- I. Economic Prime: Firebase Hosting on GCP Free Tier
- II. Gas Tank: Cost estimation endpoints
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from vindicta_api.rate_limiter import RateLimitMiddleware, RateLimiter, RateLimitConfig

app = FastAPI(
    title="Vindicta API",
    description="REST API for the Vindicta Platform",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS for Portal frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure per environment
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rate limiting middleware (free tier: 10 RPM)
rate_limiter = RateLimiter(RateLimitConfig(requests_per_minute=10, burst_capacity=15))
app.add_middleware(RateLimitMiddleware, limiter=rate_limiter)


@app.get("/health", tags=["System"])
async def health_check() -> dict[str, str]:
    """Health check endpoint - async per Constitution XVI."""
    return {"status": "healthy", "constitution": "XVI-compliant"}


@app.get("/api/v1/status", tags=["System"])
async def api_status() -> dict[str, str | bool]:
    """API status with Gas Tank state."""
    return {
        "version": "0.1.0",
        "gas_tank_active": True,
        "gemini_configured": False,  # TODO: Check actual config
        "rate_limiting": True,
    }
