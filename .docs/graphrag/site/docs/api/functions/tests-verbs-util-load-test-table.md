---
sidebar_position: 584
---

# load_test_table

**File:** `tests/verbs/util.py` (lines 53-55)

## Signature

```python
def load_test_table(output: str) -> pd.DataFrame
```

## Description

Load a test table from parquet data using the provided workflow output name.

Args:
    output: The workflow output name, typically the workflow name, used to locate the parquet file at tests/verbs/data/&#123;output&#125;.parquet.

Returns:
    pd.DataFrame: The DataFrame read from the specified parquet file.

## Called By

This function is called by:

- `tests/verbs/test_create_base_text_units.py::test_create_base_text_units`
- `tests/verbs/test_create_base_text_units.py::test_create_base_text_units_metadata`
- `tests/verbs/test_create_base_text_units.py::test_create_base_text_units_metadata_included_in_chunk`
- `tests/verbs/test_create_communities.py::test_create_communities`
- `tests/verbs/test_create_community_reports.py::test_create_community_reports`
- `tests/verbs/test_create_final_documents.py::test_create_final_documents`
- `tests/verbs/test_create_final_text_units.py::test_create_final_text_units`
- `tests/verbs/test_extract_covariates.py::test_extract_covariates`
- `tests/verbs/test_finalize_graph.py::_prep_tables`
- `tests/verbs/util.py::create_test_context`

