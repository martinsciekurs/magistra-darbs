---
sidebar_position: 21
---

# graphrag/config/get_embedding_settings.py

## Overview

Utility to derive embedding settings from a GraphRagConfig.

Purpose:
- This module provides a helper to convert a GraphRagConfig into a dictionary of embedding workflow settings.

Key exports:
- get_embedding_settings(settings: GraphRagConfig, vector_store_params: dict | None = None) -&gt; dict

Summary:
- The module's main API is get_embedding_settings, which accepts a GraphRagConfig (containing embed_text and vector_store configuration) and an optional vector_store_params dictionary to override defaults. It returns a dictionary with a single key "strategy" describing the embedding strategy to be used by downstream workflows.

## Functions

- [`get_embedding_settings`](../api/functions/graphrag-config-get-embedding-settings-get-embedding-settings)

