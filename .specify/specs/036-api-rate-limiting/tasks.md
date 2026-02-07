# Tasks: Rate Limiting Middleware

**Input**: specs/036-api-rate-limiting/ | **Prerequisites**: spec.md, plan.md

## Phase 1: Setup

- [ ] T001 Create `src/middleware/rate_limit.py`
- [ ] T002 [P] Add slowapi dependency

---

## Phase 2: Foundational

- [ ] T003 Define RateLimit model
- [ ] T004 [P] Configure Redis connection

---

## Phase 3: User Story 1 - Enforce Rate Limits (P1) 🎯 MVP

- [ ] T005 [US1] Track per-user request counts
- [ ] T006 [US1] Configure endpoint limits
- [ ] T007 [US1] Return 429 on limit exceeded
- [ ] T008 [US1] Add Retry-After header

---

## Phase 4: Polish

- [ ] T009 [P] Optimize for <10ms check
- [ ] T010 [P] Write rate limiting tests
