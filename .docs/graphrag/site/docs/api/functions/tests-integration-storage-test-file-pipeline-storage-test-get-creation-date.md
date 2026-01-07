---
sidebar_position: 442
---

# test_get_creation_date

**File:** `tests/integration/storage/test_file_pipeline_storage.py` (lines 38-48)

## Signature

```python
def test_get_creation_date()
```

## Description

Test that FilePipelineStorage.get_creation_date returns a correctly formatted creation timestamp for a blob. The test uses the fixture file tests/fixtures/text/input/dulce.txt and asserts that the returned string matches the format '%Y-%m-%d %H:%M:%S %z'.

Args:
  None

Returns:
  str - A timestamp string formatted as '%Y-%m-%d %H:%M:%S %z' as produced by FilePipelineStorage.get_creation_date for the fixture file.

Raises:
  ValueError: If the returned creation_date string cannot be parsed using the expected format '%Y-%m-%d %H:%M:%S %z'.

## Dependencies

This function calls:

- `graphrag/storage/file_pipeline_storage.py::FilePipelineStorage`

