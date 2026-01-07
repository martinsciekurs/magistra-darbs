---
sidebar_position: 287
---

# unified-search-app/app/knowledge_loader/model.py

## Overview

Knowledge loading helpers for the unified search app.

This module provides lightweight wrappers that delegate to the knowledge_loader.data_prep utilities to load slices of knowledge data from a specified dataset via a Datasource. Loaded data are returned as pandas DataFrame objects and can be used to build the knowledge model consumed by the application. The load_model function returns a KnowledgeModel object representing the assembled knowledge.

Exports:
  - load_entities(dataset: str, _datasource: Datasource) -&gt; pandas.DataFrame
  - load_entity_relationships(dataset: str, _datasource: Datasource) -&gt; pandas.DataFrame
  - load_communities(_datasource: Datasource) -&gt; pandas.DataFrame
  - load_covariates(dataset: str, _datasource: Datasource) -&gt; pandas.DataFrame
  - load_community_reports(_datasource: Datasource) -&gt; pandas.DataFrame
  - load_text_units(dataset: str, _datasource: Datasource) -&gt; pandas.DataFrame
  - load_model(dataset: str, datasource: Datasource) -&gt; KnowledgeModel

Summary:
  Each function delegates to the corresponding data_prep loader, propagating any exceptions from the underlying utilities. This module is intended for convenient access to the data slices needed to build and populate the knowledge model used by the unified search app.

## Functions

- [`load_entities`](../api/functions/unified-search-app-app-knowledge-loader-model-load-entities)
- [`load_entity_relationships`](../api/functions/unified-search-app-app-knowledge-loader-model-load-entity-relationships)
- [`load_communities`](../api/functions/unified-search-app-app-knowledge-loader-model-load-communities)
- [`load_covariates`](../api/functions/unified-search-app-app-knowledge-loader-model-load-covariates)
- [`load_community_reports`](../api/functions/unified-search-app-app-knowledge-loader-model-load-community-reports)
- [`load_text_units`](../api/functions/unified-search-app-app-knowledge-loader-model-load-text-units)
- [`load_model`](../api/functions/unified-search-app-app-knowledge-loader-model-load-model)

