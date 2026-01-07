---
sidebar_position: 34
---

# _resolve_output_files

**File:** `graphrag/cli/query.py` (lines 477-534)

## Signature

```python
def _resolve_output_files(
    config: GraphRagConfig,
    output_list: list[str],
    optional_list: list[str] | None = None,
) -> dict[str, Any]
```

## Description

Read indexing output files to a dataframe dict.

Args:
    config: GraphRagConfig The configuration for GraphRag, including outputs for multi-index search.
    output_list: list[str] Names of the output dataframe keys to load from storage.
    optional_list: list[str] | None Optional list of additional output dataframe keys to load if present.

Returns:
    dict[str, Any]: A dictionary containing the loaded dataframes and metadata describing the indexing layout.
        If config.outputs is truthy (multi-index search):
          - "multi-index": True
          - "num_indexes": int number of indexes (len(config.outputs))
          - "index_names": config.outputs.keys()
          - For each name in output_list: a list of DataFrames loaded from storage (one per index)
          - For each optional_file in optional_list, a key optional_file with a list of DataFrames if present, otherwise an empty list
        If config.outputs is falsy (single-index search):
          - "multi-index": False
          - For each name in output_list: the loaded DataFrame
          - For each optional_file in optional_list: the loaded DataFrame if present, otherwise None

## Dependencies

This function calls:

- `graphrag/utils/api.py::create_storage_from_config`
- `graphrag/utils/storage.py::load_table_from_storage`
- `graphrag/utils/storage.py::storage_has_table`

## Called By

This function is called by:

- `graphrag/cli/query.py::run_global_search`
- `graphrag/cli/query.py::run_local_search`
- `graphrag/cli/query.py::run_drift_search`
- `graphrag/cli/query.py::run_basic_search`

