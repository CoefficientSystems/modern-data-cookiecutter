# Quickstart

This document contains instructions _only_ to get a fully working development environment for this
repo. For prerequisites (e.g. how to install uv) plus details on what's being installed and why,
please see [docs/getting_started.md](getting_started.md).

We assume [**uv**](https://docs.astral.sh/uv/) and (optionally) [direnv](https://direnv.net/) are
installed.


## Part 1: Environment setup

```sh
# Get the repo
git clone ${REPO_GIT_URL}
cd {{ cookiecutter.repo_name }}

# Install Python + create .venv + install all dependencies from uv.lock
uv sync

# Install the git pre-commit hooks
uv run pre-commit install

# Create your .env for secrets (then edit it)
cp .env.template .env
direnv allow  # optional, if using direnv
```

Run any command inside the project environment with `uv run`, e.g. `uv run pytest`.


## Part 2: Project-specific setup

Please check [docs/project_specific_setup.md](project_specific_setup.md) for further instructions.
