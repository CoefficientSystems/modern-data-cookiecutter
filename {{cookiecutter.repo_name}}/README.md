# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## Project cheatsheet

  - **poetry sync:** `poetry install --no-root --remove-untracked`
{% if cookiecutter.use_towncrier == 'y' -%}
  - **create towncrier entry:** `towncrier create 123.added --edit`{% endif %}


## Initial project setup

1. See [docs/getting_started.md] for how to get up & running.
2. See [docs/using_poetry.md] for how to update Python requirements using
   [Poetry](https://python-poetry.org/).
{% if cookiecutter.use_towncrier == 'y' -%}
3. See [docs/using_towncrier.md] for how to update the `CHANGELOG.md` using
   [towncrier](https://github.com/twisted/towncrier).{% endif %}
