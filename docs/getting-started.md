# Getting Started

## Installation

```bash
uv pip install git+https://github.com/vindicta-platform/Vindicta-API.git
```

## Running the Server

```bash
uvicorn vindicta_api:app --reload --port 8000
```

## First Request

```bash
curl http://localhost:8000/health
```

Response:
```json
{"status": "healthy", "version": "0.1.0"}
```

## Development

```bash
git clone https://github.com/vindicta-platform/Vindicta-API.git
cd Vindicta-API
uv venv && uv pip install -e ".[dev]"
pytest tests/ -v
```
