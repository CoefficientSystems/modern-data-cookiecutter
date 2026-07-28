# Managing dependencies with uv

This project uses [uv](https://docs.astral.sh/uv/) to manage the Python version, the virtualenv and
all dependencies. The source of truth is `pyproject.toml` (what we ask for) and `uv.lock` (the
fully-resolved, pinned versions). Both are committed. A `requirements.txt` is also generated from
the lockfile (by pre-commit) for colleagues or deploy tooling that don't use uv.


## uv tl;dr

```sh
# Sync your environment with uv.lock (creates .venv if needed). Run this after every pull.
uv sync

# Add a runtime dependency (updates pyproject.toml + uv.lock + installs it)
uv add pandas

# Add a dev-only dependency (linters, test tools, etc.)
uv add --dev pytest-cov

# Remove a dependency
uv remove pandas

# Run a command inside the project environment (no manual activation needed)
uv run pytest
uv run python -m {{ cookiecutter.package_name }}  # runs {{ cookiecutter.package_name }}/__main__.py
```


## FAQ

**How do I sync my environment with the latest `uv.lock`?**
Run `uv sync`. This resolves and installs exactly what's in `uv.lock`, and removes anything no longer
needed — your environment always matches the lockfile.

**How do I add or change packages?**
Use `uv add <package>` / `uv add --dev <package>` / `uv remove <package>`. These edit
`pyproject.toml`, update `uv.lock`, and install into `.venv` in one step. You can also edit the
`dependencies` / `[dependency-groups]` in `pyproject.toml` by hand and then run `uv lock` + `uv sync`.

**How do I upgrade dependencies?**
See [docs/updating_requirements.md](updating_requirements.md).

**Do I need to activate the virtualenv?**
No — `uv run <cmd>` runs inside `.venv` automatically. If you prefer an activated shell, run
`source .venv/bin/activate` (direnv does this for you if configured — see [.envrc](../.envrc)).

**What about `requirements.txt`?**
It's generated from `uv.lock` by the `uv-export` pre-commit hook — don't edit it by hand. `uv.lock`
remains the source of truth.
