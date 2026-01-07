---
sidebar_position: 393
---

# _create_progress_status

**File:** `graphrag/storage/cosmosdb_pipeline_storage.py` (lines 356-363)

## Signature

```python
def _create_progress_status(
    num_loaded: int, num_filtered: int, num_total: int
) -> Progress
```

## Description

Create a Progress object representing the current load progress.

Args:
    num_loaded: int. The number of files that have been loaded.
    num_filtered: int. The number of files that were filtered out.
    num_total: int. The total number of items.

Returns:
    Progress: Progress object with total_items=num_total, completed_items=num_loaded + num_filtered, and description set to "&lt;num_loaded&gt; files loaded (&lt;num_filtered&gt; filtered)".

## Dependencies

This function calls:

- `graphrag/logger/progress.py::Progress`

## Called By

This function is called by:

- `graphrag/storage/cosmosdb_pipeline_storage.py::CosmosDBPipelineStorage.find`

