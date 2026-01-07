---
sidebar_position: 192
---

# graphrag/query/input/loaders/dfs.py

## Overview

DataFrame-based DFS loaders that construct domain model objects from pre-converted records.

Purpose
This module provides DFS-based readers that accept a pandas DataFrame containing pre-converted records and return lists of domain model instances such as TextUnit, Entity, Relationship, Covariate, CommunityReport, and Community. It uses a helper to reset the DataFrame index and convert rows to dictionaries before instantiating the objects.

Key exports
- _prepare_records(df: pd.DataFrame) -&gt; list[dict]
- read_text_units(df: pd.DataFrame, id_col: str = "id", text_col: str = "text", entities_col: str | None = "entity_ids", relationships_col: str | None = "relationship_ids", covariates_col: str | None = "covariate_ids", tokens_col: str | None = "n_tokens", document_ids_col: str | None = "document_ids", attributes_cols: list[str] | None = None) -&gt; list[TextUnit]
- read_entities(df: pd.DataFrame, id_col: str = "id", short_id_col: str | None = "human_readable_id", title_col: str = "title", type_col: str | None = "type", description_col: str | None = "description", name_embedding_col: str | None = "name_embedding", description_embedding_col: str | None = "description_embedding", community_col: str | None = "community_ids", text_unit_ids_col: str | None = "text_unit_ids", rank_col: str | None = "degree", attributes_cols: list[str] | None = None) -&gt; list[Entity]
- read_relationships(df: pd.DataFrame, id_col: str = "id", short_id_col: str | None = "human_readable_id", source_col: str = "source", target_col: str = "target", description_col: str | None = "description", rank_col: str | None = "combined_degree", description_embedding_col: str | None = "description_embedding", weight_col: str | None = "weight", text_unit_ids_col: str | None = "text_unit_ids", attributes_cols: list[str] | None = None) -&gt; list[Relationship]
- read_covariates(df: pd.DataFrame, id_col: str = "id", short_id_col: str | None = "human_readable_id", subject_col: str = "subject_id", covariate_type_col: str | None = "type", text_unit_ids_col: str | None = "text_unit_ids", attributes_cols: list[str] | None = None) -&gt; list[Covariate]
- read_community_reports(df: pd.DataFrame, id_col: str = "id", short_id_col: str | None = "community", title_col: str = "title", community_col: str = "community", summary_col: str = "summary", content_col: str = "full_content", rank_col: str | None = "rank", content_embedding_col: str | None = "full_content_embedding", attributes_cols: list[str] | None = None) -&gt; list[CommunityReport]
- read_communities(df: pd.DataFrame, id_col: str = "id", short_id_col: str | None = "community", title_col: str = "title", level_col: str = "level", entities_col: str | None = "entity_ids", relationships_col: str | None = "relationship_ids", text_units_col: str | None = "text_unit_ids", covariates_col: str | None = "covariate_ids", parent_col: str | None = "parent", children_col: str | None = "children", attributes_cols: list[str] | None = None) -&gt; list[Community]

Brief summary
The module focuses on turning pre-converted DataFrame records into domain model objects for downstream processing in Graphrag.

## Functions

- [`_prepare_records`](../api/functions/graphrag-query-input-loaders-dfs-prepare-records)
- [`read_text_units`](../api/functions/graphrag-query-input-loaders-dfs-read-text-units)
- [`read_entities`](../api/functions/graphrag-query-input-loaders-dfs-read-entities)
- [`read_relationships`](../api/functions/graphrag-query-input-loaders-dfs-read-relationships)
- [`read_covariates`](../api/functions/graphrag-query-input-loaders-dfs-read-covariates)
- [`read_community_reports`](../api/functions/graphrag-query-input-loaders-dfs-read-community-reports)
- [`read_communities`](../api/functions/graphrag-query-input-loaders-dfs-read-communities)

