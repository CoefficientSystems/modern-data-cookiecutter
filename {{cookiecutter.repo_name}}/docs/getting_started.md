# Getting Started

This document contains instructions to get a fully working development environment for this repo.
We use [**uv**](https://docs.astral.sh/uv/) to manage the Python version, the virtualenv, and all
dependencies with a single tool — it replaces `pyenv`, `virtualenvwrapper`, `pip` and `poetry`.


## 1. Install uv

macOS (recommended):

```sh
brew install uv
```

Or, on any platform:

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Keep uv up to date with `uv self update` (or `brew upgrade uv`). See the
[uv docs](https://docs.astral.sh/uv/) for more.


## 2. Get the repo & create the environment

⚠️ Replace `REPO_GIT_URL` with the actual URL of your GitHub repo.

```sh
git clone ${REPO_GIT_URL}
cd {{ cookiecutter.repo_name }}

# Install the Python version pinned in .python-version (uv downloads it if needed),
# create the .venv virtualenv, and install all dependencies from uv.lock.
uv sync
```

`uv sync` is the one command you need to get (or re-sync) a working environment. Either activate the
virtualenv (`source .venv/bin/activate`) or prefix commands with `uv run` (e.g. `uv run pytest`).


## 3. Install the pre-commit hooks

```sh
uv run pre-commit install
```


## 4. Add secrets into .env

  - Run `cp .env.template .env` and update the secrets.
  - [Install direnv](https://direnv.net/) to autoload the environment variables in `.env` and
    auto-activate the virtualenv (see [.envrc](../.envrc)).
  - Run `direnv allow` to authorise direnv (re-run whenever you change `.env`).


## 5. Initialise the `detect-secrets` pre-commit hook

We use [`detect-secrets`](https://github.com/Yelp/detect-secrets) to check that no secrets are
accidentally committed. This repo ships with a `.secrets.baseline` so the hook works out of the box;
please read [docs/detect_secrets.md](detect_secrets.md) for more, including how to regenerate it:

```shell
# Regenerate the baseline (adjust exclusions in .pre-commit-config.yaml as needed)
uv run detect-secrets scan \
    --exclude-files 'uv\.lock' \
    --exclude-files '\.secrets\.baseline' \
    --exclude-files '\.env\.template' \
    --exclude-secrets 'password|ENTER_PASSWORD_HERE|INSERT_API_KEY_HERE' \
    --exclude-lines 'integrity=*sha' \
    > .secrets.baseline

# Audit the generated baseline
uv run detect-secrets audit .secrets.baseline
```


## 6. Project-specific setup

Please check [docs/project_specific_setup.md](project_specific_setup.md) for further instructions.
