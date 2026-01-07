---
sidebar_position: 13
---

# graphrag/cli/main.py

## Overview

Graphrag CLI main module

Purpose
This module provides the core Typer-based command implementations and helpers used by Graphrag's command-line interface. It wires together project initialization, index construction and updates, knowledge-graph queries, and prompt tuning workflows, while also exposing common path autocompletion and string-matching utilities. The module relies on graphrag.config and graphrag.cli submodules to compose a cohesive CLI experience and is intended to be used as part of a Typer-powered command-line interface.

Exports
- _initialize_cli: Initialize a new Graphrag project at a given root, creating defaults and configuration files. May raise ValueError if the project already exists and the operation is not forced.
- _query_cli: Run a knowledge-graph query using a chosen method with optional verbosity and output controls.
- _index_cli: Build a knowledge-graph index with configurable method and options, including verbose and cache options.
- _prompt_tune_cli: Generate and tune prompts for a project based on configuration and tuning parameters.
- _update_cli: Update an existing index, with optional output override.
- wildcard_match: Determine whether a string matches a wildcard pattern using ? and *.
- path_autocomplete: Autocomplete file and directory paths with filtering options.
- completer: Return a list of possible directory item completions for autocompletion.
- INVALID_METHOD_ERROR: The error message displayed for an invalid method selection.
- CONFIG_AUTOCOMPLETE: Autocomplete helper for configuration file paths.
- ROOT_AUTOCOMPLETE: Autocomplete helper for project root paths.

Notes
- The module documents the public surface and runtime caveats such as import/export inconsistencies. Detailed parameter and return information exists in each exported function's own docstring.

Usage
- The CLI is designed to be used via Typer command line apps. Each exported function serves as a command handler or helper consumed by the surrounding Typer app. For quickstart, inspect the help output for each command and its options, or import the functions in Python to call them programmatically.

Example
- Initialize a project in Python:

from pathlib import Path
from graphrag.cli.main import _initialize_cli
_ = _initialize_cli(root=Path("/path/to/project"), force=True)

- Run a query in Python:

from pathlib import Path
from graphrag.cli.main import _query_cli
_ = _query_cli(method=None, query="example query", root=Path("/path/to/project"), verbose=True)

## Functions

- [`wildcard_match`](../api/functions/graphrag-cli-main-wildcard-match)
- [`path_autocomplete`](../api/functions/graphrag-cli-main-path-autocomplete)
- [`completer`](../api/functions/graphrag-cli-main-completer)
- [`_initialize_cli`](../api/functions/graphrag-cli-main-initialize-cli)
- [`_query_cli`](../api/functions/graphrag-cli-main-query-cli)
- [`_index_cli`](../api/functions/graphrag-cli-main-index-cli)
- [`_prompt_tune_cli`](../api/functions/graphrag-cli-main-prompt-tune-cli)
- [`_update_cli`](../api/functions/graphrag-cli-main-update-cli)

