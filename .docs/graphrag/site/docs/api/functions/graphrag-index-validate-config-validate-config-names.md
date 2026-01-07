---
sidebar_position: 217
---

# validate_config_names

**File:** `graphrag/index/validate_config.py` (lines 17-53)

## Signature

```python
def validate_config_names(parameters: GraphRagConfig) -> None
```

## Description

Validate config file for model deployment name typos, by running a quick test message for each.

Args:
  parameters: GraphRagConfig containing models to validate.

Returns:
  None

Raises:
  SystemExit: If validation fails for any model; the process exits with status 1.

## Dependencies

This function calls:

- `graphrag/callbacks/noop_workflow_callbacks.py::NoopWorkflowCallbacks`
- `graphrag/language_model/manager.py::ModelManager`

## Called By

This function is called by:

- `graphrag/cli/index.py::_run_index`

