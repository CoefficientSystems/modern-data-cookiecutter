# Modern Data Cookiecutter

<!-- badges-begin -->

[![Status][status badge]][status badge]
![Python Version][python version badge]
[![Tests][github actions badge]][github actions page]
[![pre-commit enabled][pre-commit badge]][pre-commit project]
[![Ruff][ruff badge]][ruff project]

[github actions badge]: https://github.com/CoefficientSystems/modern-data-cookiecutter/actions/workflows/main.yaml/badge.svg
[github actions page]: https://github.com/CoefficientSystems/modern-data-cookiecutter/actions/workflows/main.yaml?query=workflow%3ACI
[pre-commit badge]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
[pre-commit project]: https://pre-commit.com/
[python version badge]: https://img.shields.io/badge/python-3.12-blue
[ruff badge]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
[ruff project]: https://github.com/astral-sh/ruff
[status badge]: https://badgen.net/badge/status/alpha/d8624d

<!-- badges-end -->

Modern [Cookiecutter] template for Python-based data
science/engineering/analytics projects. Created by [Coefficient].

Inspired by:
  - [cookiecutter-data-science]
  - [cookiecutter-hypermodern-python]
  - [govcookiecutter]


## Usage

```sh
# uv can run cookiecutter without installing it
uvx cookiecutter https://github.com/CoefficientSystems/modern-data-cookiecutter

# Follow instructions in docs/getting_started.md or docs/quickstart.md
```

(Don't have uv yet? `brew install uv` or see [the uv docs][uv].)


## Features

<!-- features-begin -->

### 📦 Managing Python & Package Dependencies
  - Python version, virtualenv, dependencies & lockfile all managed by [uv]
  - A single `uv sync` bootstraps everything; `uv.lock` pins exact versions
  - A `requirements.txt` is auto-exported from the lockfile for tooling that doesn't use uv
  - Automated dependency upgrades with [Dependabot]

### 👷 Code Quality, Testing & CI
  - Linting **and** formatting with [Ruff] (replaces Flake8, isort, Black, pyupgrade & more)
  - Testing with [pytest]
  - Continuous integration with [GitHub Actions]
  - [Twelve Factor] app principles

### 🤖 Data Science
  - Jupyter Lab configured and linted/formatted by Ruff (notebooks included)
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
  - [VS Code Settings] configures features like "Format on save", bracket pair colorization, Pylance
    and the Ruff extension alongside recommended extensions
  - Automated release notes using [towncrier]

<!-- features-end -->

## Contributing

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidance on how to request features, report
issues, setup a development environment, test this cookiecutter and contribute to development.

[coefficient]: https://coefficient.ai
[cookiecutter-data-science]: https://drivendata.github.io/cookiecutter-data-science/
[cookiecutter-hypermodern-python]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
[cookiecutter]: https://github.com/cookiecutter/cookiecutter
[dependabot]: https://github.com/dependabot
[detect-secrets]: https://github.com/yelp/detect-secrets
[direnv]: https://direnv.net/
[github actions]: https://github.com/features/actions
[govcookiecutter]: https://best-practice-and-impact.github.io/govcookiecutter/#govcookiecutter
[pip-audit]: https://pypi.org/project/pip-audit/
[pre-commit]: https://pre-commit.com/
[pytest]: https://docs.pytest.org/
[ruff]: https://docs.astral.sh/ruff/
[towncrier]: https://github.com/twisted/towncrier
[twelve factor]: https://12factor.net/
[uv]: https://docs.astral.sh/uv/
[vs code settings]: https://code.visualstudio.com/docs/getstarted/settings
