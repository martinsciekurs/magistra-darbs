---
sidebar_position: 11
---

# graphrag/cli/index.py

## Overview

GraphRag CLI indexing utilities.

This module provides command-line interfaces to run the GraphRag indexing and update pipelines, integrating with the GraphRag API, console workflow callbacks, configuration loading and validation, redaction utilities, and logging. It also defines signal handling to enable graceful shutdown of asynchronous tasks.

Exports:
  handle_signal(signum, _): Handle a system signal by cancelling all asyncio tasks and logging exit messages.
  _register_signal_handlers(): Register signal handlers for graceful shutdown of the CLI. This function defines a signal handler that logs the received signal, cancels all asyncio tasks, and logs that all tasks have been cancelled. It registers the handler for SIGINT and, on non-Windows platforms, SIGHUP.
  _run_index(config, method, is_update_run, verbose, memprofile, cache, dry_run, skip_validation): Run the indexing pipeline using the provided configuration.
  index_cli(root_dir, method, verbose, memprofile, cache, config_filepath, dry_run, skip_validation, output_dir): Run the indexing pipeline with the given configuration. Parameters: root_dir (Path): The root directory of the project. Will search for the configuration file in this directory. method (IndexingMethod): The indexing method to use for this run. verbose (bool): Enable verbose logging/output. memprofile (bool): Enable memory profiling during execution. cache (bool): Whether to enable caching. dry_run (bool): If true, run without applying changes. skip_validation (bool): If true, skip configuration validation. output_dir (Path | None): Optional output directory override.
  update_cli(root_dir, method, verbose, memprofile, cache, config_filepath, skip_validation, output_dir): Run the update pipeline with the given configuration. Similar to index_cli but for the update step.

## Functions

- [`handle_signal`](../api/functions/graphrag-cli-index-handle-signal)
- [`_register_signal_handlers`](../api/functions/graphrag-cli-index-register-signal-handlers)
- [`_run_index`](../api/functions/graphrag-cli-index-run-index)
- [`index_cli`](../api/functions/graphrag-cli-index-index-cli)
- [`update_cli`](../api/functions/graphrag-cli-index-update-cli)

