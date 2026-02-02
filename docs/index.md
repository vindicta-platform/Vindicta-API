# Vindicta API

**The unified HTTP gateway for Vindicta services.**

Vindicta API provides RESTful endpoints for dice rolling, economy management, and AI predictions — all powered by FastAPI with full OpenAPI documentation.

---

## Features

- **Async-First** — Full async/await support
- **OpenAPI Documented** — Auto-generated API docs
- **Type-Safe** — Pydantic validation on all endpoints
- **Dependency Injection** — Clean service composition

## Quick Start

```bash
# Install
uv pip install git+https://github.com/vindicta-platform/Vindicta-API.git

# Run locally
uvicorn vindicta_api:app --reload

# Access docs
open http://localhost:8000/docs
```

## Endpoints

| Path | Method | Description |
|------|--------|-------------|
| `/health` | GET | Health check |
| `/dice/roll` | POST | Roll dice |
| `/economy/balance` | GET | Get credits |
| `/oracle/predict` | POST | Get prediction |

---

## Part of the Vindicta Platform

[Full Platform Documentation](https://vindicta-platform.github.io/mkdocs/)
