# Specification: API Foundation (v0.1.0)

**Feature ID:** 001-api-foundation
**Milestone:** v0.1.0 — Foundation
**Priority:** P0
**Status:** Specified
**Target Date:** Feb 10, 2026

---

## 1. Problem Statement

The Vindicta Platform needs a central API gateway to serve the Portal, CLI,
and third-party integrations. Without Vindicta-API, each client must
directly import Python packages, limiting the platform to local-only usage.

---

## 2. Vision

Deploy a FastAPI application on Cloud Run with Firebase Auth integration,
providing the HTTP foundation for all Vindicta platform services.

---

## 3. User Stories

### US-01: Health Check

> As an **operations engineer**,
> I want a **health endpoint** (`GET /health`),
> So that **monitoring systems can verify the API is running**.

**Acceptance Criteria:**

- [ ] Returns `{"status": "healthy", "version": "0.1.0"}`
- [ ] < 100ms response time
- [ ] No auth required

### US-02: Firebase Auth Integration

> As a **mobile/web client**,
> I want to **authenticate with Firebase tokens**,
> So that **my API requests are authorized**.

**Acceptance Criteria:**

- [ ] `Authorization: Bearer <firebase_token>` header validated
- [ ] 401 returned for invalid/expired tokens
- [ ] User ID extracted from token and available in request context
- [ ] Auth middleware configurable (allow/deny list of paths)

### US-03: Cloud Run Deployment

> As the **platform team**,
> I want the **API deployed to Cloud Run**,
> So that **it auto-scales and stays within GCP free tier**.

**Acceptance Criteria:**

- [ ] Dockerfile builds and runs FastAPI app
- [ ] Cloud Run service deployed and accessible via HTTPS
- [ ] Cold start < 500ms
- [ ] Auto-scaling 0→1→N instances

### US-04: CORS Configuration

> As the **Vindicta-Portal**,
> I want **CORS headers** configured for my domain,
> So that **browser requests are not blocked**.

**Acceptance Criteria:**

- [ ] CORS origins configurable via environment variables
- [ ] Preflight requests handled correctly
- [ ] Default: allow `localhost:*` in dev, specific domains in prod

### US-05: API Structure & OpenAPI

> As a **developer**,
> I want a **well-structured FastAPI application** with auto-generated docs,
> So that **I can explore and test endpoints easily**.

**Acceptance Criteria:**

- [ ] Router-based organization (`routers/health.py`, `routers/auth.py`)
- [ ] OpenAPI spec at `/docs` (Swagger) and `/redoc`
- [ ] Dependency injection for auth, config
- [ ] Pydantic response models

---

## 4. Functional Requirements

### 4.1 Endpoints

| Method | Path      | Auth | Description                              |
| ------ | --------- | ---- | ---------------------------------------- |
| `GET`  | `/health` | No   | Service health check                     |
| `GET`  | `/v1/me`  | Yes  | Current user profile from Firebase token |
| `GET`  | `/docs`   | No   | Swagger UI                               |
| `GET`  | `/redoc`  | No   | ReDoc UI                                 |

### 4.2 Configuration

| Env Var               | Type  | Default  | Description                           |
| --------------------- | ----- | -------- | ------------------------------------- |
| `FIREBASE_PROJECT_ID` | `str` | Required | Firebase project for token validation |
| `CORS_ORIGINS`        | `str` | `"*"`    | Comma-separated allowed origins       |
| `PORT`                | `int` | `8080`   | Server port                           |
| `LOG_LEVEL`           | `str` | `"info"` | Logging level                         |

### 4.3 Auth Middleware

```python
# Auth dependency
async def require_auth(token: str = Depends(firebase_auth)):
    return token.uid
```

---

## 5. Non-Functional Requirements

| Category         | Requirement                          |
| ---------------- | ------------------------------------ |
| **Performance**  | Cold start < 500ms, Response < 100ms |
| **Security**     | Firebase Auth, HTTPS only            |
| **Deployment**   | Cloud Run, Docker                    |
| **Dependencies** | FastAPI, uvicorn, firebase-admin     |
| **Python**       | 3.12+                                |

---

## 6. Out of Scope

- Game-specific API endpoints (v0.2.0)
- Database integration (v0.2.0)
- Rate limiting (v1.0.0)

---

## 7. Success Criteria

| Metric     | Target                    |
| ---------- | ------------------------- |
| Deployment | Cloud Run alive           |
| Auth       | Firebase tokens validated |
| Health     | Endpoint responds         |
| Docs       | OpenAPI available         |
