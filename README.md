# coefficient-cookiecutter

<!-- badges-begin -->

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
[![CI](https://github.com/CoefficientSystems/coefficient-cookiecutter/actions/workflows/main.yaml/badge.svg)](https://github.com/CoefficientSystems/coefficient-cookiecutter/actions/workflows/main.yaml)

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for Coefficient projects.

  - GitHub repo: [https://github.com/CoefficientSystems/coefficient-cookiecutter/]


## Usage

```bash
# Install cookiecutter
pipx install cookiecutter

# Install from local
cookiecutter /path/to/coefficient-cookiecutter/

# Install from repo
cookiecutter https://github.com/CoefficientSystems/coefficient-cookiecutter
```

## Features

<!-- features-begin -->

- Packaging and dependency management with [Poetry]
- Linting with [pre-commit]
- CI with [GitHub Actions]
- Automated dependency updates with [Dependabot]
- Code formatting with [Black] and [pylint]
- Import sorting with [isort]
- Testing with [pytest]

<!-- features-end -->

## Contributing

This cookiecutter project is self-referential (!) and conforms to the guidelines outlined in the generated
cookiecutter documentation. Please refer to [{{cookiecutter.repo_name}}/README.md]({{cookiecutter.repo_name}}/README.md)
and [{{cookiecutter.repo_name}}/docs/]({{cookiecutter.repo_name}}/docs/) for advice on how to contribute.
