---
sidebar_position: 395
---

# get_timestamp_formatted_with_local_tz

**File:** `graphrag/storage/pipeline_storage.py` (lines 95-99)

## Signature

```python
def get_timestamp_formatted_with_local_tz(timestamp: datetime) -> str
```

## Description

Get the formatted timestamp with the local time zone.

Args:
    timestamp (datetime): The timestamp to format in the local time zone.

Returns:
    str: The timestamp represented as 'YYYY-MM-DD HH:MM:SS ±HHMM' in the local time zone.

Raises:
    None: This function does not raise any exceptions.

## Called By

This function is called by:

- `graphrag/storage/blob_pipeline_storage.py::BlobPipelineStorage.get_creation_date`
- `graphrag/storage/cosmosdb_pipeline_storage.py::CosmosDBPipelineStorage.get_creation_date`
- `graphrag/storage/file_pipeline_storage.py::FilePipelineStorage.get_creation_date`

