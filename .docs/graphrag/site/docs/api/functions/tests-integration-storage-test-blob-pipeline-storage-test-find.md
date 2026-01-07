---
sidebar_position: 427
---

# test_find

**File:** `tests/integration/storage/test_blob_pipeline_storage.py` (lines 14-48)

## Signature

```python
def test_find()
```

## Description

Asynchronous test for BlobPipelineStorage.find and basic file operations.

This test creates a BlobPipelineStorage instance, verifies that there are no matching .txt files under the input base_dir, creates input/christmas.txt and then confirms it is found, creates test.txt and confirms both files are listed, reads the content of test.txt, and finally deletes test.txt and ensures it no longer exists. The container is cleaned up at the end.

Returns:
    None

Raises:
    None

## Dependencies

This function calls:

- `graphrag/storage/blob_pipeline_storage.py::BlobPipelineStorage`

