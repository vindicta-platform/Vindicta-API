# Vindicta-API Constraints

> Critical rules agents MUST follow when modifying this repository.

## ⛔ Hard Constraints

1. **FastAPI Only** - No Flask/Django/other frameworks
2. **Async Everywhere** - All route handlers must be `async def`
3. **Pydantic Schemas** - All requests/responses via Pydantic models
4. **No Direct DB Access** - All data via service layer

## 🔐 Security Rules

### Authentication
- All endpoints require JWT except `/health` and `/docs`
- Tokens expire in 24 hours
- Refresh tokens expire in 7 days

### Rate Limiting
```python
DEFAULT_RATE = "100/minute"
GRADE_RATE = "10/minute"  # AI-intensive
DEBATE_RATE = "5/minute"  # Most expensive
```

### Input Validation
- All inputs validated via Pydantic
- SQL injection prevented via ORM
- No raw string concatenation in queries

## 📐 API Design Rules

### Versioning
- All routes under `/api/v1/`
- Breaking changes require new version
- Old versions deprecated, not removed

### Response Format
```python
{
    "data": {...},        # Payload
    "meta": {             # Pagination, etc.
        "page": int,
        "total": int
    },
    "errors": []          # Only on failure
}
```

## 🧪 Testing Requirements

Before merging:
- [ ] `pytest` passes
- [ ] OpenAPI spec validates
- [ ] Auth tests cover all protected routes
- [ ] Rate limit tests verify throttling
