---
sidebar_position: 409
---

# storage_has_table

**File:** `graphrag/utils/storage.py` (lines 42-44)

## Signature

```python
def storage_has_table(name: str, storage: PipelineStorage) -> bool
```

## Description

Check if a table exists in storage.

Args:
    name: The name of the table to check (without the extension).
    storage: The storage backend implementing PipelineStorage.

Returns:
    bool: True if a file named "&lt;name&gt;.parquet" exists in storage, False otherwise.

Raises:
    Propagates exceptions raised by storage.has.

## Example 💡 Generated

```python
from storage_utils import storage_has_table
name = "optional_file"
class DummyStorage:
    def has(self, path: str) -> bool:
        return path == "optional_file.parquet"
storage = DummyStorage()
result = storage_has_table(name, storage)
print(result)  # True if exists
```

## Called By

This function is called by:

- `graphrag/cli/query.py::_resolve_output_files`
- `graphrag/index/workflows/create_community_reports.py::run_workflow`
- `graphrag/index/workflows/create_final_text_units.py::run_workflow`
- `graphrag/index/workflows/update_covariates.py::run_workflow`

