# Vindicta-API

FastAPI-based REST API for the Vindicta Platform.

## Overview

Vindicta-API provides the HTTP interface for all platform services, including dice rolling, economy management, and Meta-Oracle predictions.

## Features

- **RESTful Endpoints**: Clean, documented API routes
- **OpenAPI Spec**: Auto-generated documentation
- **Dependency Injection**: Clean service composition
- **Async-First**: Full async/await support

## Installation

Install from source using uv:

```bash
uv pip install git+https://github.com/vindicta-platform/Vindicta-API.git
```

Or clone and install locally:

```bash
git clone https://github.com/vindicta-platform/Vindicta-API.git
cd Vindicta-API
uv pip install -e .
```

## Quick Start

```bash
# Run development server
uvicorn vindicta_api:app --reload

# Access docs at http://localhost:8000/docs
```

## API Structure

```
/api/v1/
├── /dice     # Dice rolling endpoints
├── /economy  # Gas Tank and billing
├── /oracle   # Meta-Oracle predictions
└── /health   # Health checks
```

## Related Repositories

| Repository | Relationship |
|------------|-------------|
| [Vindicta-Core](https://github.com/vindicta-platform/Vindicta-Core) | Shared primitives |
| [Logi-Slate-UI](https://github.com/vindicta-platform/Logi-Slate-UI) | Frontend consumer |

## Platform Documentation

> **📌 Important:** All cross-cutting decisions, feature proposals, and platform-wide architecture documentation live in [**Platform-Docs**](https://github.com/vindicta-platform/Platform-Docs).
>
> Any decision affecting multiple repos **must** be recorded there before implementation.

- 📋 [Feature Proposals](https://github.com/vindicta-platform/Platform-Docs/tree/main/docs/proposals)
- 🏗️ [Architecture Decisions](https://github.com/vindicta-platform/Platform-Docs/tree/main/docs)
- 📖 [Contributing Guide](https://github.com/vindicta-platform/Platform-Docs/blob/main/CONTRIBUTING.md)

## License

MIT License - See [LICENSE](./LICENSE) for details.
