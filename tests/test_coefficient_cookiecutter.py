"""Tests for the cookiecutter template itself (not the projects it generates).

These use the ``pytest-cookies`` plugin, which bakes the template into a temporary
directory so we can assert on the generated output.

Usage:
    uv run pytest --ignore='{{cookiecutter.repo_name}}'
"""

from __future__ import annotations

import pytest

# Files that legitimately contain Jinja/`{% %}` after generation and so are exempt from
# the "no unrendered markers" check (the towncrier fragment template is copied verbatim).
_JINJA_EXEMPT = {"template.md"}


def test_bake_with_defaults(cookies):
    """The template bakes cleanly with the default answers."""
    result = cookies.bake()

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.is_dir()
    assert result.project_path.name == "example-project"


def test_templated_files_are_rendered(cookies):
    """The post-gen hook renames the ``.template`` files and creates ``.env``."""
    project = cookies.bake().project_path

    assert (project / "pyproject.toml").is_file()
    assert (project / ".pre-commit-config.yaml").is_file()
    assert (project / ".env").is_file()
    assert not (project / "pyproject.template.toml").exists()
    assert not (project / ".pre-commit-config.template.yaml").exists()


def test_pyproject_uses_uv_not_poetry(cookies):
    """The generated pyproject is PEP 621 + uv, with no Poetry config."""
    pyproject = (cookies.bake().project_path / "pyproject.toml").read_text()

    assert "[project]" in pyproject
    assert "[tool.uv]" in pyproject
    assert "[tool.poetry]" not in pyproject


def test_disabling_towncrier_removes_doc_and_config(cookies):
    """Turning towncrier off removes its doc and its pyproject config."""
    project = cookies.bake(extra_context={"use_towncrier": "n"}).project_path

    assert not (project / "docs" / "using_towncrier.md").exists()
    assert "towncrier" not in (project / "pyproject.toml").read_text()


@pytest.mark.parametrize(
    ("use_github_actions", "use_dependabot", "workflows", "dependabot"),
    [
        ("y", "y", True, True),
        ("y", "n", True, False),
        ("n", "y", False, True),
        ("n", "n", False, False),
    ],
)
def test_ci_toggles_add_and_remove_the_right_files(
    cookies,
    use_github_actions,
    use_dependabot,
    workflows,
    dependabot,
):
    """Each of the GitHub Actions / Dependabot toggles adds or removes its own files."""
    project = cookies.bake(
        extra_context={
            "use_github_actions": use_github_actions,
            "use_dependabot": use_dependabot,
        },
    ).project_path

    assert (project / ".github" / "workflows" / "main.yaml").exists() is workflows
    assert (project / ".github" / "dependabot.yml").exists() is dependabot
    # .github should only survive if it still holds something.
    assert (project / ".github").exists() is (workflows or dependabot)


def test_invalid_package_name_is_rejected(cookies):
    """The pre-gen hook rejects a project name that isn't a valid Python module."""
    result = cookies.bake(extra_context={"project_name": "123 invalid"})

    assert result.exit_code != 0


def test_no_unrendered_jinja_markers(cookies):
    """No generated text file should contain leftover cookiecutter/Jinja markers."""
    project = cookies.bake().project_path

    for path in project.rglob("*"):
        if not path.is_file() or path.name in _JINJA_EXEMPT or path.suffix == ".lock":
            continue
        try:
            text = path.read_text()
        except (UnicodeDecodeError, OSError):
            continue
        assert "{{ cookiecutter." not in text, f"Unrendered marker in {path}"
        assert "{%" not in text, f"Unrendered Jinja block in {path}"
