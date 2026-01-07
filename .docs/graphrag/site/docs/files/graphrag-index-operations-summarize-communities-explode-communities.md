---
sidebar_position: 85
---

# graphrag/index/operations/summarize_communities/explode_communities.py

## Overview

Explodes a column of entity IDs in communities into individual (community, entity) rows and enriches them with entity data for filtering and downstream processing.

Purpose
Provide a compact utility to convert community-level data into node-level records by exploding the lists of entity IDs and joining with an entities table to attach entity attributes. The function returns a DataFrame suitable for filtering and downstream analytics.

Key exports
- explode_communities(communities: pd.DataFrame, entities: pd.DataFrame) -&gt; pd.DataFrame
  Explodes the entity_ids in each community into one row per (community, entity) pair and joins with the entities DataFrame to attach entity metadata while preserving community context.

Args
explode_communities(communities: pd.DataFrame, entities: pd.DataFrame) -&gt; pd.DataFrame
  Explodes the entity_ids column in each row of communities (commonly named entity_ids) into separate rows and attaches corresponding entity attributes by joining to entities on id. The communities DataFrame is expected to contain at least the entity_ids column and community-related metadata; the entities DataFrame is expected to contain an id column used for the join.

Returns
  pd.DataFrame
  A DataFrame with one row per community-entity pair, including the exploded entity_id and any joined attributes from entities and the original community metadata.

Raises
ValueError
  If required columns are missing from inputs (e.g., entity_ids in communities or id in entities) or if entity_ids is not list-like.
TypeError
  If inputs are not pandas DataFrames.

Edge cases
- Empty inputs yield an empty DataFrame with the expected output columns.
- IDs without matching entities will have missing metadata after the join.

## Functions

- [`explode_communities`](../api/functions/graphrag-index-operations-summarize-communities-explode-communities-explode-communities)

