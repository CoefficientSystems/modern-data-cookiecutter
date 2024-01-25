"""Python that runs after the project is generated.

Read more: https://cookiecutter.readthedocs.io/en/1.7.3/advanced/hooks.html
"""

from __future__ import annotations

import logging
import shutil
from pathlib import Path

PROJECT_DIRECTORY = Path()

if __name__ == "__main__":
    # Rename templated files
    (PROJECT_DIRECTORY / "pyproject.template.toml").rename(PROJECT_DIRECTORY / "pyproject.toml")
    (PROJECT_DIRECTORY / ".pre-commit-config.template.yaml").rename(
        PROJECT_DIRECTORY / ".pre-commit-config.yaml",
    )

    # Copy .env.template -> .env
    shutil.copy(PROJECT_DIRECTORY / ".env.template", PROJECT_DIRECTORY / ".env")

    if "{{ cookiecutter.use_towncrier }}" != "y":
        (PROJECT_DIRECTORY / "docs" / "using_towncrier.md").unlink()

    if "{{ cookiecutter.use_github_actions }}" != "y":
        try:
            shutil.rmtree(PROJECT_DIRECTORY / ".github" / "workflows")
        except Exception:  # pylint: disable=broad-except
            logging.exception("failed to delete .github/workflows")

        # Don't need .github if using neither GitHub Actions nor dependabot
        if "{{ cookiecutter.use_dependabot }}" != "y":
            try:
                shutil.rmtree(PROJECT_DIRECTORY / ".github")
            except Exception:  # pylint: disable=broad-except
                logging.exception("failed to delete .github")
