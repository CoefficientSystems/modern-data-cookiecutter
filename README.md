# coefficient-cookiecutter

<!-- badges-begin -->

[![Status][status badge]][status badge]
![Python Version][python version badge]
[![Tests][github actions badge]][github actions page]
[![pre-commit enabled][pre-commit badge]][pre-commit project]
[![Black codestyle][black badge]][black project]

[black badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black project]: https://github.com/psf/black
[github actions badge]: https://github.com/CoefficientSystems/coefficient-cookiecutter/actions/workflows/main.yaml/badge.svg
[github actions page]: https://github.com/CoefficientSystems/coefficient-cookiecutter/actions/workflows/main.yaml?query=workflow%3ACI
[pre-commit badge]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
[pre-commit project]: https://pre-commit.com/
[python version badge]: https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue
[status badge]: https://badgen.net/badge/status/alpha/d8624d

<!-- badges-end -->

Modern [Cookiecutter] template for Python-based data
science/engineering/analytics projects. Made by [Coefficient].

Inspired by:
  - [cookiecutter-data-science]
  - [cookiecutter-hypermodern-python]
  - [govcookiecutter]


## Usage

```sh
# Install cookiecutter (if you haven't already done so)
pipx install cookiecutter

# Install the latest release directly from this repo
cookiecutter https://github.com/CoefficientSystems/coefficient-cookiecutter

# Follow instructions in docs/getting_started.md or docs/quickstart.md
```


## Features

<!-- features-begin -->

### 📦 Managing Python & Package Dependencies
  - Work across multiple Python versions using [pyenv]
  - Virtualenv management using [virtualenv] and [pyenv-virtualenv]
  - Packaging and dependency management with [Poetry]
  - Automated dependency upgrades with [poetry-plugin-up] and [Dependabot]

### 👷 Code Quality, Testing & CI
  - Linting pre-configured using [pre-commit], [Flake8] and [pylint]
  - Code auto-formatting with [Black], [autoflake], [add-trailing-comma]
  - Import sorting with [isort]
  - Automated Python syntax upgrades with [pyupgrade]
  - Testing with [pytest]
  - Continuous integration with [GitHub Actions]
  - [Twelve Factor] app principles

### 🤖 Data Science
  - Jupyter Lab/Notebook configured with [jupyter-black] autoformatter
  - Directory structure designed [specifically for data science & analytics
    projects](https://drivendata.github.io/cookiecutter-data-science/#directory-structure) (adapted
    from [cookiecutter-data-science])

### 🔒 Security Features
  - Security audit with [pip-audit] and [detect-secrets]
  - Keep secrets & config out of code by loading as environment variables using [direnv]


## 📚 Documentation, IDE Settings & Release Notes
  - Get started easily using [Getting Started]({{cookiecutter.repo_name}}/docs/getting_started.md) or
    the [Quickstart]({{cookiecutter.repo_name}}/docs/quickstart.md) with further documentation on how
    to use the packages in this cookiecutter available in [docs/]({{cookiecutter.repo_name}}/docs/)
  - [VS Code Settings] configures features like "Format on save", isort configuration, bracket pair
    colorization, Pylance and mypy alongside recommended extensions
  - Automated release notes using [towncrier]

<!-- features-end -->

## Contributing

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidance on how to request features, report
issues, setup a development environment, test this cookiecutter and contribute to development.

[add-trailing-comma]: https://github.com/asottile/add-trailing-comma
[autoflake]: https://github.com/pycqa/autoflake
[black]: https://github.com/psf/black
[coefficient]: https://coefficient.ai
[cookiecutter-data-science]: https://drivendata.github.io/cookiecutter-data-science/
[cookiecutter-hypermodern-python]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
[cookiecutter]: https://github.com/cookiecutter/cookiecutter
[dependabot]: https://github.com/dependabot
[detect-secrets]: https://github.com/yelp/detect-secrets
[direnv]: https://direnv.net/
[flake8]: https://flake8.pycqa.org/
[github actions]: https://github.com/features/actions
[govcookiecutter]: https://best-practice-and-impact.github.io/govcookiecutter/#govcookiecutter
[isort]: https://pycqa.github.io/isort/
[jupyter-black]: https://pypi.org/project/jupyter-black/
[pip-audit]: https://pypi.org/project/pip-audit/
[poetry]: https://python-poetry.org/
[poetry-plugin-up]: https://github.com/MousaZeidBaker/poetry-plugin-up
[pre-commit]: https://pre-commit.com/
[pyenv-virtualenv]: https://github.com/pyenv/pyenv-virtualenv
[pyenv]: https://github.com/pyenv/pyenv
[pylint]: https://pypi.org/project/pylint/
[pytest]: https://docs.pytest.org/
[pyupgrade]: https://github.com/asottile/pyupgrade
[towncrier]: https://github.com/twisted/towncrier
[twelve factor]: https://12factor.net/
[virtualenv]: https://pypi.org/project/virtualenv/
[vs code settings]: https://code.visualstudio.com/docs/getstarted/settings
