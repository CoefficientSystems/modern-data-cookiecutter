"""Python that runs before the project is generated.

Read more: https://cookiecutter.readthedocs.io/en/1.7.3/advanced/hooks.html
"""

from __future__ import annotations

import logging
import re
import sys

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

module_name = "{{ cookiecutter.package_name}}"

if not re.match(MODULE_REGEX, module_name):
    logging.error(
        f"The project slug ({module_name}) is not a valid Python module name. "
        "Please do not use a - and use _ instead",
    )

    # Exit to cancel project
    sys.exit(1)
