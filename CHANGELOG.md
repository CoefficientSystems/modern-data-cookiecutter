# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<!-- TOWNCRIER -->

## [0.2.2] - 2023-05-20

### Maintenance Changes

  - Bump dependencies


## [0.2.1] - 2023-04-06

### Added

  - Added guidance on how to bump Python version in `CONTRIBUTING.md`
  - Added `name-tests-test` to pre-commit
  - Added `flake8-bugbear`, `flake8-comprehensions`, `flake8-mutable`, and `flake8-simplify` ([#172](https://github.com/CoefficientSystems/coefficient-cookiecutter/issues/172))


### Changed

  - CLI flag interface changed in poetry from --remove-untracked to --sync ([#165](https://github.com/CoefficientSystems/coefficient-cookiecutter/issues/165))
  - Switched flake8 source in pre-commit from Gitlab to GitHub
  - Switched isort source in pre-commit from timothycrosley to pycqa
  - Run poetry in pre-commit as local hook due to issues using the correct (active) Python interpreter ([#172](https://github.com/CoefficientSystems/coefficient-cookiecutter/issues/172))


### Maintenance Changes

  - Bump Python version (to 3.11), pyenv version in CI
  - Updated versions of pre-commit, Python dependencies, pyproject.toml, constraints.txt, GitHub Actions
  - Improved settings.json, improved docs ([#172](https://github.com/CoefficientSystems/coefficient-cookiecutter/issues/172))


## [0.2.0] - 2022-09-10

### Added

  - "Quickstart" document in `docs/` inside generated repo, covering minimum CLI commands required to
    setup a new project (assuming all other dependencies are already installed, e.g. pyenv, direnv)
    ([#19](https://github.com/CoefficientSystems/coefficient-cookiecutter/issues/19))
  - Added CI config for Github Actions / dependabot / CodeQL
    ([#26](https://github.com/CoefficientSystems/coefficient-cookiecutter/pull/26))
  - Automate manual testing of generated project
    ([#55](https://github.com/CoefficientSystems/coefficient-cookiecutter/issues/55))
  - Add [jupyter-black](https://github.com/n8henrie/jupyter-black) configuration
    ([#37](https://github.com/CoefficientSystems/coefficient-cookiecutter/issues/37))
  - Set PYTHONBREAKPOINT to use ipdb for an improved debugging experience
    ([#87](https://github.com/CoefficientSystems/coefficient-cookiecutter/pull/87/))

### Improved Documentation

  - Improved the README & added CONTRIBUTORS.md guide ([#96](https://github.com/CoefficientSystems/coefficient-cookiecutter/pull/96))
  - Various improvements to docs; added `use_gcloud` and `use_jupyter` CLI commands; better
    detect-secrets config ([#25](https://github.com/CoefficientSystems/coefficient-cookiecutter/pull/25))

### Maintenance Changes

  - Upgraded base repo to Python 3.9.10; dependency upgrades with poetryup; added prettier, pip-audit, TOML formatting, CI badge
    ([#27](https://github.com/CoefficientSystems/coefficient-cookiecutter/pull/27))
  - Update dependencies (poetryup, precommit, CI)
    ([#56](https://github.com/CoefficientSystems/coefficient-cookiecutter/issues/56) and
    [#108](https://github.com/CoefficientSystems/coefficient-cookiecutter/issues/108))

### Bug Fixes

  - Fix poetryup bug ([#51](https://github.com/CoefficientSystems/coefficient-cookiecutter/issues/51))

## [0.1.0] - 2021-09-13

### Added

  - Added towncrier ([#8](https://github.com/CoefficientSystems/coefficient-cookiecutter/issues/8))
  - Add linters, pyproject.toml and .vscode/settings.json ([#10](https://github.com/CoefficientSystems/coefficient-cookiecutter/issues/10))
  - Add .gitignore ([#12](https://github.com/CoefficientSystems/coefficient-cookiecutter/issues/12))
  - Added pre-commit, various flake8 plugins and detect-secrets ([#14](https://github.com/CoefficientSystems/coefficient-cookiecutter/issues/14))
