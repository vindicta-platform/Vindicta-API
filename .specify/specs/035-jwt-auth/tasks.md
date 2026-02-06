# Tasks: JWT Authentication Middleware

**Input**: specs/035-jwt-auth/ | **Prerequisites**: spec.md, plan.md

## Phase 1: Setup

- [ ] T001 Create `src/middleware/auth.py`
- [ ] T002 [P] Add firebase-admin dependency

---

## Phase 2: Foundational

- [ ] T003 Define AuthContext Pydantic model
- [ ] T004 [P] Initialize Firebase Admin SDK

---

## Phase 3: User Story 1 - Validate Firebase JWT (P1) 🎯 MVP

- [ ] T005 [US1] Extract token from Authorization header
- [ ] T006 [US1] Verify JWT signature
- [ ] T007 [US1] Check token expiration
- [ ] T008 [US1] Extract user claims
- [ ] T009 [US1] Cache public keys
- [ ] T010 [US1] Return 401 on invalid token

---

## Phase 4: Polish

- [ ] T011 [P] Optimize for <50ms auth check
- [ ] T012 [P] Write auth validation tests
