# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## Project cheatsheet

  - **pre-commit:** `pre-commit run --all-files`
  - **pytest:** `pytest` or `pytest -s`
  - **coverage:** `coverage run -m pytest` or `coverage html`
  - **poetry sync:** `poetry install --no-root --remove-untracked`
{% if cookiecutter.use_towncrier == 'y' -%}
  - **create towncrier entry:** `towncrier create 123.added --edit`{% endif %}


## Initial project setup

1. See [docs/getting_started.md] for how to get up & running.
2. See [docs/using_poetry.md] for how to update Python requirements using
   [Poetry](https://python-poetry.org/).
3. See [docs/detect_secrets.md] for more on creating a `.secrets.baseline` file using
   [detect-secrets](https://github.com/Yelp/detect-secrets).
{% if cookiecutter.use_towncrier == 'y' -%}
4. See [docs/using_towncrier.md] for how to update the `CHANGELOG.md` using
   [towncrier](https://github.com/twisted/towncrier).{% endif %}
