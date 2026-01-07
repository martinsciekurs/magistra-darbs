---
sidebar_position: 2
---

# GraphRAG Command-Line Interface

CLI entry points and tooling to run indexing, querying, and prompt tuning workflows via uv/poethepoet.

## Overview

GraphRAG Command-Line Interface (CLI) for indexing, querying, and prompt tuning workflows via uv/poethepoet.

Architectural purpose:
- Provide a Typer-based CLI layer that orchestrates project initialization, index construction and updates, knowledge-graph queries, and prompt tuning workflows, integrating with configuration, storage, logging, and the GraphRAG API.

Key components and responsibilities:
- graphrag.cli.main: Implements the core Typer-based command implementations and helpers used by Graphrag's CLI. It wires together project initialization, index construction and updates, knowledge-graph queries, and prompt tuning workflows, while also exposing the primary CLI entry points.
- graphrag.cli.index: GraphRag CLI indexing utilities. This module provides command-line interfaces to run the GraphRag indexing and update pipelines, integrating with the GraphRag API, console workflow callbacks, configuration loading and validation, redaction utilities, and logging. It also defines signal handling and related tooling.
- graphrag.cli.initialize: GraphRag CLI initialization utilities. Purpose: module that provides the CLI entry point functionality to initialize a GraphRag project at a given filesystem path by creating initial configuration files and preparing prompt templates.
- graphrag.cli.prompt_tune: Asynchronous prompt tuning orchestration for the GraphRag CLI. Purpose: this module exposes the prompt_tune coroutine which coordinates configuration loading, chunking overrides, logging initialization, and indexing-prompt generation for prompt tuning.
- graphrag.cli.query: GraphRag CLI query module. Overview: this module provides the command-line interfaces to run GraphRag queries in multiple modes (global, local, drift, and basic) with optional streaming and integrated configuration and storage support.

Main entry points / public APIs:
- main.py: wildcard_match, path_autocomplete, completer, _initialize_cli, _query_cli, _index_cli, _prompt_tune_cli, _update_cli
- index.py: handle_signal, _register_signal_handlers, _run_index, index_cli, update_cli
- initialize.py: initialize_project_at
- prompt_tune.py: prompt_tune
- query.py: on_context, run_streaming_search, _resolve_output_files, run_global_search, run_local_search, run_drift_search, run_basic_search

## Files in this Module

- [`graphrag/cli/__init__.py`](../files/graphrag-cli-init)
- [`graphrag/cli/main.py`](../files/graphrag-cli-main)
- [`graphrag/cli/index.py`](../files/graphrag-cli-index)
- [`graphrag/cli/initialize.py`](../files/graphrag-cli-initialize)
- [`graphrag/cli/prompt_tune.py`](../files/graphrag-cli-prompt-tune)
- [`graphrag/cli/query.py`](../files/graphrag-cli-query)
