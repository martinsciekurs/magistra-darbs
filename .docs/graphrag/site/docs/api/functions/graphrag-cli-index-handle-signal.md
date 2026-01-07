---
sidebar_position: 17
---

# handle_signal

**File:** `graphrag/cli/index.py` (lines 28-33)

## Signature

```python
def handle_signal(signum, _)
```

## Description

Handle a system signal by cancelling all asyncio tasks and logging exit messages.

Args:
    signum: The signal number received.
    _: The current stack frame (unused).

Returns:
    None

## Example 💡 Generated

```python
from app.signals import handle_signal
import signal, types
frame = types.SimpleNamespace()
handle_signal(signal.SIGINT, frame)  # simulate SIGINT
# expected: logs and task cancellation
```

