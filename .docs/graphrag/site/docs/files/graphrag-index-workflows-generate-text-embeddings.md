---
sidebar_position: 129
---

# graphrag/index/workflows/generate_text_embeddings.py

## Overview

Generates text embedding workflows for GraphRAG.

Purpose:
This module defines utilities for generating text embeddings from various input data sources (e.g., documents, relationships, text units, entities, and community reports) using configured embedding settings. It wires together data preparation, embedding generation, and optional persistence of embedding snapshots.

Key exports:
- _run_embeddings: Generate a single embedding for a given data frame.
- generate_text_embeddings: Generate all configured text embeddings from the provided input data.
- run_workflow: Entry point for the workflow; orchestrates loading inputs, generating embeddings, and persisting snapshots.

Summary:
Provides the end-to-end workflow to produce text embeddings for GraphRAG components, enabling flexible embedding configurations and caching during processing.

Args:
    None: The module itself does not accept parameters on import. Use the exported functions with their own arguments.

Returns:
    None: The module does not return a value on import. It exposes functions that return data when invoked.

Raises:
    None: Importing the module does not raise exceptions by itself.

## Functions

- [`_run_embeddings`](../api/functions/graphrag-index-workflows-generate-text-embeddings-run-embeddings)
- [`generate_text_embeddings`](../api/functions/graphrag-index-workflows-generate-text-embeddings-generate-text-embeddings)
- [`run_workflow`](../api/functions/graphrag-index-workflows-generate-text-embeddings-run-workflow)

