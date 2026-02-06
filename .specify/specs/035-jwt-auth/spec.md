# Feature Specification: JWT Authentication Middleware

**Feature Branch**: `035-jwt-auth`  
**Created**: 2026-02-06  
**Status**: Draft  
**Target**: Week 2 | **Repository**: Vindicta-API

## User Scenarios & Testing

### User Story 1 - Validate Firebase JWT (Priority: P1)

API validates Firebase ID tokens on protected routes.

**Acceptance Scenarios**:
1. **Given** valid token, **When** request made, **Then** user authenticated
2. **Given** expired token, **When** request made, **Then** 401 returned

---

## Requirements

### Functional Requirements
- **FR-001**: Middleware MUST verify Firebase JWT signature
- **FR-002**: Middleware MUST check token expiration
- **FR-003**: Middleware MUST extract user claims
- **FR-004**: Middleware MUST cache public keys

### Key Entities
- **AuthContext**: uid, email, claims, token_exp

## Success Criteria
- **SC-001**: Auth check in under 50ms
- **SC-002**: Zero unauthorized access
