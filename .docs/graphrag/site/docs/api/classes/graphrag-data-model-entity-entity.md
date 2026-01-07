---
sidebar_position: 114
---

# Entity

**File:** `graphrag/data_model/entity.py`

## Overview

Entity represents a graph entity with identifying information and metadata in the GraphRag data model.

This class encapsulates identifiers, descriptive metadata, embeddings, and relationships to related data such as text units and communities. It can be constructed from a dictionary via the from_dict class method, which supports configurable keys for mapping.

Key attributes:
- id: The unique identifier for the entity.
- human_readable_id: Optional short identifier for human-friendly display.
- title: Title of the entity.
- type: Classification type of the entity.
- description: Textual description of the entity.
- description_embedding: Embedding representation of the description.
- name_embedding: Embedding representation of the name.
- community: Community the entity belongs to.
- text_unit_ids: Identifiers of related text units.
- degree: Rank or degree of the entity.
- attributes: Additional attributes associated with the entity.

From dictionary construction:
- from_dict(cls, d, id_key="id", short_id_key="human_readable_id", title_key="title", type_key="type", description_key="description", description_embedding_key="description_embedding", name_embedding_key="name_embedding", community_key="community", text_unit_ids_key="text_unit_ids", rank_key="degree", attributes_key="attributes") creates an Entity from the provided dictionary using the given key mappings and defaults.

Returns: An Entity instance created from the input dictionary.

Raises: Exceptions may be raised by from_dict if the input data are invalid or required fields are missing.

## Methods

### `from_dict`

```python
def from_dict(
        cls,
        d: dict[str, Any],
        id_key: str = "id",
        short_id_key: str = "human_readable_id",
        title_key: str = "title",
        type_key: str = "type",
        description_key: str = "description",
        description_embedding_key: str = "description_embedding",
        name_embedding_key: str = "name_embedding",
        community_key: str = "community",
        text_unit_ids_key: str = "text_unit_ids",
        rank_key: str = "degree",
        attributes_key: str = "attributes",
    ) -> "Entity"
```

