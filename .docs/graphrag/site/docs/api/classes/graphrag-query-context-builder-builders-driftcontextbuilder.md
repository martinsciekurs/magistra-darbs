---
sidebar_position: 80
---

# DRIFTContextBuilder

**File:** `graphrag/query/context_builder/builders.py`

## Overview

DRIFTContextBuilder is an abstract base class that defines the contract for constructing the DRIFT context used to prime subsequent search actions for a given query. It specifies an asynchronous interface to build the context, exposed via the build_context(query, **kwargs) method, which returns a tuple containing a DataFrame of contextual items and a metrics dictionary used to warm up or seed downstream DRIFT search processes.

Args:
    self: The instance of the class.
    query (str): The search query for which to build the context.
    **kwargs: Additional keyword arguments to customize or influence context construction.

Returns:
    tuple[pd.DataFrame, dict[str, int]]: A pair consisting of a DataFrame of contextual items and a metrics dictionary mapping metric names to integer counts.

Raises:
    NotImplementedError: If the subclass does not implement build_context.

## Methods

### `build_context`

```python
def build_context(
        self,
        query: str,
        **kwargs,
    ) -> tuple[pd.DataFrame, dict[str, int]]
```

