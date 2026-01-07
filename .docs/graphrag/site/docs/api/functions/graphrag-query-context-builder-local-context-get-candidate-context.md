---
sidebar_position: 334
---

# get_candidate_context

**File:** `graphrag/query/context_builder/local_context.py` (lines 320-357)

## Signature

```python
def get_candidate_context(
    selected_entities: list[Entity],
    entities: list[Entity],
    relationships: list[Relationship],
    covariates: dict[str, list[Covariate]],
    include_entity_rank: bool = True,
    entity_rank_description: str = "number of relationships",
    include_relationship_weight: bool = False,
) -> dict[str, pd.DataFrame]
```

## Description

Prepare candidate context data tables (entities, relationships, and covariates) to be used in a system prompt.

Args:
  selected_entities (list[Entity]): The selected entities for which to build candidate context.
  entities (list[Entity]): The pool of entities to consider when constructing the candidate entity DataFrame.
  relationships (list[Relationship]): The pool of relationships to filter to candidate relationships.
  covariates (dict[str, list[Covariate]]): Mapping from covariate group names to Covariate objects to include in the context.
  include_entity_rank (bool): Whether to include a rank column for entities. Default is True.
  entity_rank_description (str): Header name for the rank column when include_entity_rank is True. Default is "number of relationships".
  include_relationship_weight (bool): Whether to include a weight column in the relationships DataFrame. Default is False.

Returns:
  dict[str, pd.DataFrame]: A dictionary containing the following DataFrames:
    - "relationships": DataFrame of candidate relationships (optionally including weight).
    - "entities": DataFrame of candidate entities (with optional rank column).
    - For each key in covariates, a lowercase-keyed DataFrame of the corresponding covariates.

## Dependencies

This function calls:

- `graphrag/query/input/retrieval/covariates.py::get_candidate_covariates`
- `graphrag/query/input/retrieval/covariates.py::to_covariate_dataframe`
- `graphrag/query/input/retrieval/entities.py::to_entity_dataframe`
- `graphrag/query/input/retrieval/relationships.py::get_candidate_relationships`
- `graphrag/query/input/retrieval/relationships.py::get_entities_from_relationships`
- `graphrag/query/input/retrieval/relationships.py::to_relationship_dataframe`

## Called By

This function is called by:

- `graphrag/query/structured_search/local_search/mixed_context.py::LocalSearchMixedContext._build_local_context`

