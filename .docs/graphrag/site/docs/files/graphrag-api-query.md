---
sidebar_position: 3
---

# graphrag/api/query.py

## Overview

Query interfaces for GraphRAG API.

This module provides high-level query functions to perform global, local, drift, and basic searches, with both streaming and non-streaming variants. It coordinates a graphrag configuration (GraphRagConfig), DataFrames for entities, communities, community reports, text units, relationships, and covariates, and utilizes embedding configurations and logging. It exposes a set of functions that return either a full response plus context data or yield streaming chunks to be consumed asynchronously. It also allows capturing and propagating context data through the on_context helper.

Key exports:
- on_context
- global_search
- global_search_streaming
- multi_index_global_search
- basic_search
- basic_search_streaming
- multi_index_basic_search
- drift_search
- drift_search_streaming
- multi_index_drift_search
- local_search
- local_search_streaming
- multi_index_local_search

## Functions

- [`on_context`](../api/functions/graphrag-api-query-on-context)
- [`global_search_streaming`](../api/functions/graphrag-api-query-global-search-streaming)
- [`global_search`](../api/functions/graphrag-api-query-global-search)
- [`multi_index_global_search`](../api/functions/graphrag-api-query-multi-index-global-search)
- [`basic_search`](../api/functions/graphrag-api-query-basic-search)
- [`basic_search_streaming`](../api/functions/graphrag-api-query-basic-search-streaming)
- [`drift_search`](../api/functions/graphrag-api-query-drift-search)
- [`drift_search_streaming`](../api/functions/graphrag-api-query-drift-search-streaming)
- [`local_search`](../api/functions/graphrag-api-query-local-search)
- [`local_search_streaming`](../api/functions/graphrag-api-query-local-search-streaming)
- [`multi_index_basic_search`](../api/functions/graphrag-api-query-multi-index-basic-search)
- [`multi_index_drift_search`](../api/functions/graphrag-api-query-multi-index-drift-search)
- [`multi_index_local_search`](../api/functions/graphrag-api-query-multi-index-local-search)

