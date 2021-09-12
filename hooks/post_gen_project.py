from __future__ import annotations

import os
from pathlib import Path

PROJECT_DIRECTORY = Path(".")


if __name__ == "__main__":

    # Rename pyproject-template.toml -> pyproject.toml
    os.rename(PROJECT_DIRECTORY / "pyproject-template.toml", PROJECT_DIRECTORY / "pyproject.toml")

    if "{{ cookiecutter.use_towncrier }}" != "y":
        os.remove(PROJECT_DIRECTORY / "docs" / "using_towncrier.md")
