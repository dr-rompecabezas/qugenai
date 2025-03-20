# QuGenAI

[![Build Status](https://github.com/think-elearn/qugenai/actions/workflows/ci.yml/badge.svg)](https://github.com/think-elearn/qugenai/actions)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/think-elearn/qugenai/main.svg)](https://results.pre-commit.ci/latest/github/think-elearn/qugenai/main)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

This is a proof-of-concept project that demonstrates how to use the OpenAI API to generate [structured outputs](https://platform.openai.com/docs/guides/structured-outputs). It is a simple [nanodjango](https://github.com/radiac/nanodjango) app that allows users to input a subject and receive a few questions as output.

## Requirements

- Python 3.9+
- Your own [OpenAI API key](https://platform.openai.com/api-keys)

## Installation

Clone the repository and install the dependencies with [uv](https://docs.astral.sh/uv/).

```shell
git clone https://github.com/thinkelearn/qugenai
cd qugenai
uv sync
```

## Usage

Export your OpenAI API key as an environment variable.

```shell
uv run nanodjango run app.py
```

Then, navigate to <http://localhost:8000> in your browser.

## Testing

```shell
uv run pytest tests.py
```

## Screenshot

![QuGenAI application interface](https://github.com/user-attachments/assets/c969cf0b-359a-4a80-9aee-ffe017bb2dc4)

