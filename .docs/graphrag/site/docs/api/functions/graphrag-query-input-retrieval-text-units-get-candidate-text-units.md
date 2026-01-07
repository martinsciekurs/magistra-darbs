---
sidebar_position: 388
---

# get_candidate_text_units

**File:** `graphrag/query/input/retrieval/text_units.py` (lines 14-24)

## Signature

```python
def get_candidate_text_units(
    selected_entities: list[Entity],
    text_units: list[TextUnit],
) -> pd.DataFrame
```

## Description

Get all text units that are associated to selected entities.

Args:
    selected_entities (list[Entity]): Entities whose text_unit_ids (if any) are used to select text units.
    text_units (list[TextUnit]): The pool of TextUnit objects to search.

Returns:
    pd.DataFrame: A DataFrame containing the text units associated with the selected entities. The DataFrame is produced by converting the selected TextUnit objects via to_text_unit_dataframe; if no such text units are found, an empty DataFrame is returned.

## Dependencies

This function calls:

- `graphrag/query/input/retrieval/text_units.py::to_text_unit_dataframe`

## Called By

This function is called by:

- `graphrag/query/structured_search/local_search/mixed_context.py::LocalSearchMixedContext._build_text_unit_context`

