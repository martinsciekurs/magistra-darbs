---
sidebar_position: 418
---

# test_register_and_create_custom_logger

**File:** `tests/integration/logging/test_factory.py` (lines 34-53)

## Signature

```python
def test_register_and_create_custom_logger()
```

## Description

Test registering and creating a custom logger type.

This test registers a custom logger type named "custom" using LoggerFactory.register with a factory function, creates a logger via LoggerFactory.create_logger("custom", &#123;&#125;), and asserts that the factory was invoked and the returned logger is the expected instance. It also asserts that the created logger has the initialized attribute set to True and that "custom" is present in the list of registered logger types and is reported as supported.

