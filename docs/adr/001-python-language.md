# ADR-001: Python as Primary Language

**Status**: Accepted
**Date**: 2026-02-01

## Context

This repository requires a programming language for implementation.

## Decision

We adopt **Python 3.10+** as the primary language.

## Rationale

- Vindicta Platform is Python-first
- Rich ecosystem (FastAPI, pytest, ruff)
- Native async/await for API operations

## Alternatives Considered

| Alternative | Decision |
|-------------|----------|
| TypeScript | Rejected — different ecosystem |
| Rust | Rejected — slower iteration |
| Go | Rejected — less expressive |

## Consequences

- All source code uses Python 3.10+
- Type hints required on all public APIs
