---
sidebar_position: 247
---

# finalize_graph

**File:** `graphrag/index/workflows/finalize_graph.py` (lines 65-76)

## Signature

```python
def finalize_graph(
    entities: pd.DataFrame,
    relationships: pd.DataFrame,
    embed_config: EmbedGraphConfig | None = None,
    layout_enabled: bool = False,
) -> tuple[pd.DataFrame, pd.DataFrame]
```

## Description

Finalize the entity and relationship formats by applying the finalization steps.

Args:
    entities (pd.DataFrame): Input entities to be transformed into final records.
    relationships (pd.DataFrame): DataFrame containing edge information used to finalize relationships.
    embed_config (EmbedGraphConfig | None): Optional configuration for embedding graphs; passed to finalization.
    layout_enabled (bool): If True, enables applying a layout during finalization.

Returns:
    tuple[pd.DataFrame, pd.DataFrame]: A tuple containing the final_entities DataFrame and final_relationships DataFrame.

Raises:
    Propagates exceptions raised by finalize_entities or finalize_relationships.

## Dependencies

This function calls:

- `graphrag/index/operations/finalize_entities.py::finalize_entities`
- `graphrag/index/operations/finalize_relationships.py::finalize_relationships`

## Called By

This function is called by:

- `graphrag/index/workflows/finalize_graph.py::run_workflow`

