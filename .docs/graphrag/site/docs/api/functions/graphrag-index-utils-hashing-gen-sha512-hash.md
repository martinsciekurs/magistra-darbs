---
sidebar_position: 206
---

# gen_sha512_hash

**File:** `graphrag/index/utils/hashing.py` (lines 11-14)

## Signature

```python
def gen_sha512_hash(item: dict[str, Any], hashcode: Iterable[str])
```

## Description

Generate a SHA512 hash from the concatenation of string representations of selected fields of an item.

Args:
  item: input dictionary containing values to hash.
  hashcode: keys whose corresponding values are used for the hash, in order.

Returns:
  str: Hexadecimal SHA512 digest string.

Raises:
  KeyError: if a key from hashcode is not present in item.

## Called By

This function is called by:

- `graphrag/index/input/text.py::load_file`
- `graphrag/index/input/util.py::process_data_columns`
- `graphrag/index/operations/build_noun_graph/build_noun_graph.py::extract`
- `graphrag/index/workflows/create_base_text_units.py::create_base_text_units`

