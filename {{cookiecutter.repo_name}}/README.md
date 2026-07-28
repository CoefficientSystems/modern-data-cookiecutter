# {{ cookiecutter.project_name }}

[![CI]({{cookiecutter.repo_url}}/actions/workflows/main.yaml/badge.svg)]({{cookiecutter.repo_url}}/actions/workflows/main.yaml)

{{ cookiecutter.project_short_description }}

## Project cheatsheet

  - **sync environment:** `uv sync`
  - **add / remove a package:** `uv add <pkg>` / `uv add --dev <pkg>` / `uv remove <pkg>`
  - **run a command in the env:** `uv run <cmd>` (e.g. `uv run python -m {{ cookiecutter.package_name }}`)
  - **pytest:** `uv run pytest` or `uv run pytest -s`
  - **pre-commit:** `uv run pre-commit run --all-files`
  - **updating requirements:** see [docs/updating_requirements.md](docs/updating_requirements.md)
{%- if cookiecutter.use_towncrier == 'y' %}
  - **create towncrier entry:** `uv run towncrier create 123.added --edit`
{%- endif %}


## Initial project setup

1. See [docs/getting_started.md](docs/getting_started.md) or [docs/quickstart.md](docs/quickstart.md)
   for how to get up & running.
2. Check [docs/project_specific_setup.md](docs/project_specific_setup.md) for project specific setup.
3. See [docs/using_uv.md](docs/using_uv.md) for how to manage Python dependencies using
   [uv](https://docs.astral.sh/uv/).
4. See [docs/detect_secrets.md](docs/detect_secrets.md) for more on creating a `.secrets.baseline`
   file using [detect-secrets](https://github.com/Yelp/detect-secrets).
{%- if cookiecutter.use_towncrier == 'y' %}
5. See [docs/using_towncrier.md](docs/using_towncrier.md) for how to update the `CHANGELOG.md`
   using [towncrier](https://github.com/twisted/towncrier).
{%- endif %}
