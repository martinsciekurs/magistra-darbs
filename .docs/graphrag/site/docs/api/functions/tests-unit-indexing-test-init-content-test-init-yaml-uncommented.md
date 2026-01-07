---
sidebar_position: 527
---

# test_init_yaml_uncommented

**File:** `tests/unit/indexing/test_init_content.py` (lines 20-31)

## Signature

```python
def test_init_yaml_uncommented()
```

## Description

Test that uncommenting the YAML in INIT_YAML produces a valid GraphRagConfig.

Returns:
    None (type: None)

Raises:
    ValidationError: If the configuration values do not satisfy pydantic validation.

## Dependencies

This function calls:

- `graphrag/config/create_graphrag_config.py::create_graphrag_config`
- `tests/unit/indexing/test_init_content.py::uncomment_line`

