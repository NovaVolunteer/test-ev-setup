# test_ev_setup

### Setup

The environment is already built. The goal is to use this directory as an example to help students understand the importance of folder and file construction as it relates to managing data science projects. 

**VS Code** — open this folder. The interpreter is pinned in `.vscode/settings.json`;
accept the recommended extensions when prompted.

**Terminal** — activate the venv:

```bash
# macOS / Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1

# Windows cmd
.venv\Scripts\activate.bat
```

**Notebooks** — select the kernel named `Python (test_ev_setup)`.

## Layout

```
src/test_ev_setup/      your code
tests/          pytest suite
notebooks/      exploration
requirements.txt
.env.example    copy to .env for secrets
```

## Common commands

```bash
pytest                          # run tests
ruff check . --fix              # lint + sort imports
black .                         # format
pip install -r requirements.txt # sync after editing requirements
pip freeze > requirements.lock  # snapshot exact versions
```

## Rebuilding from scratch

The venv is disposable — everything needed to recreate it is in `requirements.txt`.
Requires [uv](https://docs.astral.sh/uv/): `pip install uv` or `winget install astral-sh.uv`.

```bash
uv venv .venv
uv pip install --python .venv/bin/python -r requirements.txt   # Scripts/python.exe on Windows
uv pip install --python .venv/bin/python -e .
.venv/bin/python -m ipykernel install --user --name test_ev_setup --display-name "Python (test_ev_setup)"
```

Preset: `ml`.

