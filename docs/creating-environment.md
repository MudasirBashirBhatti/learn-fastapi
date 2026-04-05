# 1. Create a Python virtual environment

The following command creates a new isolated Python environment named `myevironment`:

```bash
python -m venv myenvironment
```

## Activate the virtual environment

```bash
# Go to your project root folder
cd ~/Desktop/fast-project

# Activate the virtual environment and this command will only works on gitbash
source myenvironment/Scripts/activate
```

## Deactivate the virtual environment

```bash

# deactivate the virtual environment
deactivate
```

# 2. Install dependencies

```bash
uv add fastapi uvicorn
```

# 3. How to run the project using uv

```bash
uv run uvicorn main:app --reload
```
