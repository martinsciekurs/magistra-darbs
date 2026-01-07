---
sidebar_position: 373
---

# get_candidate_covariates

**File:** `graphrag/query/input/retrieval/covariates.py` (lines 14-24)

## Signature

```python
def get_candidate_covariates(
    selected_entities: list[Entity],
    covariates: list[Covariate],
) -> list[Covariate]
```

## Description

Get all covariates that are related to selected entities.

Args:
    selected_entities: The list of Entity objects representing the selected entities.
    covariates: The list of Covariate objects to filter.

Returns:
    list[Covariate]: Covariates related to the selected entities.

## Example 💡 Generated

```python
from covariate_utils import get_candidate_covariates
from types import SimpleNamespace
sel = [SimpleNamespace(title="Entity A")]
covA = SimpleNamespace(subject_id="Entity A")
covC = SimpleNamespace(subject_id="Entity C")
covs = [covA, covC]
res = get_candidate_covariates(sel, covs)
print(res)  # covariates for Entity A
```

## Called By

This function is called by:

- `graphrag/query/context_builder/local_context.py::get_candidate_context`

