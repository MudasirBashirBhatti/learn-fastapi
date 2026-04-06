# 1. Install Alembic

Alembic is a lightweight database migration tool for Python that works specifically with the SQLAlchemy Database Toolkit.

# Adds alembic as a dependency to your project

```bash
uv add alembic
```

---

# 2. Verify Installation

# Checks that alembic is installed correctly

```bash
uv run alembic --version

```

---

# 3. Initialize Alembic

# Creates the 'migrations' folder and necessary configuration files

```bash
uv run alembic init migrations
```

---

# 4. Generate Migration Script

# Compares your SQLAlchemy models with the database and creates a migration script

```bash
uv run alembic revision --autogenerate -m "initial tables"
```

---

# 5. Apply Migrations

# Upgrades your database schema to the latest version (head)

```bash
uv run alembic upgrade head
```
