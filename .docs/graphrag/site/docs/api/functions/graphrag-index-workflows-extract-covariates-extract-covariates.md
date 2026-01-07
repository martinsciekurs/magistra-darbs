---
sidebar_position: 239
---

# extract_covariates

**File:** `graphrag/index/workflows/extract_covariates.py` (lines 64-93)

## Signature

```python
def extract_covariates(
    text_units: pd.DataFrame,
    callbacks: WorkflowCallbacks,
    cache: PipelineCache,
    covariate_type: str,
    extraction_strategy: dict[str, Any] | None,
    async_mode: AsyncType = AsyncType.AsyncIO,
    entity_types: list[str] | None = None,
    num_threads: int = 4,
) -> pd.DataFrame
```

## Description

All the steps to extract and format covariates.

Args:
- text_units (pd.DataFrame): Input text units to process. Must contain at least the columns "id" and "text". This function mutates text_units in place by adding a temporary text_unit_id column equal to id, and then removes it before returning.
- callbacks (WorkflowCallbacks): Callbacks used during the extraction workflow.
- cache (PipelineCache): Cache for the extraction process.
- covariate_type (str): Covariate type to extract (for example, "claim").
- extraction_strategy (dict[str, Any] | None): Configuration for the extraction strategy or None.
- async_mode (AsyncType): Asynchronous execution mode to use.
- entity_types (list[str] | None): Entity types to consider; None to include all.
- num_threads (int): Number of threads for the extraction step.

Returns:
pd.DataFrame: A covariates dataframe containing the final columns defined by COVARIATES_FINAL_COLUMNS. Each row represents an extracted covariate and is augmented with a unique id and a human_readable_id corresponding to the dataframe index.

Side effects:
- The input text_units DataFrame is mutated in place by adding a temporary text_unit_id column equal to the original id, which is dropped before returning.

Raises:
- KeyError if required columns (e.g., "id" or "text") are missing from text_units.
- ValueError, TypeError, or other exceptions raised by the underlying extractor if inputs are invalid.

Example:
Suppose text_units is a DataFrame with columns ["id", "text"] and two rows. After calling extract_covariates with appropriate callbacks, cache, covariate_type, and strategy, the function returns a covariates DataFrame containing the final covariate columns as defined by COVARIATES_FINAL_COLUMNS, with additional id (uuid4) and human_readable_id (index) columns. The original text_units is restored after processing aside from the transient in-place mutation during execution.

