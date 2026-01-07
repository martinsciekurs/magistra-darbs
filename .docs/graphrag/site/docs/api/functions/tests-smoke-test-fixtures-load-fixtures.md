---
sidebar_position: 459
---

# _load_fixtures

**File:** `tests/smoke/test_fixtures.py` (lines 34-48)

## Signature

```python
def _load_fixtures()
```

## Description

Load all fixtures from the tests/fixtures directory and return their configurations (internal helper).

If GH_PAGES is set, only the min-csv fixture is loaded; otherwise all subdirectories under tests/fixtures are considered.

Returns:
  list of tuple (str, dict): a list where each item is a pair consisting of the subfolder name and the parsed JSON configuration loaded from config.json for that fixture. The first entry is omitted in order to disable the azure blob connection test.

Raises:
  FileNotFoundError: If a subfolder is missing config.json.
  json.JSONDecodeError: If config.json cannot be parsed as JSON.

