---
sidebar_position: 144
---

# Community

**File:** `graphrag/data_model/community.py`

## Overview

Dataclass representing a Community in the graph data model, extending Named with community-specific metadata and relationships. It encapsulates identity, hierarchical placement, and associations to entities, relationships, text units, and covariates.

Inherits from Named to provide consistent identity and naming semantics across the graph model. This class is a dataclass and is intended to be instantiated directly or via the from_dict factory method.

Attributes:
- id (str): Unique identifier of the community.
- title (str): Human-readable title of the community.
- human_readable_id (Optional[str]): Optional short identifier for human readability (default: None).
- level (int): Hierarchical level of the community within the graph.
- entity_ids (List[str]): Identifiers of entities belonging to the community.
- relationship_ids (List[str]): Identifiers of relationships associated with the community.
- text_unit_ids (List[str]): Identifiers of text units in the community.
- covariate_ids (List[str]): Identifiers of covariates associated with the community.
- parent (Optional[str]): Identifier of the parent community, if any (default: None).
- children (List[str]): Identifiers of child communities.
- attributes (Dict[str, Any]): Additional attributes describing the community (default: empty dict).
- size (Optional[int]): Size metric for the community (default: None).
- period (Optional[str]): Time period associated with the community (default: None).

Factory methods:
- from_dict: Classmethod that constructs a Community from a dictionary using configurable keys. It maps dict keys to the corresponding fields (with defaults for key names) and returns a Community instance populated from the provided data.

## Methods

### `from_dict`

```python
def from_dict(
        cls,
        d: dict[str, Any],
        id_key: str = "id",
        title_key: str = "title",
        short_id_key: str = "human_readable_id",
        level_key: str = "level",
        entities_key: str = "entity_ids",
        relationships_key: str = "relationship_ids",
        text_units_key: str = "text_unit_ids",
        covariates_key: str = "covariate_ids",
        parent_key: str = "parent",
        children_key: str = "children",
        attributes_key: str = "attributes",
        size_key: str = "size",
        period_key: str = "period",
    ) -> "Community"
```

