# Project-specific setup

This document contains setup instructions specifically for this project only. This design enables
us to keep other docs easily aligned with future upstream changes to
[coefficient-cookiecutter](https://github.com/CoefficientSystems/coefficient-cookiecutter/).


## Install system-level dependencies with [homebrew](https://brew.sh/)

```sh
# brew install wkhtmltopdf
```

{% if cookiecutter.use_gcloud == 'y' -%}
## gcloud setup

Install [gcloud as per these instructions](https://cloud.google.com/sdk/docs/install).

Run `gcloud init` to create a new named configuration. Unless it exists already, create a new
configuration as required, e.g. `{{ cookiecutter.virtualenv }}`. This configuration can be activated at any
point, for example:

```sh
gcloud config set project {{ cookiecutter.virtualenv }}

# Top tip: install tldr to get quick help with gcloud commands!
# https://dbrgn.github.io/tealdeer/
brew install tealdeer
tldr gcloud
```

{% endif %}
{% if cookiecutter.use_jupyter == 'y' -%}
## Jupyter kernel

```sh
python -m ipykernel install --user --name {{ cookiecutter.virtualenv }} --display-name "Python ({{ cookiecutter.virtualenv }})"
```

{% endif %}
