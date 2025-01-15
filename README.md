# CRM Skautoteka - Analysis module (Polars/FastAPI)

-   [Introduction](#introduction)
-   [Prerequisites](#prerequisites)
-   [Installation](#installation)
-   [Starting the Development Server](#starting-the-development-server)
-   [Formating and linting](#formating-and-linting)
-   [Testing](#testing)

## Introduction

The `crm-analysis` project is an endpoint for the Skautoteka project. Its purpose is to calculate averages
of players traits and to find players which have traits which are given by predicates.

## Project structure

The app is in the `app` folder. It has the following files:

- **config.py**
  - loads the configuration of the project from the `.env` file

- **main.py**
  - has the code of the `/analyze/` endpoint

- **test_main.py**
  - contains the unit tests of the `/analyze/` endpoint

## Prerequisites

You will have to have `uv` on your system. Follow the
[instalation instructions](https://docs.astral.sh/uv/getting-started/installation/).

## Installation

First install uv (see [Prerequisites](#prerequisites)). Then create virtual environment with `uv venv`. Install with `uv pip install -r pyproject.toml`. If you need development or testing dependencies
install them with (accordingly): `uv pip install -r pyproject.toml --extra development` and 
`uv pip install -r pyproject.toml --extra testing`.

To install all dependencies run `uv pip install -r pyproject.toml --all-extras`.

## Configuration

Optionally create the .env file in root directory of the project. If you don't create it, project will
have default settings.

Example .env file with default settings:

```shell
BACKEND_URL=http://localhost:3000/api/
```

## Starting the development server

Start the development server with `uv run fastapi dev app/main.py`. It will be available on localhost
on port 8000.

## Formating and linting

Format the code with `uv run ruff format`. Lint with `uv run ruff check `.
To automatically apply fixes (mainly to sort imports) run `uv run ruff check --fix`.

## Testing

Test with `uv run pytest`.
