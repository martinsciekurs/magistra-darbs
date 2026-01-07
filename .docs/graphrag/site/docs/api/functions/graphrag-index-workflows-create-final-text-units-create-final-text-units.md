---
sidebar_position: 237
---

# create_final_text_units

**File:** `graphrag/index/workflows/create_final_text_units.py` (lines 55-83)

## Signature

```python
def create_final_text_units(
    text_units: pd.DataFrame,
    final_entities: pd.DataFrame,
    final_relationships: pd.DataFrame,
    final_covariates: pd.DataFrame | None,
) -> pd.DataFrame
```

## Description

Transfroms input text units and their associated entities, relationships, and optional covariates into the final text units DataFrame.

Args:
    text_units (pd.DataFrame): Input text units. Expected to contain at least the columns:
        - id
        - text
        - document_ids
        - n_tokens
    final_entities (pd.DataFrame): Mapping of entities to text units. Must contain:
        - id (entity_id)
        - text_unit_ids (list-like of text_unit_ids)
    final_relationships (pd.DataFrame): Mapping of relationships to text units. Must contain:
        - id (relationship_id)
        - text_unit_ids (list-like of text_unit_ids)
    final_covariates (pd.DataFrame | None): Optional covariates mapping. If provided, must contain:
        - id (covariate_id)
        - text_unit_id (text_unit_id to which the covariate applies)

Returns:
    pd.DataFrame: Final text units data frame with columns defined by TEXT_UNITS_FINAL_COLUMNS.

Raises:
    KeyError: If required columns are missing from any input DataFrame:
        - text_units must include id, text, document_ids, and n_tokens
        - final_entities must include id and text_unit_ids
        - final_relationships must include id and text_unit_ids
        - final_covariates (if not None) must include id and text_unit_id

Processing details:
    1) Select core fields from text_units (id, text, document_ids, n_tokens) and add a human_readable_id derived from the index.
    2) Build text-unit-to-entity and text-unit-to-relationship mappings via _entities and _relationships.
    3) Join the selected text units with the entity mapping, then with the relationship mapping to propagate IDs.
    4) If final_covariates is provided, build the covariate mapping via _covariates and join; otherwise initialize covariate_ids with empty lists.
    5) Group by text unit id and take the first row per id to collapse duplicates.
    6) Return only the columns defined by TEXT_UNITS_FINAL_COLUMNS.

Notes:
    - When final_covariates is None, covariate_ids are set to empty lists for every row.
    - The exact output columns depend on TEXT_UNITS_FINAL_COLUMNS and may vary with configuration.

## Dependencies

This function calls:

- `graphrag/index/workflows/create_final_text_units.py::_covariates`
- `graphrag/index/workflows/create_final_text_units.py::_entities`
- `graphrag/index/workflows/create_final_text_units.py::_join`
- `graphrag/index/workflows/create_final_text_units.py::_relationships`

## Called By

This function is called by:

- `graphrag/index/workflows/create_final_text_units.py::run_workflow`

