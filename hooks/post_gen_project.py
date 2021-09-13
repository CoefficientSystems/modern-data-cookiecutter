"""Python that runs after the project is generated.

Read more: https://cookiecutter.readthedocs.io/en/1.7.3/advanced/hooks.html
"""

from __future__ import annotations

import os
import shutil
from pathlib import Path

PROJECT_DIRECTORY = Path(".")


if __name__ == "__main__":

    # Rename templated files
    os.rename(PROJECT_DIRECTORY / "pyproject.template.toml", PROJECT_DIRECTORY / "pyproject.toml")
    os.rename(
        PROJECT_DIRECTORY / ".pre-commit-config.template.yaml",
        PROJECT_DIRECTORY / ".pre-commit-config.yaml",
    )

    # Copy .env.template -> .env
    shutil.copy(PROJECT_DIRECTORY / ".env.template", PROJECT_DIRECTORY / ".env")

    if "{{ cookiecutter.use_towncrier }}" != "y":
        os.remove(PROJECT_DIRECTORY / "docs" / "using_towncrier.md")
