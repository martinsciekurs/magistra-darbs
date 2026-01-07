---
sidebar_position: 585
---

# compare_outputs

**File:** `tests/verbs/util.py` (lines 58-86)

## Signature

```python
def compare_outputs(
    actual: pd.DataFrame, expected: pd.DataFrame, columns: list[str] | None = None
) -> None
```

## Description

Compare the actual and expected dataframes, optionally specifying columns to compare. This function uses pandas.testing.assert_series_equal to compare columns and intentionally omits the id column from value checks. If a mismatch is found, the function prints the Expected and Actual values for debugging before raising an AssertionError.

Args:
    actual: The actual DataFrame produced by the workflow.
    expected: The expected DataFrame against which to compare the actual DataFrame.
    columns: Optional list of column names to compare. If None, all columns from expected are compared.

Returns:
    None

Raises:
    AssertionError: If the number of rows differs or any compared column's values (excluding id) differ, or if a column listed in columns is not present in actual.

## Called By

This function is called by:

- `tests/verbs/test_create_base_text_units.py::test_create_base_text_units`
- `tests/verbs/test_create_base_text_units.py::test_create_base_text_units_metadata`
- `tests/verbs/test_create_base_text_units.py::test_create_base_text_units_metadata_included_in_chunk`
- `tests/verbs/test_create_communities.py::test_create_communities`
- `tests/verbs/test_create_community_reports.py::test_create_community_reports`
- `tests/verbs/test_create_final_documents.py::test_create_final_documents`
- `tests/verbs/test_create_final_documents.py::test_create_final_documents_with_metadata_column`
- `tests/verbs/test_create_final_text_units.py::test_create_final_text_units`

