---
sidebar_position: 621
---

# load_model

**File:** `unified-search-app/app/knowledge_loader/model.py` (lines 87-110)

## Signature

```python
def load_model(
    dataset: str,
    datasource: Datasource,
)
```

## Description

Load all relevant graph-indexed data into collections of knowledge model objects and store the model collections in the session variables.

This is a one-time data retrieval and preparation per session.

Args:
    dataset (str): The dataset identifier to load from.
    datasource (Datasource): The Datasource descriptor used to access the data.

Returns:
    KnowledgeModel: A KnowledgeModel containing the loaded DataFrames for entities, relationships, community_reports, communities, text_units, and covariates (covariates will be None if empty).

Raises:
    Exception: Propagates any exceptions raised by the underlying data-loading helpers (e.g., get_entity_data, get_relationship_data, get_covariate_data, get_community_report_data, get_communities_data, get_text_unit_data).

## Dependencies

This function calls:

- `unified-search-app/app/knowledge_loader/model.py::load_communities`
- `unified-search-app/app/knowledge_loader/model.py::load_community_reports`
- `unified-search-app/app/knowledge_loader/model.py::load_covariates`
- `unified-search-app/app/knowledge_loader/model.py::load_entities`
- `unified-search-app/app/knowledge_loader/model.py::load_entity_relationships`
- `unified-search-app/app/knowledge_loader/model.py::load_text_units`

