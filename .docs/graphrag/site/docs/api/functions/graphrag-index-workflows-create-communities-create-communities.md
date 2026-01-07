---
sidebar_position: 222
---

# create_communities

**File:** `graphrag/index/workflows/create_communities.py` (lines 54-156)

## Signature

```python
def create_communities(
    entities: pd.DataFrame,
    relationships: pd.DataFrame,
    max_cluster_size: int,
    use_lcc: bool,
    seed: int | None = None,
) -> pd.DataFrame
```

## Description

Create final communities from entities and relationships using graph-based clustering and metadata enrichment.

This function builds a graph from the provided relationships, performs Leiden-based clustering to group entities into hierarchical communities, and then aggregates related entities and relationships into a final, metadata-rich DataFrame. The result is aligned to the column schema defined by COMMUNITIES_FINAL_COLUMNS and is suitable for storage and downstream processing.

Args:
    entities (pd.DataFrame): DataFrame containing entities. Must include at least:
        - title (str): The display title used to link to relationships
        - id (str): The unique identifier for the entity
    relationships (pd.DataFrame): DataFrame containing relationships. Must include:
        - source (str): Title of the source entity
        - target (str): Title of the target entity
        - id (str): Unique identifier for the relationship
        - text_unit_ids (list): Identifiers of the text units associated with the relationship
        - weight (float, optional): Edge weight used when constructing the graph
    max_cluster_size (int): Maximum allowed size for a cluster produced by the clustering step.
    use_lcc (bool): If True, operate on the largest connected component of the input graph.
    seed (int | None, optional): Random seed for reproducibility of the clustering process.

Returns:
    pd.DataFrame: Final communities DataFrame containing metadata and ready for storage. The exact
    columns are defined by COMMUNITIES_FINAL_COLUMNS and include fields such as identifiers (id,
    human_readable_id, title), hierarchical and grouping fields (community, level, parent, children),
    membership aggregations (entity_ids, relationship_ids, text_unit_ids), and update-tracking fields
    (period, size).

Raises:
    ValueError: If required input columns are missing or inputs have invalid types.
    KeyError: If expected keys are missing during processing (indicative of unexpected input shape).

## Dependencies

This function calls:

- `graphrag/index/operations/cluster_graph.py::cluster_graph`
- `graphrag/index/operations/create_graph.py::create_graph`

## Called By

This function is called by:

- `graphrag/index/workflows/create_communities.py::run_workflow`

