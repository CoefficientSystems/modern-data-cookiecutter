# {{ cookiecutter.project_name }}

[![CI]({{cookiecutter.repo_url}}/actions/workflows/main.yaml/badge.svg)]({{cookiecutter.repo_url}}/actions/workflows/main.yaml)

{{ cookiecutter.project_short_description }}

## Project cheatsheet

  - **pre-commit:** `pre-commit run --all-files`
  - **pytest:** `pytest` or `pytest -s`
  - **coverage:** `coverage run -m pytest` or `coverage html`
  - **poetry sync:** `poetry install --no-root --sync`
  - **updating requirements:** see [docs/updating_requirements.md](docs/updating_requirements.md)
{% if cookiecutter.use_towncrier == 'y' -%}
  - **create towncrier entry:** `towncrier create 123.added --edit`{% endif %}


## Initial project setup

1. See [docs/getting_started.md](docs/getting_started.md) or [docs/quickstart.md](docs/quickstart.md)
   for how to get up & running.
2. Check [docs/project_specific_setup.md](docs/project_specific_setup.md) for project specific setup.
3. See [docs/using_poetry.md](docs/using_poetry.md) for how to update Python requirements using
   [Poetry](https://python-poetry.org/).
4. See [docs/ripsecrets.md](docs/ripsecrets.md) for more on maintaining a `.secretsignore`
   file using [ripsecrets](https://github.com/sirwart/ripsecrets).
{% if cookiecutter.use_towncrier == 'y' -%}
5. See [docs/using_towncrier.md](docs/using_towncrier.md) for how to update the `CHANGELOG.md`
   using [towncrier](https://github.com/twisted/towncrier). {% endif %}
