---
sidebar_position: 16
---

# graphrag/config/create_graphrag_config.py

## Overview

GraphRag configuration utilities.

Purpose
Provide helpers to create and load GraphRagConfig instances from simple data sources, enabling convenient integration with the rest of the graphrag package.

Key exports
- create_graphrag_config: Build a GraphRagConfig from a values dictionary and optional root_dir.

Brief summary
This module exposes a single helper, create_graphrag_config, which accepts a dictionary of configuration values and an optional root directory, returning a validated GraphRagConfig instance. The function validates input using pydantic and raises ValidationError if the values are invalid.

Args:
  values: dict[str, Any] | None
      Dictionary of configuration values to pass into the pydantic model.
  root_dir: str | None
      Root directory for the project.

Returns:
  GraphRagConfig
      The configuration object.

Raises:
  ValidationError
      If the configuration values do not satisfy pydantic validation.

## Functions

- [`create_graphrag_config`](../api/functions/graphrag-config-create-graphrag-config-create-graphrag-config)

