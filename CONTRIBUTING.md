# Contributor Guide

Your contributions to modern-data-cookiecutter are very welcome, and credit will always be given.


## How to request a feature

Request features on the [Issue Tracker].


## How to report a bug

Report bugs on the [Issue Tracker].

When filing an issue, make sure to answer these questions:
    - Which operating system and Python version are you using?
    - Which version of this project are you using?
    - What did you do?
    - What did you expect to see?
    - What did you see instead?

The best way to get your bug fixed is to provide a test case, and/or steps to reproduce the issue.


## How to set up your development environment

This cookiecutter project is self-referential (!) and conforms to the guidelines outlined in the
generated cookiecutter documentation. For example, there is an "outer repo" `README.md` as well as
the "inner repo" README template found at `{{cookiecutter.repo_name}}/README.md`.

First, install [uv](https://docs.astral.sh/uv/) (`brew install uv`), which manages the Python
version, virtualenv and dependencies for both this repo (the "outer repo") and the generated project
(the "inner repo"). Then:

```sh
uv sync                       # create .venv and install dependencies
uv run pre-commit install     # install the git hooks
```

Fork the repository on [GitHub] and clone the fork to your local machine. You can now generate a
project from your development version:

```sh
uvx cookiecutter /path/to/modern-data-cookiecutter/
```


## How to test the project

CI (`.github/workflows/main.yaml`) runs the checks below automatically. To run them locally:

```sh
# Lint & unit-test the cookiecutter repo itself
uv run pre-commit run --all-files
uv run pytest --ignore='{{cookiecutter.repo_name}}'

# End-to-end: generate a project and run its full checks
uvx cookiecutter /path/to/modern-data-cookiecutter/ --no-input --output-dir /tmp/baked
cd /tmp/baked/example-project

git init                      # towncrier & pre-commit need a repo
uv sync                       # install Python + deps into .venv
uv run pytest
uv run towncrier create 123.added --edit   # then write something, save & close
uv run towncrier build --version=0.2       # confirm it lands in CHANGELOG.md
uv run pre-commit run --all-files --hook-stage=manual --show-diff-on-failure

# Clean up
cd .. && rm -rf ./example-project
```


## How to submit changes

Please open a [pull request] to submit changes to this project. Your pull request needs to meet the
following guidelines for acceptance:
    - The GitHub Actions CI test suite must pass.
    - Please add a Towncrier entry if appropriate, you can check `docs/using_towncrier.md` for guidance.
    - If your changes add functionality, update the documentation accordingly.

It is recommended to open an issue before starting work on anything. This will allow a chance to
talk it over with the owners and validate your approach.


## Tip: How to bump the default Python version

The repo's own Python version is set in `.python-version`, while the default cookiecutter Python
version is set in `cookiecutter.json` (`python_version`). These don't have to match, though it's
recommended to keep them close. uv will download whichever version is requested, so the main
constraint is that your chosen version is generally available (check
[https://www.python.org/downloads/]).


[github]: https://github.com/CoefficientSystems/modern-data-cookiecutter/
[issue tracker]: https://github.com/CoefficientSystems/modern-data-cookiecutter/issues
[pull request]: https://github.com/CoefficientSystems/modern-data-cookiecutter/pulls
