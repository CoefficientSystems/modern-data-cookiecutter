The exported `requirements.txt` now contains runtime dependencies only (`uv export --no-default-groups`), matching its intended use as a deploy manifest rather than the full dev environment.
