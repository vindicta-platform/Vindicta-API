# Vindicta-API Roadmap

> **Vision**: Unified API gateway for all Vindicta services
> **Status**: Active Development
> **Last Updated**: 2026-02-03

---

## v1.0 Target: March 2026

### Mission Statement
Provide a secure, scalable API gateway that exposes all Vindicta backend services to the Portal and external consumers, running on GCP Cloud Run within free tier limits.

---

## Milestone Timeline

```
┌─────────────────────────────────────────────────────────────────┐
│  Feb 2026          Mar 2026          Apr 2026                   │
│  ─────────────────────────────────────────────────────────────  │
│  [v0.1.0]          [v0.2.0]          [v1.0.0]                   │
│  Foundation        Core APIs         Production                 │
│                                                                  │
│  Week 1-2          Week 3-4          Week 5+                    │
└─────────────────────────────────────────────────────────────────┘
```

---

## v0.1.0 — Foundation (Target: Feb 10, 2026)

### Deliverables
- [ ] FastAPI application structure
- [ ] Cloud Run deployment
- [ ] Firebase Auth integration
- [ ] Health check endpoints
- [ ] CORS configuration
- [ ] Environment configuration

### Key Measurable Results
| Metric | Target | Measurement |
|--------|--------|-------------|
| **Deployment** | Cloud Run working | Smoke test |
| **Auth** | Firebase tokens validated | Integration test |
| **Latency** | <500ms cold start | Benchmark |

### Exit Criteria
- [ ] Deployed to Cloud Run
- [ ] Auth validates Firebase tokens
- [ ] Health endpoint responds

---

## v0.2.0 — Core APIs (Target: Feb 24, 2026)

### Deliverables
- [ ] Meta-Oracle endpoints
  - `/api/meta/snapshot`
  - `/api/meta/grade`
  - `/api/meta/upsets`
- [ ] WARScribe endpoints
  - `/api/games` (CRUD)
  - `/api/transcripts`
- [ ] Opening Book endpoints
  - `/api/openings/book`
  - `/api/openings/history`
- [ ] Agent-Auditor-SDK integration

### Key Measurable Results
| Metric | Target | Measurement |
|--------|--------|-------------|
| **Endpoints** | 8+ routes | API coverage |
| **Response Time** | <2 sec for grades | Performance test |
| **Error Rate** | <1% | Monitoring |

### Exit Criteria
- [ ] All core endpoints functional
- [ ] Quota-aware via Agent-Auditor
- [ ] Error handling consistent

---

## v1.0.0 — Production (Target: Mar 15, 2026)

### Deliverables
- [ ] Rate limiting
- [ ] API versioning
- [ ] OpenAPI documentation
- [ ] Monitoring and alerting
- [ ] Performance optimization
- [ ] GCP Free Tier compliance

### Key Measurable Results
| Metric | Target | Measurement |
|--------|--------|-------------|
| **Uptime** | 99%+ | Monitoring |
| **GCP Costs** | $0 (free tier) | Billing |
| **Documentation** | 100% endpoints | OpenAPI spec |
| **Latency P95** | <1 second | Metrics |

### Exit Criteria
- [ ] No critical bugs for 2 weeks
- [ ] Free tier limits respected
- [ ] OpenAPI docs published

---

## API Endpoints

### Meta-Oracle

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/meta/snapshot` | Current meta tier list |
| POST | `/api/meta/grade` | Grade an army list |
| GET | `/api/meta/upsets` | Find giant-killer lists |
| GET | `/api/meta/predictions` | Tracked predictions |

### WARScribe

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/games` | List user's games |
| POST | `/api/games` | Record a new game |
| GET | `/api/games/{id}` | Get game details |
| GET | `/api/transcripts/{id}` | Get WARScribe transcript |

### Opening Book

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/openings/book` | Get book setup for list |
| GET | `/api/openings/history` | Find historical games |

---

## Technology Stack

- **Framework**: FastAPI (Python)
- **Runtime**: GCP Cloud Run
- **Auth**: Firebase Authentication
- **Quota**: Agent-Auditor-SDK
- **Database**: DuckDB (embedded) / Firestore

---

## GCP Free Tier Compliance

| Resource | Free Tier | Our Usage |
|----------|-----------|-----------|
| Cloud Run | 2M requests/month | <100K expected |
| CPU | 180K vCPU-seconds | Within limits |
| Memory | 360K GB-seconds | Within limits |
| Egress | 1GB/month | Within limits |

---

## Dependencies

| Dependency | Status | Notes |
|------------|--------|-------|
| Meta-Oracle | 🔄 Parallel | Grading service |
| WARScribe-Core | 🔄 Parallel | Game data |
| Primordia AI | 🔄 Parallel | Opening Book |
| Agent-Auditor-SDK | 🔄 Parallel | Quota management |
| Firebase | ✅ Available | Auth |

---

## Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Free tier exceeded | Low | Medium | Usage monitoring |
| Cold start latency | Medium | Low | Minimum instances |
| Auth vulnerabilities | Low | High | Security audit |

---

## Success Criteria

1. **Reliability**: 99%+ uptime
2. **Cost**: $0 (free tier)
3. **Performance**: <1 second P95 latency
4. **Coverage**: All Portal features supported

---

*Maintained by: Vindicta Platform Team*
