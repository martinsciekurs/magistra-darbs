---
sidebar_position: 128
---

# Covariate

**File:** `graphrag/data_model/covariate.py`

## Overview

Covariate model representing a covariate linked to a subject in the graph-based data model.

This class encapsulates a covariate's identity, its association with a subject, its covariate_type, a human_readable_id, related text_unit_ids, and additional attributes. The id attribute is inherited from the Identified base class.

Key attributes
- id: Unique identifier for the covariate (inherited from Identified)
- subject_id: Identifier of the subject this covariate pertains to
- covariate_type: Type or category of the covariate
- human_readable_id: Short, human-readable identifier
- text_unit_ids: Collection of text unit identifiers related to this covariate
- attributes: Additional arbitrary attributes for the covariate

Brief summary
Describes a covariate and its relationships to subjects and text units, with a utility to construct instances from a dictionary via from_dict.

From_dict
This classmethod constructs a Covariate from a dictionary. It reads and uses the following keys by default: id ("id"), subject_id ("subject_id"), covariate_type ("covariate_type"), human_readable_id ("human_readable_id"), text_unit_ids ("text_unit_ids"), attributes ("attributes"). The keys can be customized via id_key, subject_id_key, covariate_type_key, short_id_key, text_unit_ids_key, and attributes_key.

Args
- cls (type Covariate): The Covariate class; this is a classmethod.
- d (dict[str, Any]): The dictionary containing covariate fields.
- id_key (str): The key in d that corresponds to the covariate id (default "id")
- subject_id_key (str): The key in d for the subject identifier (default "subject_id")
- covariate_type_key (str): The key in d for the covariate type (default "covariate_type")
- short_id_key (str): The key in d for the human-readable id (default "human_readable_id")
- text_unit_ids_key (str): The key in d for the text unit identifiers (default "text_unit_ids")
- attributes_key (str): The key in d for the attributes dictionary (default "attributes")

Returns
- Covariate: An instance populated from the provided data

Raises
- KeyError: If required keys are missing from the input dictionary
- TypeError: If any field has an inappropriate type

## Methods

### `from_dict`

```python
def from_dict(
        cls,
        d: dict[str, Any],
        id_key: str = "id",
        subject_id_key: str = "subject_id",
        covariate_type_key: str = "covariate_type",
        short_id_key: str = "human_readable_id",
        text_unit_ids_key: str = "text_unit_ids",
        attributes_key: str = "attributes",
    ) -> "Covariate"
```

