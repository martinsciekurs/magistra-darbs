---
sidebar_position: 66
---

# StorageConfig

**File:** `graphrag/config/models/storage_config.py`

## Overview

StorageConfig manages storage-related configuration for GraphRAG backends.

Purpose:
    Encapsulates settings for storage backends, including the storage type and
    the base directory for local storage. It reads defaults from graphrag_config_defaults
    and uses StorageType to determine behavior. It provides a validator to normalize
    the base_dir when using local storage.

Attributes:
    base_dir: The filesystem path for local storage base directory. Used when storage_type
        indicates local file storage.
    storage_type: The StorageType enum value that selects the storage backend.

Brief summary:
    Centralizes storage configuration for GraphRAG, ensuring consistent handling of
    base directories for local storage and pass-through for non-local storage types.

Methods:
    validate_base_dir(cls, value, info):
        Normalize base_dir to a filesystem path string for local storage. This validator
        does not verify that the path exists or is valid beyond conversion to a string.
        It only performs normalization when the storage type is local (StorageType.file);
        for all other storage types, the input value is returned unchanged.

Args:
    cls (type): The class that defines the validator.
    value (Any): The input value to be validated and normalized.
    info (dict): Validation information provided by Pydantic.

Returns:
    str: The normalized base_dir path when storage_type is local; otherwise, the input value
        unchanged.

Raises:
    None

## Methods

### `validate_base_dir`

```python
def validate_base_dir(cls, value, info)
```

