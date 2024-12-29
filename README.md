# Installing

First install uv. Then create virtual environment with `uv venv`. Install with `uv pip install -r pyproject.toml`. If you need development or testing dependencies
install them with (accordingly): `uv pip install -r pyproject.toml --extra development` and 
`uv pip install -r pyproject.toml --extra testing`.

To install all dependencies run `uv pip install -r pyproject.toml --all-extras`. 

# Running

Start the  test app with `uv run fastapi dev app/main.py`. It will be available on localhost
on port 8000.

# Testing

Test with `uv run pytest`.
