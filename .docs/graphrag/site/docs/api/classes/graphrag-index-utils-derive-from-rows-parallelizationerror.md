---
sidebar_position: 96
---

# ParallelizationError

**File:** `graphrag/index/utils/derive_from_rows.py`

## Overview

ParallelizationError stores information about errors that occurred during parallel transformation.

Attributes:
- num_errors (int): The number of errors that occurred during the parallel transformation.
- example (str | None): Optional example error string to include in messages or logs. Defaults to None.

Initialization:
__init__(self, num_errors: int, example: str | None = None)

Initializes the instance with the given error details and stores them on the object for later access (e.g., for error reporting or messaging).

## Methods

### `__init__`

```python
def __init__(self, num_errors: int, example: str | None = None)
```

