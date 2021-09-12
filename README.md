# coefficient-cookiecutter

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for Coefficient projects.

  - GitHub repo: [https://github.com/CoefficientSystems/coefficient-cookiecutter/]


## Project cheatsheet

  - **poetry sync:** `poetry install --no-root --remove-untracked`

## Initial project setup

See `docs/getting_started.md` for how to get up & running.

## Updating Python requirements using Poetry

This project uses Poetry to manage dependencies:
[https://python-poetry.org/docs/](https://python-poetry.org/docs/)

The Poetry virtualenv should activate automatically if you are using
[zsh-autoswitch-virtualenv](https://github.com/MichaelAquilina/zsh-autoswitch-virtualenv). You can
also activate it manually by running `workon dp-security` (preferred) or `poetry shell` (Poetry
created/managed virtualenv).

### Poetry tl;dr

```bash
# Sync your environment with poetry.lock
poetry install --no-root --remove-untracked

# Add and install a new package into your environment (or update an existing one)
# 1. Add a package to pyproject.toml
# 2. Run this
poetry add package@version

# N.B. We lock & export to requirements when you run `pre-commit run --all-files` so you
# shouldn't need to run the commands below yourself.

# Compile all poetry.lock file
poetry update

# Export to requirements.txt (this is for compatibility with team members who may not
# have Poetry; Poetry itself uses poetry.lock when you run `poetry install`)
poetry export -f requirements.txt --output requirements.txt
```

### Poetry FAQ

**How do I sync my environment with the latest `poetry.lock`?**
To install dependencies, simply `cd backend-security` and run `poetry install --no-root --remove-untracked`.
This will resolve & install all deps in `pyproject.toml` via `poetry.lock`. Options:
  - `--no-root` skips installing the repo itself as a Python package
  - `--remove-untracked` removes old dependencies no longer present in the lock file

You may wish to set an alias e.g. `alias poetry-sync='poetry install --no-root --remove-untracked'`

**How do I add/change packages?**
In order to install a new package or remove an old one, please edit `pyproject.toml`
or use either `poetry add package` or `pipx run poetry add package@version` as desired.

**How do I update `poetry.lock` to match new changes in `pyproject.toml`?**
You can run `poetry update`, although this will also get run when you run pre-commit. This fetches
the latest matching versions (according to `pyproject.toml`) and updates `poetry.lock`, and is
equivalent to deleting `poetry.lock` and running `poetry install --no-root` again from scratch.

**What do `~`, `^` and `*` mean?**
Check out the Poetry docs page for [specifying version constraints](https://python-poetry.org/docs/dependency-specification/#version-constraints).
Environment markers are great, e.g. this means "for Python 2.7.* OR Windows, install pathlib2 >=2.2, <3.0"
`pathlib2 = { version = "^2.2", markers = "python_version ~= '2.7' or sys_platform == 'win32'" }`


## Changelog & releases

The format of `CHANGELOG.md` is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

### Using towncrier to create news entries

We use [towncrier](https://github.com/twisted/towncrier) to reduce merge conflicts by generating
`CHANGELOG.md` from news fragments, rather than maintaining it directly. Create a news fragment for
each MR if you would like to ensure your changes are communicated to other project contributors.

```bash
# To create a news entry for an added feature relating to MR !123
# Adding --edit is optional and will open in your default shell's $EDITOR
towncrier create 123.added --edit
```

Top tips:
  - You may wish to add `export EDITOR="code -w"` to your `.zshrc` file to open this directly in VS Code.
  - News fragments should be written in markdown.
  - The generated news fragments live in `.changelog/` and can be easily rewritten as an MR evolves.

We use the following custom types (adapted from [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)):
  - `.added` for new features
  - `.changed` for changes in existing functionality
  - `.deprecated` for soon-to-be removed features
  - `.removed` for now removed features
  - `.fixed` for any bug fixes
  - `.security` in case of vulnerabilities
  - `.analysis` for data analyses
  - `.docs` for documentation improvements
  - `.maintenance` for maintenance tasks & upgrades

### Releasing a new version & updating `CHANGELOG.md`

Release versions are tied to Gitlab milestones and sprints. Release checklist:

1. Review MRs assigned to the release milestone in Gitlab & reallocate to the next release.
2. Run `towncrier build --version=VERSION` (preview with `--draft`)
3. Add a git tag for the release.
