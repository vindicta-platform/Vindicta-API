# Authentication Design

## Provider: Firebase Authentication

**Rationale**: GCP Free Tier compliant (10K MAU), JWT-based, integrates with Vindicta-Portal.

### Supported Auth Methods
1. **Google OAuth** (primary)
2. **GitHub OAuth** (developer community)
3. **Anonymous Auth** (free tier)

## JWT Token Flow

Portal obtains Firebase JWT → API verifies token via Firebase Admin SDK → Extract user ID + tier → Enforce rate limits.

## FastAPI Implementation

```python
# src/vindicta_api/auth.py
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from firebase_admin import auth

security = HTTPBearer()

async def get_current_user(credentials = Depends(security)) -> dict:
    """Verify Firebase JWT and return user claims."""
    try:
        return auth.verify_id_token(credentials.credentials)
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")
```

### Usage Example

```python
@app.get("/api/v1/army/{armyId}")
async def get_army(armyId: str, user: dict = Depends(get_current_user)):
    user_id = user['user_id']
    # ... fetch army for user_id
```

## Role-Based Access Control (RBAC)

| Tier | Endpoints | Rate Limit |
|------|-----------|------------|
| Anonymous | /health, /meta (read-only) | 10 RPM |
| Free | All GET, limited POST | 60 RPM |
| Paid | All endpoints | 300 RPM |

## Rate Limiting Integration

Uses Agent-Auditor-SDK `RateLimiter` with per-user quotas based on Firebase `tier` custom claim.

## Security

- **HTTPS only** (Firebase Hosting enforces TLS)
- **Token expiry**: 1-hour (Firebase default)
- **CORS**: Restricted to `vindicta-portal.web.app` in production

## Implementation Timeline

- **Week 3 (Feb 11-17)**: Install `firebase-admin`, implement `get_current_user`
- **Week 4 (Feb 18-24)**: Portal integration, OAuth flows, E2E tests

## References

- [OpenAPI Auth Spec](./openapi.yaml#L33-L35)
- [Firebase Auth Docs](https://firebase.google.com/docs/auth)
- [Planned ADR-0004: Firebase Auth Strategy](../../Platform-Docs/docs/adr) (Week 2)
