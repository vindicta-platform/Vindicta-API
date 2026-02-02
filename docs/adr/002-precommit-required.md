# ADR-002: Pre-commit Hooks Required

**Status**: Accepted  
**Date**: 2026-02-01

## Context

Code quality requires enforcement before commits.

## Decision

All repositories MUST configure **pre-commit** hooks.

## Required Hooks

- ruff (lint + format)
- trailing-whitespace
- end-of-file-fixer
- check-yaml

## Alternatives Considered

| Alternative | Decision |
|-------------|----------|
| CI-only | Rejected — late feedback |
| Manual | Rejected — inconsistent |

## Consequences

- `.pre-commit-config.yaml` required
- Developers run `pre-commit install`
