---
sidebar_position: 33
---

# graphrag/config/read_dotenv.py

## Overview

Utility to load environment variables from a .env file located under a given root directory into the process environment.

Purpose:
Provide a lightweight helper to read a .env file located at root/.env and populate os.environ with its variables, without overwriting existing environment values. If the .env file is missing, no variables are loaded.

Key exports:
- read_dotenv(root: str) -&gt; None: Read and apply variables from root/.env into the current process environment without overwriting existing keys.

Args:
- root: Path to the root directory that should contain the .env file.

Returns:
- None

Raises:
- None (errors encountered while reading the file are logged and do not propagate).

Side effects:
- Mutates os.environ by adding new variables found in the .env file, preserving existing variables.
- Logs informational messages about loading actions and missing files.

Notes:
- If root/.env does not exist, the function is a no-op with a log entry.
- Existing environment variables are preserved; variables from the .env file will not overwrite pre-existing ones.

## Functions

- [`read_dotenv`](../api/functions/graphrag-config-read-dotenv-read-dotenv)

