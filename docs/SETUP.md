# Setup Guide

## Prerequisites
- Python 3.10+
- uv

## Development Setup
```bash
git clone https://github.com/vindicta-platform/Vindicta-API.git
cd Vindicta-API
uv venv
uv pip install -e ".[dev]"
```

## Running
```bash
uvicorn vindicta_api:app --reload
```

## Testing
```powershell
pytest tests/ -v
```
