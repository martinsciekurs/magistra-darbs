---
sidebar_position: 248
---

# tests/unit/config/utils.py

## Overview

Test utilities for graphrag configuration models used in unit tests.

This module provides a collection of assertion helpers for comparing instances of
various graphrag configuration models and a helper to construct a default GraphRagConfig
for tests. It also exposes top-level constants used by tests.

Key exports
- FAKE_API_KEY
- DEFAULT_CHAT_MODEL_CONFIG
- DEFAULT_EMBEDDING_MODEL_CONFIG
- DEFAULT_MODEL_CONFIG
- get_default_graphrag_config
- assert_prune_graph_configs
- assert_extract_claims_configs
- assert_community_reports_configs
- assert_chunking_configs
- assert_cache_configs
- assert_global_search_configs
- assert_text_analyzer_configs
- assert_language_model_configs
- assert_reporting_configs
- assert_cluster_graph_configs
- assert_output_configs
- assert_drift_search_configs
- assert_update_output_configs
- assert_input_configs
- assert_vector_store_configs
- assert_extract_graph_configs
- assert_umap_configs
- assert_snapshots_configs
- assert_basic_search_configs
- assert_embed_graph_configs
- assert_local_search_configs
- assert_summarize_descriptions_configs
- assert_text_embedding_configs
- assert_extract_graph_nlp_configs
- assert_graphrag_configs

Brief summary
The module centralizes test helpers for Graphrag config objects to simplify and standardize assertions across unit tests.

## Functions

- [`assert_prune_graph_configs`](../api/functions/tests-unit-config-utils-assert-prune-graph-configs)
- [`assert_extract_claims_configs`](../api/functions/tests-unit-config-utils-assert-extract-claims-configs)
- [`assert_community_reports_configs`](../api/functions/tests-unit-config-utils-assert-community-reports-configs)
- [`assert_chunking_configs`](../api/functions/tests-unit-config-utils-assert-chunking-configs)
- [`assert_cache_configs`](../api/functions/tests-unit-config-utils-assert-cache-configs)
- [`assert_global_search_configs`](../api/functions/tests-unit-config-utils-assert-global-search-configs)
- [`assert_text_analyzer_configs`](../api/functions/tests-unit-config-utils-assert-text-analyzer-configs)
- [`assert_language_model_configs`](../api/functions/tests-unit-config-utils-assert-language-model-configs)
- [`assert_reporting_configs`](../api/functions/tests-unit-config-utils-assert-reporting-configs)
- [`assert_cluster_graph_configs`](../api/functions/tests-unit-config-utils-assert-cluster-graph-configs)
- [`assert_output_configs`](../api/functions/tests-unit-config-utils-assert-output-configs)
- [`assert_drift_search_configs`](../api/functions/tests-unit-config-utils-assert-drift-search-configs)
- [`assert_update_output_configs`](../api/functions/tests-unit-config-utils-assert-update-output-configs)
- [`assert_input_configs`](../api/functions/tests-unit-config-utils-assert-input-configs)
- [`assert_vector_store_configs`](../api/functions/tests-unit-config-utils-assert-vector-store-configs)
- [`assert_extract_graph_configs`](../api/functions/tests-unit-config-utils-assert-extract-graph-configs)
- [`assert_umap_configs`](../api/functions/tests-unit-config-utils-assert-umap-configs)
- [`assert_snapshots_configs`](../api/functions/tests-unit-config-utils-assert-snapshots-configs)
- [`assert_basic_search_configs`](../api/functions/tests-unit-config-utils-assert-basic-search-configs)
- [`assert_embed_graph_configs`](../api/functions/tests-unit-config-utils-assert-embed-graph-configs)
- [`assert_local_search_configs`](../api/functions/tests-unit-config-utils-assert-local-search-configs)
- [`assert_summarize_descriptions_configs`](../api/functions/tests-unit-config-utils-assert-summarize-descriptions-configs)
- [`get_default_graphrag_config`](../api/functions/tests-unit-config-utils-get-default-graphrag-config)
- [`assert_text_embedding_configs`](../api/functions/tests-unit-config-utils-assert-text-embedding-configs)
- [`assert_extract_graph_nlp_configs`](../api/functions/tests-unit-config-utils-assert-extract-graph-nlp-configs)
- [`assert_graphrag_configs`](../api/functions/tests-unit-config-utils-assert-graphrag-configs)

