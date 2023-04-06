# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<!-- TOWNCRIER -->

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
