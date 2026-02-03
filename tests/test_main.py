"""Tests for Vindicta API - Constitution XV/XVI compliant.

- All tests are async (XVI)
- Tests isolated, no network I/O (XV.2)
- AAA pattern (XV.5)
"""

import pytest
from httpx import ASGITransport, AsyncClient

from vindicta_api.main import app


@pytest.fixture
async def client():
    """Async test client - no real network I/O per Constitution XV."""
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as ac:
        yield ac


@pytest.mark.asyncio
async def test_health_check(client: AsyncClient):
    """Health endpoint returns healthy status."""
    # Arrange - client fixture
    
    # Act
    response = await client.get("/health")
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["constitution"] == "XVI-compliant"


@pytest.mark.asyncio
async def test_api_status(client: AsyncClient):
    """API status returns version and Gas Tank state."""
    # Arrange - client fixture
    
    # Act
    response = await client.get("/api/v1/status")
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data["version"] == "0.1.0"
    assert "gas_tank_active" in data
