"""Python that runs after the project is generated.

Read more: https://cookiecutter.readthedocs.io/en/stable/advanced/hooks.html
"""

from __future__ import annotations

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

    # Remove the optional pieces the user didn't opt into. These deletions are intentionally
    # unguarded: if one fails we want generation to abort loudly rather than hand back a
    # half-configured project that reports success.
    if "{{ cookiecutter.use_towncrier }}" != "y":
        (PROJECT_DIRECTORY / "docs" / "using_towncrier.md").unlink()

    if "{{ cookiecutter.use_github_actions }}" != "y":
        shutil.rmtree(PROJECT_DIRECTORY / ".github" / "workflows")

    if "{{ cookiecutter.use_dependabot }}" != "y":
        (PROJECT_DIRECTORY / ".github" / "dependabot.yml").unlink()

    # Drop the now-empty .github directory if neither GitHub Actions nor Dependabot is used.
    github_dir = PROJECT_DIRECTORY / ".github"
    if github_dir.is_dir() and not any(github_dir.iterdir()):
        github_dir.rmdir()
