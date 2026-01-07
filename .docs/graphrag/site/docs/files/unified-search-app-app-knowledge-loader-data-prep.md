---
sidebar_position: 282
---

# unified-search-app/app/knowledge_loader/data_prep.py

## Overview

Utilities to load and prepare datasets from the indexed data store for the knowledge loader used by the unified-search-app.

This module provides data preparation utilities that read datasets from the indexed data via a configured data source and return pandas DataFrames for downstream processing and visualization. It relies on a configured data source and is intended for use by the knowledge loader workflows in the unified-search-app.

Key exports
- get_community_report_data(_datasource: Datasource) -&gt; pd.DataFrame: Returns a DataFrame with community report data loaded from the indexed data.
- get_communities_data(_datasource: Datasource) -&gt; pd.DataFrame: Returns a DataFrame with communities data loaded from the indexed data.
- get_text_unit_data(dataset: str, _datasource: Datasource) -&gt; pd.DataFrame: Returns a DataFrame containing text units for the specified dataset from the indexed data.
- get_entity_data(dataset: str, _datasource: Datasource) -&gt; pd.DataFrame: Returns a DataFrame with entity data for the specified dataset from the indexed data.
- get_relationship_data(dataset: str, _datasource: Datasource) -&gt; pd.DataFrame: Returns a DataFrame with entity-entity relationship data for the specified dataset.
- get_covariate_data(dataset: str, _datasource: Datasource) -&gt; pd.DataFrame: Returns a DataFrame with covariate data for the specified dataset.

## Functions

- [`get_community_report_data`](../api/functions/unified-search-app-app-knowledge-loader-data-prep-get-community-report-data)
- [`get_communities_data`](../api/functions/unified-search-app-app-knowledge-loader-data-prep-get-communities-data)
- [`get_text_unit_data`](../api/functions/unified-search-app-app-knowledge-loader-data-prep-get-text-unit-data)
- [`get_entity_data`](../api/functions/unified-search-app-app-knowledge-loader-data-prep-get-entity-data)
- [`get_relationship_data`](../api/functions/unified-search-app-app-knowledge-loader-data-prep-get-relationship-data)
- [`get_covariate_data`](../api/functions/unified-search-app-app-knowledge-loader-data-prep-get-covariate-data)

