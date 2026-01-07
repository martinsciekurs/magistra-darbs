---
sidebar_position: 26
---

# graphrag/config/models/graph_rag_config.py

## Overview

GraphRagConfig configuration model for aggregating and validating GraphRag's settings.

Purpose:
Defines the GraphRagConfig class, a Pydantic-based model that aggregates numerous sub-config models
(e.g., BasicSearchConfig, CacheConfig, ChunkingConfig, LanguageModelConfig, VectorStoreConfig, etc.)
to provide a single, validated configuration surface for GraphRag.

Exports:
- GraphRagConfig: The main configuration model class that ties together sub-configs and validation hooks.

Public API:
- GraphRagConfig.get_vector_store_config(vector_store_id: str) -&gt; VectorStoreConfig
- GraphRagConfig.get_language_model_config(model_id: str) -&gt; LanguageModelConfig

Summary:
The module centralizes defaults, path handling, and validation orchestration to ensure consistent runtime
configuration for GraphRag.

## Classes

- [`GraphRagConfig`](../api/classes/graphrag-config-models-graph-rag-config-graphragconfig)

## Functions

- [`_validate_input_base_dir`](../api/functions/graphrag-config-models-graph-rag-config-validate-input-base-dir)
- [`_validate_rate_limiter_services`](../api/functions/graphrag-config-models-graph-rag-config-validate-rate-limiter-services)
- [`_validate_reporting_base_dir`](../api/functions/graphrag-config-models-graph-rag-config-validate-reporting-base-dir)
- [`_validate_factories`](../api/functions/graphrag-config-models-graph-rag-config-validate-factories)
- [`_validate_model`](../api/functions/graphrag-config-models-graph-rag-config-validate-model)
- [`_validate_output_base_dir`](../api/functions/graphrag-config-models-graph-rag-config-validate-output-base-dir)
- [`_validate_retry_services`](../api/functions/graphrag-config-models-graph-rag-config-validate-retry-services)
- [`__str__`](../api/functions/graphrag-config-models-graph-rag-config-str)
- [`get_vector_store_config`](../api/functions/graphrag-config-models-graph-rag-config-get-vector-store-config)
- [`_validate_vector_store_db_uri`](../api/functions/graphrag-config-models-graph-rag-config-validate-vector-store-db-uri)
- [`_validate_input_pattern`](../api/functions/graphrag-config-models-graph-rag-config-validate-input-pattern)
- [`_validate_multi_output_base_dirs`](../api/functions/graphrag-config-models-graph-rag-config-validate-multi-output-base-dirs)
- [`get_language_model_config`](../api/functions/graphrag-config-models-graph-rag-config-get-language-model-config)
- [`__repr__`](../api/functions/graphrag-config-models-graph-rag-config-repr)
- [`_validate_models`](../api/functions/graphrag-config-models-graph-rag-config-validate-models)
- [`_validate_update_index_output_base_dir`](../api/functions/graphrag-config-models-graph-rag-config-validate-update-index-output-base-dir)
- [`_validate_root_dir`](../api/functions/graphrag-config-models-graph-rag-config-validate-root-dir)

