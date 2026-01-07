---
sidebar_position: 415
---

# test_create_blob_logger

**File:** `tests/integration/logging/test_factory.py` (lines 23-31)

## Signature

```python
def test_create_blob_logger()
```

## Description

Test for creating a blob logger via LoggerFactory (skipped in this environment).

This test is marked with pytest.mark.skip(reason="Blob storage emulator is not available in this environment"). If executed, it would construct a kwargs dictionary containing: type: "blob", connection_string: WELL_KNOWN_BLOB_STORAGE_KEY, base_dir: "testbasedir", container_name: "testcontainer". It would then call LoggerFactory.create_logger(ReportingType.blob.value, kwargs) and assert that the resulting logger is an instance of BlobWorkflowLogger.

Returns:
    None

