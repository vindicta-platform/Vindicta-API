# Feature Proposal: API Rate Limiting & DDoS Protection

**Proposal ID**: FEAT-014  
**Author**: Unified Product Architect (Autonomous)  
**Created**: 2026-02-01  
**Status**: Draft  
**Priority**: Critical  

---

## Part A: Software Design Document (SDD)

### 1. Executive Summary

Implement comprehensive rate limiting and DDoS protection for the Vindicta API, protecting platform availability while providing fair access to all users based on their membership tier.

### 2. System Architecture

#### 2.1 Current State
- Basic Cloud Run scaling
- No application-level rate limiting
- No abuse detection
- No per-user quotas

#### 2.2 Proposed Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    Rate Limiting Stack                          │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │              Cloud Armor (Layer 7)                      │    │
│  │   - IP-based rate limits                                │    │
│  │   - Geo-blocking                                        │    │
│  │   - Bot detection                                       │    │
│  └─────────────────────────────────────────────────────────┘    │
│                              │                                  │
│                              ▼                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │              Application Rate Limiter                   │    │
│  │   - Token bucket per user                               │    │
│  │   - Sliding window per endpoint                         │    │
│  │   - Tier-based limits                                   │    │
│  └─────────────────────────────────────────────────────────┘    │
│                              │                                  │
│                              ▼                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │              Redis Cluster (State)                      │    │
│  │   - Rate limit counters                                 │    │
│  │   - Sliding window data                                 │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

#### 2.3 File Changes

```
Vindicta-API/
├── src/
│   └── api/
│       ├── middleware/
│       │   ├── __init__.py        [NEW]
│       │   ├── rate_limit.py      [NEW] Rate limiting middleware
│       │   └── abuse_detect.py    [NEW] Abuse pattern detection
│       ├── limiter/
│       │   ├── __init__.py        [NEW]
│       │   ├── token_bucket.py    [NEW] Token bucket algorithm
│       │   ├── sliding_window.py  [NEW] Sliding window counter
│       │   └── redis_store.py     [NEW] Redis backend
│       └── main.py                [MODIFY] Add middleware
├── tests/
│   └── test_rate_limiting.py      [NEW]
└── docs/
    └── rate-limiting.md           [NEW]
```

### 3. Rate Limits by Tier

| Tier | Requests/Minute | Burst | Daily Limit |
|------|-----------------|-------|-------------|
| Anonymous | 10 | 20 | 100 |
| Free | 30 | 50 | 1,000 |
| Supporter | 100 | 200 | 10,000 |
| Champion | 300 | 500 | Unlimited |
| API Partner | Custom | Custom | Custom |

### 4. Endpoint-Specific Limits

| Endpoint | Additional Limit | Rationale |
|----------|-----------------|-----------|
| `/auth/*` | 5/min | Prevent brute force |
| `/battles` POST | 10/min | Spam prevention |
| `/oracle/predict` | 20/hour | Compute intensive |
| `/dice/roll` | 100/min | High-frequency use case |

### 5. Abuse Detection

```python
class AbuseDetector:
    """Detect and block abusive patterns."""
    
    patterns = {
        'credential_stuffing': {'login_failures': 10, 'window': 300},
        'scraping': {'unique_endpoints': 50, 'window': 60},
        'enumeration': {'404_responses': 20, 'window': 60},
    }
    
    def check(self, request: Request) -> Optional[AbuseType]:
        """Check if request matches abuse pattern."""
```

### 6. Response Headers

```http
HTTP/1.1 200 OK
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 87
X-RateLimit-Reset: 1706842800
Retry-After: 60  # (only on 429)
```

---

## Part B: Behavior Driven Development (BDD)

### User Stories

#### US-001: Fair Access
**As a** paying member  
**I want** higher rate limits than free users  
**So that** my subscription provides value

#### US-002: Clear Feedback
**As an** API consumer  
**I want** rate limit headers in responses  
**So that** I can implement proper backoff

#### US-003: Attack Protection
**As a** platform operator  
**I want** automatic abuse blocking  
**So that** the platform stays available

### Acceptance Criteria

```gherkin
Feature: API Rate Limiting

  Scenario: Rate limit applied to anonymous user
    Given I am not authenticated
    When I make 15 requests in one minute
    Then the first 10 should succeed
    And requests 11-15 should return 429 Too Many Requests
    And include a Retry-After header

  Scenario: Higher limits for Champion tier
    Given I am authenticated as a Champion member
    When I make 200 requests in one minute
    Then all requests should succeed
    And X-RateLimit-Remaining should decrease

  Scenario: Abuse pattern blocked
    Given an IP makes 50 failed login attempts
    When they try another login
    Then the IP should be temporarily blocked
    And return 403 Forbidden
```

---

## Implementation Estimate

| Phase | Effort | Dependencies |
|-------|--------|--------------|
| Rate Limit Middleware | 6 hours | Redis |
| Token Bucket | 4 hours | None |
| Abuse Detection | 6 hours | None |
| Cloud Armor Config | 4 hours | GCP access |
| Testing | 4 hours | Load testing tools |
| **Total** | **24 hours** | |
