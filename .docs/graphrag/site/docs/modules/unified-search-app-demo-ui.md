---
sidebar_position: 8
---

# Unified Search App (Demo UI)

Demo UI and data loading components for Unified Search, built around the GraphRAG index and results visualization.

## Overview

Unified Search App (Demo UI) - Demo UI and data loading components for Unified Search, built around the GraphRAG index and results visualization.

Purpose:
    Provide a cohesive client-side dashboard and data-loading stack that orchestrates dataset loading, knowledge model provisioning, multiple search strategies (global, local, drift, and basic), question generation, and visualization using the GraphRAG framework. This module ties together the demo UI (Streamlit-based) with the knowledge-loader stack and GraphRAG visualization components to enable end-to-end experimentation and demonstration.

Architecture:
    - app: Streamlit-based UI and orchestration layer that wires the app logic to UI components (GraphRAG UI, questions, reports, side bar).
    - knowledge_loader: data loading layer with support for blob and local storage, dataset discovery, and prompts.
    - rag: GraphRAG integration typings used across the app.
    - ui: rendering utilities for search results, citations, HTML rendering, and graph visualizations.
    - data sources: default, blob_source, and loader utilities to construct and read knowledge data.

Public APIs:
    - app_logic: load_knowledge_model; dataset_name; run_global_search_question_generation; run_global_search; run_drift_search; run_local_search; run_basic_search; run_generate_questions
    - home_page: main; on_click_reset; on_change
    - knowledge_loader.model: load_entities; load_entity_relationships; load_communities; load_covariates; load_community_reports; load_text_units; load_model
    - knowledge_loader.data_sources.blob_source: BlobDatasource class with __init__, _get_container, load_blob_prompt_config, load_blob_file, read, read_settings
    - knowledge_loader.data_sources.loader: _get_base_path; create_datasource; load_dataset_listing; load_prompts
    - rag.typing: type definitions for GraphRAG integration
    - ui.search: init_search_ui; render_html_table; convert_numbered_list_to_array; format_response_hyperlinks_by_key; get_ids_per_key; format_suggested_questions; format_response_hyperlinks; display_citations
    - ui.sidebar: update_basic_rag; reset_app; update_global_search; lookup_label; update_drift_search; update_local_search; create_side_bar; update_dataset
    - ui.full_graph: create_full_graph_ui

## Files in this Module

- [`unified-search-app/app/__init__.py`](../files/unified-search-app-app-init)
- [`unified-search-app/app/app_logic.py`](../files/unified-search-app-app-app-logic)
- [`unified-search-app/app/home_page.py`](../files/unified-search-app-app-home-page)
- [`unified-search-app/app/knowledge_loader/model.py`](../files/unified-search-app-app-knowledge-loader-model)
- [`unified-search-app/app/knowledge_loader/data_sources/default.py`](../files/unified-search-app-app-knowledge-loader-data-sources-default)
- [`unified-search-app/app/knowledge_loader/data_sources/blob_source.py`](../files/unified-search-app-app-knowledge-loader-data-sources-blob-source)
- [`unified-search-app/app/knowledge_loader/data_sources/loader.py`](../files/unified-search-app-app-knowledge-loader-data-sources-loader)
- [`unified-search-app/app/rag/typing.py`](../files/unified-search-app-app-rag-typing)
- [`unified-search-app/app/ui/search.py`](../files/unified-search-app-app-ui-search)
- [`unified-search-app/app/ui/sidebar.py`](../files/unified-search-app-app-ui-sidebar)
- [`unified-search-app/app/ui/full_graph.py`](../files/unified-search-app-app-ui-full-graph)
