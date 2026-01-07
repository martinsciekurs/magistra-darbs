---
sidebar_position: 304
---

# create_file_logger

**File:** `graphrag/logger/factory.py` (lines 82-96)

## Signature

```python
def create_file_logger(**kwargs) -> logging.Handler
```

## Description

Create a file-based logger handler.

Args:
    root_dir: The root directory under which logs are stored.
    base_dir: The base directory under root_dir where logs are written.
    filename: The log filename to use for the log file.

Returns:
    logging.Handler: A configured handler writing to the specified log file.

Raises:
    KeyError: If required keys (root_dir, base_dir, filename) are missing in kwargs.
    OSError: If the log directory cannot be created or the log file cannot be opened.

