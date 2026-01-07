---
sidebar_position: 440
---

# test_find

**File:** `tests/integration/storage/test_file_pipeline_storage.py` (lines 17-35)

## Signature

```python
def test_find()
```

## Description

Asynchronous test for FilePipelineStorage.find and basic get/set/delete operations.

This test is asynchronous and uses await to verify the behavior of FilePipelineStorage:
- find: lists .txt files under a base directory matching a pattern
- get: reads file contents (including verifying the existence)
- set: creates a new file with specified content
- delete: removes the file and confirms it is deleted

Note: Failures may raise assertions or other exceptions during test execution.

Args:
    None: The function does not accept any input parameters. Type: None

Returns:
    None: The test does not return a value. Type: None

Raises:
    AssertionError: If any assertion in the test fails.
    Exception: If any other error occurs during test execution.

## Dependencies

This function calls:

- `graphrag/storage/file_pipeline_storage.py::FilePipelineStorage`

