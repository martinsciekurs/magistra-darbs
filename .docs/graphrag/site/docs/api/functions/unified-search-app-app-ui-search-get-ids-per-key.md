---
sidebar_position: 630
---

# get_ids_per_key

**File:** `unified-search-app/app/ui/search.py` (lines 172-184)

## Signature

```python
def get_ids_per_key(str_response: str, key: str)
```

## Description

Get IDs associated with a given key from a string response.

Args:
  str_response (str): The string to search for occurrences of the pattern 'key (&lt;numbers&gt;)'.
  key (str): The prefix text preceding the parenthesized list of IDs.

Returns:
  List[str]: The IDs extracted from the parentheses after the last matching occurrence of the key. If no occurrences are found, returns an empty list.

Notes:
  - If multiple matches are found, only the IDs from the last match are returned.
  - IDs are strings and may contain whitespace; you may trim each element if needed. The IDs are extracted from within the first pair of parentheses following the key and are split on commas.
  - The function does not perform type checking and assumes inputs are strings; it does not raise a TypeError on invalid types.

Pattern:
  A regular expression that matches a parenthesized list of digits separated by commas, optionally followed by , +more.

