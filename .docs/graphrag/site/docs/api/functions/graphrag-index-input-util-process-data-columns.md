---
sidebar_position: 60
---

# process_data_columns

**File:** `graphrag/index/input/util.py` (lines 56-86)

## Signature

```python
def process_data_columns(
    documents: pd.DataFrame, config: InputConfig, path: str
) -> pd.DataFrame
```

## Description

Process configured data columns of a DataFrame by augmenting it with id, text, and title columns according to the provided configuration. Warnings are logged if a configured text or title column is not found in the data.

The function mutates the input DataFrame and returns it.

Args:
  documents (pd.DataFrame): DataFrame to augment with id, text, and title columns as configured.
  config (InputConfig): Configuration containing optional text_column and title_column. If text_column is provided, a text column will be created from that column if present; otherwise a warning is logged and no text column is created. If text_column is None, no text column is created.
  path (str): File path used for logging warnings and as the default title when no title column is specified.

Returns:
  pd.DataFrame: The input DataFrame augmented with id, text, and title columns as configured.

Raises:
  Exception: If hashing or data processing fails due to underlying data issues or library operations. The exact exception depends on the hashing function or pandas operations.

## Dependencies

This function calls:

- `graphrag/index/utils/hashing.py::gen_sha512_hash`

## Called By

This function is called by:

- `graphrag/index/input/csv.py::load_file`
- `graphrag/index/input/json.py::load_file`

