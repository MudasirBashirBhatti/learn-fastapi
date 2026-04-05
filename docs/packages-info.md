# Packages Documentation

## 1. (fastapi & uvicorn) Overview

`fastapi` and `uvicorn` are commonly used together to build and run modern Python web APIs.

- **FastAPI** → Used to create APIs (application logic)
- **Uvicorn** → Used to run the API (server)

---

## 2. Ruff — Python Linter & Formatter

[Ruff](https://github.com/charliermarsh/ruff) is a **fast Python linter and code formatter**.  
It combines the functionality of tools like `flake8`, `isort`, and `black` into **one extremely fast tool**.

### Installation

Inside a Python virtual environment:

```bash
# Using uv (recommended in your setup)
uv add ruff
```

**Basic Commands**

```bash
# Check command
uv run ruff check .
```

```bash
# Check and fix
uv run ruff check . --fix
```

```bash
# Formating only
uv run ruff format .
```
