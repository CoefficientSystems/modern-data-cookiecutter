"""Entry point so the package can be run with `python -m {{ cookiecutter.package_name }}`.

Replace the body of `main()` with your project's real entry point (e.g. a CLI).
"""

from __future__ import annotations

from {{ cookiecutter.package_name }} import __version__


def main() -> None:
    """Run the package."""
    print(f"Hello from {{ cookiecutter.package_name }} v{__version__}!")  # noqa: T201


if __name__ == "__main__":
    main()
