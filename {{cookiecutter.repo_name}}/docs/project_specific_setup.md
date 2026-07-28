# Project-specific setup

This document contains setup instructions specifically for this project only. This design enables
us to keep other docs easily aligned with future upstream changes to
[modern-data-cookiecutter](https://github.com/CoefficientSystems/modern-data-cookiecutter/).


## Install system-level dependencies with [homebrew](https://brew.sh/)

```sh
# brew install wkhtmltopdf
```
{%- if cookiecutter.use_gcloud == 'y' %}

## gcloud setup

Install [gcloud as per these instructions](https://cloud.google.com/sdk/docs/install).

Run `gcloud init` to create a new named configuration. Unless it exists already, create a new
configuration as required, e.g. `{{ cookiecutter.repo_name }}`. This configuration can be activated at any
point, for example:

```sh
gcloud config set project {{ cookiecutter.repo_name }}

# Top tip: install tldr to get quick help with gcloud commands!
# https://dbrgn.github.io/tealdeer/
brew install tealdeer
tldr gcloud
```
{%- endif %}
{%- if cookiecutter.use_jupyter == 'y' %}

## Jupyter kernel

`ipykernel` is installed as a dev dependency. Register a kernel for this project's virtualenv so it
shows up in Jupyter:

```sh
uv run python -m ipykernel install --user --name {{ cookiecutter.repo_name }} --display-name "Python ({{ cookiecutter.repo_name }})"
```

Launch JupyterLab with `uv run jupyter lab`.
{%- endif %}
