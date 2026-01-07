---
sidebar_position: 15
---

# graphrag/cli/query.py

## Overview

GraphRag CLI query module.

Overview:
This module provides the command-line interfaces to run GraphRag queries in multiple modes
(global, local, drift, and basic) with optional streaming and integrated configuration and
storage support. It wires together configuration loading, storage access, and the GraphRag
API to execute queries and to resolve and load output data from storage.

Key exports:
- on_context(context: Any) -&gt; None: Stores the given context in the enclosing scope's nonlocal variable context_data.
- run_streaming_search() -&gt; tuple[str, dict[str, Any]]: Runs a streaming search and collects the full response while printing streamed chunks.
- _resolve_output_files(config: GraphRagConfig, output_list: list[str], optional_list: list[str] | None = None) -&gt; dict[str, Any]: Reads indexing output files to a dataframe dict.
- run_global_search(config_filepath: Path | None, data_dir: Path | None, root_dir: Path, community_level: int | None, dynamic_community_selection: bool, response_type: str, streaming: bool, query: str, verbose: bool): Perform a global search with a given query.
- run_local_search(config_filepath: Path | None, data_dir: Path | None, root_dir: Path, community_level: int, response_type: str, streaming: bool, query: str, verbose: bool): Perform a local search with a given query.
- run_drift_search(config_filepath: Path | None, data_dir: Path | None, root_dir: Path, community_level: int, response_type: str, streaming: bool, query: str, verbose: bool): Perform a local drift search for a given query across either a multi-index or single-index dataset.
- run_basic_search(config_filepath: Path | None, data_dir: Path | None, root_dir: Path, streaming: bool, query: str, verbose: bool): Perform a basics search with a given query.

Notes:
- This module relies on graphrag.api, storage utilities, and configuration loading utilities.

## Functions

- [`on_context`](../api/functions/graphrag-cli-query-on-context)
- [`run_streaming_search`](../api/functions/graphrag-cli-query-run-streaming-search)
- [`_resolve_output_files`](../api/functions/graphrag-cli-query-resolve-output-files)
- [`run_global_search`](../api/functions/graphrag-cli-query-run-global-search)
- [`run_local_search`](../api/functions/graphrag-cli-query-run-local-search)
- [`run_drift_search`](../api/functions/graphrag-cli-query-run-drift-search)
- [`run_basic_search`](../api/functions/graphrag-cli-query-run-basic-search)

