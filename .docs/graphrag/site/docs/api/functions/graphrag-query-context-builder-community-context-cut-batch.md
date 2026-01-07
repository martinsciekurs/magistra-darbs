---
sidebar_position: 328
---

# _cut_batch

**File:** `graphrag/query/context_builder/community_context.py` (lines 132-149)

## Signature

```python
def _cut_batch() -> None
```

## Description

Convert the current batch of context records to a DataFrame, convert it to CSV, and append it to the aggregated context. This function calls _convert_report_context_to_df with context_records=batch_records and header=header, passing weight_column as community_weight_name if entities and include_community_weight are truthy, otherwise None, and rank_column as community_rank_name if include_community_rank is truthy, otherwise None. If the resulting DataFrame is empty, the function returns without modification. Otherwise, it converts the DataFrame to CSV with index=None and sep=column_delimiter. If not all_context_text and single_batch, it prefixes the current context header to the CSV text. Finally, it appends the CSV text to all_context_text and the DataFrame to all_context_records. Returns: None

## Dependencies

This function calls:

- `graphrag/query/context_builder/community_context.py::_convert_report_context_to_df`

## Called By

This function is called by:

- `graphrag/query/context_builder/community_context.py::build_community_context`

