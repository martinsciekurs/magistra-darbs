---
sidebar_position: 125
---

# StaticRateLimiter

**File:** `graphrag/language_model/providers/litellm/services/rate_limiter/static_rate_limiter.py`

## Overview

StaticRateLimiter enforces fixed-per-period limits on requests per minute (RPM) and tokens per minute (TPM) with an optional default stagger between requests. It tracks usage within a configurable period and resets counts at period boundaries. Limits can be disabled individually by setting rpm or tpm to None. The acquire() method is a context manager used to guard a block of code; pass token_count as the estimated number of tokens for the current request. The context manager yields None and blocks as needed to ensure the limits are not exceeded. If both RPM and TPM are disabled, acquire() yields immediately. A non-negative default_stagger is applied between requests when appropriate.

Key attributes
- rpm: RPM limit; positive integer or None to disable.
- tpm: TPM limit; positive integer or None to disable.
- default_stagger: Non-negative delay between requests, in seconds.
- period_in_seconds: Length of the monitoring period in seconds; must be &gt; 0.

Constructor and usage notes
- rpm and tpm must be None or a positive integer; invalid values raise ValueError.
- default_stagger must be &gt;= 0; invalid values raise ValueError.
- period_in_seconds must be &gt; 0; invalid values raise ValueError.
- token_count should be a positive integer; misuse may raise ValueError.

Thread-safety
- The limiter is designed for multi-threaded use; internal state is synchronized to support concurrent acquire() calls.

Behavior overview
- Limits are enforced within each period window and reset when a new period begins. The limiter blocks (and optionally staggers) to ensure that usage never exceeds the configured RPM/TPM within a period.

## Methods

### `__init__`

```python
def __init__(
        self,
        *,
        rpm: int | None = None,
        tpm: int | None = None,
        default_stagger: float = 0.0,
        period_in_seconds: int = 60,
        **kwargs: Any,
    )
```

### `acquire`

```python
def acquire(self, *, token_count: int) -> Iterator[None]
```

