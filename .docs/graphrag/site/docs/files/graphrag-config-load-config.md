---
sidebar_position: 22
---

# graphrag/config/load_config.py

## Overview

Module to load GraphRag configuration from disk and environment, returning a GraphRagConfig instance.

Overview:
This module provides utilities to locate, load, and parse configuration files for GraphRag, supporting YAML (.yaml/.yml) and JSON (.json), optional dotenv loading from the config directory, and applying CLI overrides to the loaded configuration. The main entry point is load_config, which returns a GraphRagConfig object. Internal helpers implement dotenv loading, override application, content parsing, config search, environment variable substitution, and path resolution.

Public API:
- load_config(root_dir: Path, config_filepath: Path | None = None, cli_overrides: dict[str, Any] | None = None) -&gt; GraphRagConfig
  Load configuration from a file, resolving the path, parsing contents, applying overrides and environment variables, and returning a GraphRagConfig.

Internal helpers:
- _load_dotenv(config_path: Path | str) -&gt; None
- _apply_overrides(data: dict[str, Any], overrides: dict[str, Any]) -&gt; None
- _parse(file_extension: str, contents: str) -&gt; dict[str, Any]
- _search_for_config_in_root_dir(root: str | Path) -&gt; Path | None
- _parse_env_variables(text: str) -&gt; str
- _get_config_path(root_dir: Path, config_filepath: Path | None) -&gt; Path

Returns:
- GraphRagConfig: The loaded configuration wrapped in a GraphRagConfig instance.

Raises:
- FileNotFoundError: If the configuration file cannot be found.
- TypeError: If attempting to override a non-dict value along the path with a non-dict override.

## Functions

- [`_load_dotenv`](../api/functions/graphrag-config-load-config-load-dotenv)
- [`_apply_overrides`](../api/functions/graphrag-config-load-config-apply-overrides)
- [`_parse`](../api/functions/graphrag-config-load-config-parse)
- [`_search_for_config_in_root_dir`](../api/functions/graphrag-config-load-config-search-for-config-in-root-dir)
- [`_parse_env_variables`](../api/functions/graphrag-config-load-config-parse-env-variables)
- [`_get_config_path`](../api/functions/graphrag-config-load-config-get-config-path)
- [`load_config`](../api/functions/graphrag-config-load-config-load-config)

