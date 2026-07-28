# Updating requirements

We use [uv](https://docs.astral.sh/uv/) to keep dependencies up to date. See
[docs/using_uv.md](using_uv.md) for day-to-day dependency management.

To upgrade everything to the latest versions allowed by the constraints in `pyproject.toml`:

```sh
# Create a feature branch first, then:
uv lock --upgrade          # bump uv.lock to the latest compatible versions
uv sync                     # install the upgraded versions into .venv
uv run pre-commit run --all-files --hook-stage=manual
uv run pytest
# Review the uv.lock diff, then commit & push
```

To upgrade a single package:

```sh
uv lock --upgrade-package pandas
uv sync
```

If a newer version needs a wider constraint than `pyproject.toml` currently allows, update the
specifier (e.g. `uv add "pandas>=3"`) and re-run the steps above. uv's resolver reports a clear
error if two packages have incompatible requirements.
