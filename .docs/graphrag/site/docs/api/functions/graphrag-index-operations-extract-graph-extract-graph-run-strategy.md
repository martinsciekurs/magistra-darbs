---
sidebar_position: 112
---

# run_strategy

**File:** `graphrag/index/operations/extract_graph/extract_graph.py` (lines 50-61)

## Signature

```python
def run_strategy(row)
```

## Description

Run a strategy on a single input row to extract graph data.

Args:
    row: A row from the input DataFrame containing the values for text_column and id_column. The text is read from row[text_column] and the id from row[id_column].

Returns:
    A list with three elements: the entities, relationships, and graph returned by the strategy execution for this row.

Raises:
    Exceptions raised by the underlying strategy execution (strategy_exec) are propagated.

## Dependencies

This function calls:

- `graphrag/index/operations/extract_graph/typing.py::Document`

