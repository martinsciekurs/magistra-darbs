---
sidebar_position: 191
---

# graphrag/query/indexer_adapters.py

## Overview

Adapters for converting raw indexing outputs into domain model objects used by GraphRAG queries.

Overview
This module provides adapter functions that read the raw indexing outputs (represented as pandas DataFrames and Python objects) produced by the indexer and convert them into the domain model objects defined in graphrag.data_model: TextUnit, Entity, Relationship, Covariate, Community, and CommunityReport. It relies on DFS-based loaders, an embedding model, and a vector store to enrich and assemble the final structures. The functions support operations such as filtering by community level, embedding reports, and reconstructing the hierarchy of communities.

Exports
- _filter_under_community_level(df: pd.DataFrame, community_level: int) -&gt; pd.DataFrame: Filter a DataFrame by a maximum community level threshold.
- read_indexer_report_embeddings(community_reports: list[CommunityReport], embeddings_store: BaseVectorStore) -&gt; None: Populate CommunityReport objects with their embeddings from the vector store.
- embed_community_reports(reports_df: pd.DataFrame, embedder: EmbeddingModel, source_col: str = "full_content", embedding_col: str = "full_content_embedding") -&gt; pd.DataFrame: Generate and attach embeddings for a given source column.
- read_indexer_text_units(final_text_units: pd.DataFrame) -&gt; list[TextUnit]: Convert final text unit data to a list of TextUnit objects.
- read_indexer_entities(entities: pd.DataFrame, communities: pd.DataFrame, community_level: int | None) -&gt; list[Entity]: Build Entity objects from raw entity data and associated communities, optionally filtered by level.
- read_indexer_relationships(final_relationships: pd.DataFrame) -&gt; list[Relationship]: Convert final relationships data into Relationship objects.
- read_indexer_covariates(final_covariates: pd.DataFrame) -&gt; list[Covariate]: Convert final covariate data into Covariate objects.
- read_indexer_reports(final_community_reports: pd.DataFrame, final_communities: pd.DataFrame, community_level: int | None, dynamic_community_selection: bool = False, content_embedding_col: str = "full_content_embedding", config: GraphRagConfig | None = None) -&gt; list[CommunityReport]: Build CommunityReport objects from raw data, optionally applying dynamic community selection and embedding content.
- read_indexer_communities(final_communities: pd.DataFrame, final_community_reports: pd.DataFrame) -&gt; list[Community]: Reconstruct the Community hierarchy and membership using the raw data.

## Functions

- [`_filter_under_community_level`](../api/functions/graphrag-query-indexer-adapters-filter-under-community-level)
- [`read_indexer_report_embeddings`](../api/functions/graphrag-query-indexer-adapters-read-indexer-report-embeddings)
- [`embed_community_reports`](../api/functions/graphrag-query-indexer-adapters-embed-community-reports)
- [`read_indexer_text_units`](../api/functions/graphrag-query-indexer-adapters-read-indexer-text-units)
- [`read_indexer_entities`](../api/functions/graphrag-query-indexer-adapters-read-indexer-entities)
- [`read_indexer_relationships`](../api/functions/graphrag-query-indexer-adapters-read-indexer-relationships)
- [`read_indexer_covariates`](../api/functions/graphrag-query-indexer-adapters-read-indexer-covariates)
- [`read_indexer_reports`](../api/functions/graphrag-query-indexer-adapters-read-indexer-reports)
- [`read_indexer_communities`](../api/functions/graphrag-query-indexer-adapters-read-indexer-communities)

