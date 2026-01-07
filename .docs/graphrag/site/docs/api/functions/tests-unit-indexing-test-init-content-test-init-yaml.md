---
sidebar_position: 526
---

# test_init_yaml

**File:** `tests/unit/indexing/test_init_content.py` (lines 14-17)

## Signature

```python
def test_init_yaml()
```

## Description

Load configuration parameters into a plain dictionary suitable for subsequent GraphRagConfig validation.

Args:
    values: dict[str, Any] | None
        Configuration values to pass into the GraphRagConfig validation step. If None, defaults are applied.
    root_dir: str | None
        Root directory for the project; used to resolve relative paths within the configuration.

Returns:
    dict[str, Any]
        A dictionary of configuration values ready to be consumed by GraphRagConfig.model_validate to produce a GraphRagConfig instance.

Examples:
    data = &#123;...&#125;  # your input dictionary
    config = create_graphrag_config(data)
    GraphRagConfig.model_validate(config, strict=True)

## Dependencies

This function calls:

- `graphrag/config/create_graphrag_config.py::create_graphrag_config`

