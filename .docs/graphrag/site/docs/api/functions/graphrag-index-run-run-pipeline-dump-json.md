---
sidebar_position: 165
---

# _dump_json

**File:** `graphrag/index/run/run_pipeline.py` (lines 142-157)

## Signature

```python
def _dump_json(context: PipelineRunContext) -> None
```

## Description

Dump the stats and context state to the storage.

Args:
    context: PipelineRunContext
        The pipeline run context containing stats, state, and output storage used for persistence.

Returns:
    None
        The function completes without returning a value.

Raises:
    Exception
        If storage operations fail or JSON serialization fails.

## Example 💡 Generated

```python
from pipeline_run import _dump_json
import asyncio
class Stats:
    ok = True
class Store:
    async def set(self, k, v):
        pass
ctx = type("Ctx", (), {})()
ctx.stats = Stats()
ctx.state = {"s":"r"}
ctx.output_storage = Store()
async def _run():
    await _dump_json(ctx)
asyncio.run(_run())
```

## Called By

This function is called by:

- `graphrag/index/run/run_pipeline.py::_run_pipeline`

