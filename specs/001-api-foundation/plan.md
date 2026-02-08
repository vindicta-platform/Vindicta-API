# Implementation Plan: API Foundation (v0.1.0)

**Spec Reference:** [spec.md](./spec.md)

---

## Proposed Changes

```
src/vindicta_api/
├── __init__.py
├── main.py              # FastAPI app factory
├── config.py            # Settings via pydantic-settings
├── middleware/
│   ├── __init__.py
│   ├── auth.py          # Firebase Auth dependency
│   └── cors.py          # CORS configuration
├── routers/
│   ├── __init__.py
│   ├── health.py        # GET /health
│   └── auth.py          # GET /v1/me
└── models/
    ├── __init__.py
    └── responses.py     # HealthResponse, UserResponse
Dockerfile
cloudbuild.yaml          # Cloud Run deployment
```

### Tests

```
tests/
├── test_health.py
├── test_auth.py
├── test_cors.py
└── conftest.py         # TestClient fixture
```

---

## Verification

```powershell
uv run pytest tests/ -v
uv run uvicorn vindicta_api.main:app --port 8080  # local smoke test
curl http://localhost:8080/health
```
