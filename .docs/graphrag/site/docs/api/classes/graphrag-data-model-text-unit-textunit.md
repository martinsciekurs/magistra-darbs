---
sidebar_position: 68
---

# TextUnit

**File:** `graphrag/data_model/text_unit.py`

## Overview

TextUnit is a data model that encapsulates a unit of text and its metadata for graph-based data handling.

Purpose:
- Store the text content together with identifiers linking it to entities, relationships, covariates, and related documents.

Inherits:
- Identified to provide a stable, unique identifier for the text unit.

Key attributes:
- id: Text unit identifier.
- human_readable_id: Optional short identifier.
- text: The actual text content.
- entity_ids: Identifiers of entities present in the text.
- relationship_ids: Identifiers of relationships associated with the text.
- covariate_ids: Identifiers of covariates linked to the text.
- n_tokens: Number of tokens in the text.
- document_ids: Identifiers of documents containing the text unit.
- attributes: Additional arbitrary attributes.

From dictionary construction:
- This class provides a from_dict classmethod to construct a TextUnit from a dictionary, mapping configured keys to the corresponding fields.

Args:
- cls: The class.
- d (dict[str, Any]): The source dictionary containing the values for the TextUnit fields.
- id_key (str): Key in d for the text unit's identifier. Defaults to "id".
- short_id_key (str): Key in d for the optional short identifier. Defaults to "human_readable_id".
- text_key (str): Key in d for the text content. Defaults to "text".
- entities_key (str): Key in d for the entity identifiers. Defaults to "entity_ids".
- relationships_key (str): Key in d for the relationship identifiers. Defaults to "relationship_ids".
- covariates_key (str): Key in d for the covariate identifiers. Defaults to "covariate_ids".
- n_tokens_key (str): Key in d for the token count. Defaults to "n_tokens".
- document_ids_key (str): Key in d for the document identifiers. Defaults to "document_ids".
- attributes_key (str): Key in d for the attributes. Defaults to "attributes".

Returns:
- TextUnit: A new TextUnit instance constructed from the provided dictionary data.

Raises:
- May raise exceptions stemming from dictionary access or type mismatches depending on input data.

## Methods

### `from_dict`

```python
def from_dict(
        cls,
        d: dict[str, Any],
        id_key: str = "id",
        short_id_key: str = "human_readable_id",
        text_key: str = "text",
        entities_key: str = "entity_ids",
        relationships_key: str = "relationship_ids",
        covariates_key: str = "covariate_ids",
        n_tokens_key: str = "n_tokens",
        document_ids_key: str = "document_ids",
        attributes_key: str = "attributes",
    ) -> "TextUnit"
```

