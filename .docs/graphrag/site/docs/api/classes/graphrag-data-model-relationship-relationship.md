---
sidebar_position: 95
---

# Relationship

**File:** `graphrag/data_model/relationship.py`

## Overview

Represents a relationship between two entities in the graph data model.

This dataclass captures metadata about a relationship, including identifiers, source
and target references, descriptive text, ranking and weight, related text units, and
arbitrary attributes.

Args:
    id: Unique identifier for the relationship.
    short_id: Optional short identifier (human_readable_id).
    source: Reference to the source entity in the relationship.
    target: Reference to the target entity in the relationship.
    description: Description of the relationship.
    rank: Ranking value for ordering or prioritization.
    weight: Weight or strength of the relationship.
    text_unit_ids: Identifiers of related text units.
    attributes: Arbitrary additional attributes associated with the relationship.

Returns:
    Relationship: A Relationship instance created from dictionary data via from_dict.

Raises:
    KeyError: If required keys are missing from the input dictionary during construction.
    TypeError: If input data types are not as expected.

## Methods

### `from_dict`

```python
def from_dict(
        cls,
        d: dict[str, Any],
        id_key: str = "id",
        short_id_key: str = "human_readable_id",
        source_key: str = "source",
        target_key: str = "target",
        description_key: str = "description",
        rank_key: str = "rank",
        weight_key: str = "weight",
        text_unit_ids_key: str = "text_unit_ids",
        attributes_key: str = "attributes",
    ) -> "Relationship"
```

