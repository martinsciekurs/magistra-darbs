---
sidebar_position: 58
---

# load_file

**File:** `graphrag/index/input/text.py` (lines 25-33)

## Signature

```python
def load_file(path: str, group: dict | None = None) -> pd.DataFrame
```

## Description

Load a text input from storage and return it as a DataFrame containing metadata.

Args:
  path (str): Path to the text file.
  group (dict | None): Optional grouping metadata to merge with the item. If None, an empty dict is used.

Returns:
  pd.DataFrame: A DataFrame containing a single row with the loaded text and metadata, including id, title, and creation_date.

Raises:
  KeyError: If a key from the hashcode used for hashing is not present in the item.

## Dependencies

This function calls:

- `graphrag/index/utils/hashing.py::gen_sha512_hash`

