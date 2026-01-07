---
sidebar_position: 197
---

# graphrag/query/input/retrieval/relationships.py

## Overview

Utilities for retrieving and manipulating Relationship objects in Graphrag query processing.

This module provides helper functions to sort, filter, and transform Relationship objects for graph-based queries. It includes utilities to sort relationships by a ranking attribute, identify candidate relationships associated with selected entities, convert relationships to pandas DataFrames, and extract involved entities. The functions operate on the Entity and Relationship data models.

Key exports:
- sort_relationships_by_rank(relationships: list[Relationship], ranking_attribute: str = "rank") -&gt; list[Relationship]
- get_candidate_relationships(selected_entities: list[Entity], relationships: list[Relationship]) -&gt; list[Relationship]
- to_relationship_dataframe(relationships: list[Relationship], include_relationship_weight: bool = True) -&gt; pd.DataFrame
- get_entities_from_relationships(relationships: list[Relationship], entities: list[Entity]) -&gt; list[Entity]
- get_in_network_relationships(selected_entities: list[Entity], relationships: list[Relationship], ranking_attribute: str = "rank") -&gt; list[Relationship]
- get_out_network_relationships(selected_entities: list[Entity], relationships: list[Relationship], ranking_attribute: str = "rank") -&gt; list[Relationship]

Brief summary: The utilities enable ranking-based sorting, network-based filtering, and dataframe conversion for analysis of relationship data in graph queries.

## Functions

- [`sort_relationships_by_rank`](../api/functions/graphrag-query-input-retrieval-relationships-sort-relationships-by-rank)
- [`get_candidate_relationships`](../api/functions/graphrag-query-input-retrieval-relationships-get-candidate-relationships)
- [`to_relationship_dataframe`](../api/functions/graphrag-query-input-retrieval-relationships-to-relationship-dataframe)
- [`get_entities_from_relationships`](../api/functions/graphrag-query-input-retrieval-relationships-get-entities-from-relationships)
- [`get_in_network_relationships`](../api/functions/graphrag-query-input-retrieval-relationships-get-in-network-relationships)
- [`get_out_network_relationships`](../api/functions/graphrag-query-input-retrieval-relationships-get-out-network-relationships)

