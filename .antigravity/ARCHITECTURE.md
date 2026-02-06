# Vindicta-API Architecture

> Agent context artifact for the unified REST gateway service.

## Purpose

Central REST API gateway orchestrating all platform services. Handles authentication, rate limiting, and request routing.

## Technology Stack

- **Framework**: FastAPI
- **Language**: Python 3.11+
- **Auth**: JWT tokens
- **Docs**: OpenAPI 3.0
- **Validation**: Pydantic v2

## Directory Structure

```
├── src/vindicta_api/
│   ├── routes/         # API endpoint handlers
│   ├── middleware/     # Auth, rate limiting, logging
│   ├── services/       # Business logic orchestration
│   ├── schemas/        # Request/response models
│   └── deps/           # Dependency injection
├── tests/
└── docs/
```

## API Architecture

```mermaid
graph TD
    A[Client] --> B[API Gateway]
    B --> C[Auth Middleware]
    C --> D[Rate Limiter]
    D --> E{Router}
    
    E --> F[/lists/*]
    E --> G[/matches/*]
    E --> H[/debates/*]
    E --> I[/grades/*]
    
    F --> J[WARScribe-Core]
    G --> K[Vindicta-Core]
    H --> L[Meta-Oracle]
    I --> M[Primordia-AI]
```

## Key Endpoints

| Endpoint          | Method | Service                 |
| ----------------- | ------ | ----------------------- |
| `/api/v1/lists`   | CRUD   | WARScribe-Core          |
| `/api/v1/matches` | CRUD   | Vindicta-Core           |
| `/api/v1/grade`   | POST   | Meta-Oracle + Primordia |
| `/api/v1/debate`  | POST   | Meta-Oracle             |

## Integration Points

All backend services connect through this API.
