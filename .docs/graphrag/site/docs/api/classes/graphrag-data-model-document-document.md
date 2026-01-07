---
sidebar_position: 93
---

# Document

**File:** `graphrag/data_model/document.py`

## Overview

Document data model representing a document in the GraphRag data model.

Purpose:
Encapsulates identifiers, metadata, and content for a document, supporting construction from a dictionary.

Key attributes:
- id: The document's identifier.
- human_readable_id: Optional short identifier.
- title: The document title.
- type: The document type.
- text: The document text content.
- text_units: Units describing text content.
- attributes: Additional attributes associated with the document.

From dictionary construction:
The class provides a from_dict classmethod to create a Document instance from a dictionary. The method accepts keys for each field, with sensible defaults:
- id_key: Key in d for the document's identifier. Defaults to "id".
- short_id_key: Key in d for the optional short identifier. Defaults to "human_readable_id".
- title_key: Key in d for the title. Defaults to "title".
- type_key: Key in d for the document's type. Defaults to "type".
- text_key: Key in d for the document's text. Defaults to "text".
- text_units_key: Key in d for the text units. Defaults to "text_units".
- attributes_key: Key in d for the document's attributes. Defaults to "attributes".

Returns:
Document: The constructed Document instance.

Raises:
None documented.

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
        text_key: str = "text",
        text_units_key: str = "text_units",
        attributes_key: str = "attributes",
    ) -> "Document"
```

