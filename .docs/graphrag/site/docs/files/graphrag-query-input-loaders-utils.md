---
sidebar_position: 193
---

# graphrag/query/input/loaders/utils.py

## Overview

Utilities to extract and validate values from mappings used by loaders.

This module provides a set of helper functions that operate on a Mapping[str, Any]
to retrieve values by key and convert them to common Python types with validation.
Optional variants return None when the key is missing or when the requested key is None,
providing a consistent handling policy across the API. A central _get_value helper is used
to implement the required vs optional retrieval logic.

Key exports:
- to_optional_float(data, column_name) -&gt; float | None
- _get_value(data, column_name, required=True) -&gt; Any
- to_optional_int(data, column_name) -&gt; int | None
- to_optional_dict(data, column_name, key_type=None, value_type=None) -&gt; dict | None
- to_optional_list(data, column_name, item_type=None) -&gt; list | None
- to_str(data, column_name) -&gt; str
- to_optional_str(data, column_name) -&gt; str | None
- to_list(data, column_name, item_type=None) -&gt; list
- to_int(data, column_name) -&gt; int
- to_float(data, column_name) -&gt; float
- to_dict(data, column_name, key_type=None, value_type=None) -&gt; dict

Notes on behavior:
- Optional helpers return None if column_name is None or the column is missing from data.
- Required helpers rely on _get_value and raise ValueError if column_name is None or missing.
- Type validations raise TypeError when a value does not conform to the expected type; conversion
  errors may raise ValueError or TypeError depending on the scenario.

Examples:
- Using to_optional_int(data, 'age') returns an int or None if the column is missing or None
- Using to_dict(data, 'preferences', key_type=str, value_type=int) validates that the value is a dict with string keys and integer values

Raises:
- ValueError for missing required columns or invalid column_name for required helpers
- TypeError for mismatched types or invalid item/key/value types in dict/list helpers
- ValueError for invalid conversions where appropriate

## Functions

- [`to_optional_float`](../api/functions/graphrag-query-input-loaders-utils-to-optional-float)
- [`_get_value`](../api/functions/graphrag-query-input-loaders-utils-get-value)
- [`to_optional_int`](../api/functions/graphrag-query-input-loaders-utils-to-optional-int)
- [`to_optional_dict`](../api/functions/graphrag-query-input-loaders-utils-to-optional-dict)
- [`to_optional_list`](../api/functions/graphrag-query-input-loaders-utils-to-optional-list)
- [`to_str`](../api/functions/graphrag-query-input-loaders-utils-to-str)
- [`to_optional_str`](../api/functions/graphrag-query-input-loaders-utils-to-optional-str)
- [`to_list`](../api/functions/graphrag-query-input-loaders-utils-to-list)
- [`to_int`](../api/functions/graphrag-query-input-loaders-utils-to-int)
- [`to_float`](../api/functions/graphrag-query-input-loaders-utils-to-float)
- [`to_dict`](../api/functions/graphrag-query-input-loaders-utils-to-dict)

