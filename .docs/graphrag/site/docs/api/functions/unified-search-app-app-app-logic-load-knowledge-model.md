---
sidebar_position: 588
---

# load_knowledge_model

**File:** `unified-search-app/app/app_logic.py` (lines 354-368)

## Signature

```python
def load_knowledge_model(sv: SessionVariables)
```

## Description

Load knowledge model from the datasource and populate the session variables with the loaded model data.

Args:
    sv (SessionVariables): The session variables container to be updated with the loaded knowledge model
        data, including entities, relationships, covariates, community reports, communities, and text units.
        The function also resets generated_questions and selected_question.

Returns:
    SessionVariables: The same sv object after it has been populated with the knowledge model data.

Raises:
    Propagates exceptions raised by load_model or datasource access as encountered.

## Called By

This function is called by:

- `unified-search-app/app/app_logic.py::load_dataset`

