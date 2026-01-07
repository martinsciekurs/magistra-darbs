---
sidebar_position: 424
---

# test_get_creation_date

**File:** `tests/integration/storage/test_blob_pipeline_storage.py` (lines 66-81)

## Signature

```python
def test_get_creation_date()
```

## Description

Test that BlobPipelineStorage.get_creation_date returns a correctly formatted creation timestamp for a blob.

Returns:
A string representing the creation date of the blob, formatted as "%Y-%m-%d %H:%M:%S %z".
Type: str

## Dependencies

This function calls:

- `graphrag/storage/blob_pipeline_storage.py::BlobPipelineStorage`

