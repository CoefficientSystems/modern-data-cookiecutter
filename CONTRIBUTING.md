# Contributor Guide

Your contributions to coefficient-cookiecutter are very welcome, and credit will always be given.

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

First, set up your environment tooling by following the instructions in [Getting
Started]({{cookiecutter.repo_name}}/docs/getting_started.md) to install tools such as pyenv,
pyenv-virtualenv, Poetry, direnv that are utilised by this project (the "outer repo") as well as the
generated project (the "inner repo").

Fork the repository on [GitHub] and clone the fork to your local machine. You can now generate a
project from your development version:

```sh
cookiecutter path/to/coefficient-cookiecutter
```

Follow the instructions below for a full test including installing cookiecutter, generating a
project using this cookiecutter, initialising a Python environment including a Poetry-controlled
virtualenv based on the Python version specified during cookiecutter configuration, installing
packages, running the test suite, adding a Towncrier update, and running pre-commit.

## How to test the project

```sh
pipx install cookiecutter
cookiecutter /path/to/coefficient-cookiecutter/
# Use project defaults
cd coefficient-project

# Install Python & dependencies
pyenv shell $(cat .python-version)
python -V  # check this is the correct version of Python
mkvirtualenv $(cat .venv)
python -V  # check this is the correct version of Python
python -m pip install --upgrade pip
poetry install --no-root --remove-untracked

# Run tests
pytest

# Towncrier & pre-commit require us to be in a repo
git init

# Test towncrier (if installed)
towncrier create 123.added --edit
# Write something, save, close
towncrier build --version=0.2
# Confirm your update is now in CHANGELOG.md

# Test out pre-commit
pre-commit run --all-files --hook-stage=manual --show-diff-on-failure

# Clean up
deactivate
rmvirtualenv $(cat .venv)
rm -rf ./.git/
cd ..
rm -r ./coefficient-project
```

## How to submit changes

Please open a [pull request] to submit changes to this project. Your pull request needs to meet the
following guidelines for acceptance:

- The GitHub Actions CI test suite must pass.
- Please add a Towncrier entry if appropriate, you can check `docs/using_towncrier.md` for guidance.
- If your changes add functionality, update the documentation accordingly.

It is recommended to open an issue before starting work on anything. This will allow a chance to
talk it over with the owners and validate your approach.

[github]: https://github.com/CoefficientSystems/coefficient-cookiecutter/
[issue tracker]: https://github.com/CoefficientSystems/coefficient-cookiecutter/issues
[pull request]: https://github.com/CoefficientSystems/coefficient-cookiecutter/pulls
