# Contributing

## Setup
```bash
git clone https://github.com/vindicta-platform/Vindicta-API.git
cd Vindicta-API
uv venv && uv pip install -e ".[dev]"
```

## Tests
```bash
pytest tests/ -v
```

## Style
- Ruff formatting
- Type hints required
- Async-first design

## Pre-Commit Hooks (Required)

All developers **must** install and run pre-commit hooks before committing. This ensures:
- All markdown links are validated
- Code quality (Ruff) is enforced

### Setup

```bash
uv pip install pre-commit
pre-commit install
```

## License
MIT
