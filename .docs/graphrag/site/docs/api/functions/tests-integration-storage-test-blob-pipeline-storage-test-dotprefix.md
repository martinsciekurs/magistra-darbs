---
sidebar_position: 425
---

# test_dotprefix

**File:** `tests/integration/storage/test_blob_pipeline_storage.py` (lines 51-63)

## Signature

```python
def test_dotprefix()
```

## Description

Test that a dot-prefix path is handled correctly by BlobPipelineStorage when setting and listing files. The test creates a storage with path_prefix='.' and writes input/christmas.txt, then searches for .txt files and asserts that the resulting path is ['input/christmas.txt'].

## Dependencies

This function calls:

- `graphrag/storage/blob_pipeline_storage.py::BlobPipelineStorage`

