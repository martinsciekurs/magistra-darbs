---
sidebar_position: 177
---

# _group_and_resolve_entities

**File:** `graphrag/index/update/entities.py` (lines 14-78)

## Signature

```python
def _group_and_resolve_entities(
    old_entities_df: pd.DataFrame, delta_entities_df: pd.DataFrame
) -> tuple[pd.DataFrame, dict]
```

## Description

Group old and delta entity data, resolve conflicts by title, and return a merged entities dataframe along with a mapping from delta to existing entity IDs.

This function merges the existing entities with a delta of new or updated entities, constructs a mapping from delta entity IDs to existing entity IDs for overlapping titles, and returns a resolved dataframe with a consistent column order.

Parameters
----------
old_entities_df : pd.DataFrame
    The existing entities dataframe containing current entities.
delta_entities_df : pd.DataFrame
    The delta dataframe containing new or updated entities to be merged.

Returns
-------
tuple[pd.DataFrame, dict]
    A pair consisting of:
    - The resolved entities dataframe, with columns ordered according to ENTITIES_FINAL_COLUMNS.
    - id_mapping: A mapping from delta (B) entity ids to existing (A) entity ids, in the form &#123;delta_id: existing_id&#125;. The mapping only includes titles that exist in both dataframes. If a delta id would produce duplicate keys in the mapping (due to duplicate delta ids for the same title), a ValueError may be raised because dict construction is done with strict=True.

Raises
------
ValueError
    If id_mapping cannot be constructed due to duplicate delta ids (id_B) which would produce duplicate keys when building the mapping (strict key enforcement).

Notes
-----
- For overlapping titles, id_mapping records the mapping from the delta entity id (B) to the existing entity id (A).
- human_readable_id in delta_entities_df is incremented to continue from the maximum value present in old_entities_df to ensure unique identifiers.
- The old and delta entities are concatenated and grouped by title to resolve conflicts; for each title, the first occurrence of fields (id, type, human_readable_id, x, y) is kept, while description is collected as a list of strings and text_unit_ids are flattened into a single list.
- Frequency is recomputed as the length of the text_unit_ids list to reflect added text units.
- The final dataframe is explicitly ordered to ENTITIES_FINAL_COLUMNS for consistency.

## Example 💡 Generated

```python
from my_graph_module import _group_and_resolve_entities
# old_entities_df and delta_entities_df
# are predefined with required columns
merged_df, mapping = _group_and_resolve_entities(
    old_entities_df, delta_entities_df)
# merged_df has ENTITIES_FINAL_COLUMNS; mapping maps
# delta ids to existing ids
```

## Called By

This function is called by:

- `graphrag/index/workflows/update_entities_relationships.py::_update_entities_and_relationships`

