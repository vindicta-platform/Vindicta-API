# Feature Specification: Rate Limiting Middleware

**Feature Branch**: `036-api-rate-limiting`  
**Created**: 2026-02-06  
**Status**: Draft  
**Target**: Week 3 | **Repository**: Vindicta-API

## User Scenarios & Testing

### User Story 1 - Enforce Rate Limits (Priority: P1)

API enforces per-user and global rate limits.

**Acceptance Scenarios**:
1. **Given** under limit, **When** request made, **Then** allowed
2. **Given** over limit, **When** request made, **Then** 429 returned

---

## Requirements

### Functional Requirements
- **FR-001**: Middleware MUST track per-user request counts
- **FR-002**: Middleware MUST enforce configurable limits
- **FR-003**: Middleware MUST return Retry-After header

### Key Entities
- **RateLimit**: limit, window, current
- **RateLimitConfig**: limits[], global_limit

## Success Criteria
- **SC-001**: Rate check in <10ms
- **SC-002**: Zero service degradation
