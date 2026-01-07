---
sidebar_position: 40
---

# graphrag/data_model/text_unit.py

## Overview

Text unit data model for graph-based text data handling.

This module defines the TextUnit data model, which encapsulates a unit of text and its metadata for graph-based data handling, including identifiers linking it to entities, relationships, covariates, and related documents. It inherits from Identified to provide a stable, unique identifier for the text unit.

Public exports:
- TextUnit: Data model class representing a unit of text and its metadata.
- TextUnit.from_dict: Classmethod to construct a TextUnit from a dictionary.

Summary:
- TextUnit stores the text content together with identifiers linking it to entities, relationships, covariates, and related documents.
- The module supports constructing TextUnit instances from dictionary data via from_dict.

Classes:
- TextUnit: Data model for a unit of text and its metadata.

Functions:
- TextUnit.from_dict(cls, d: dict[str, Any], id_key: str = "id", short_id_key: str = "human_readable_id", text_key: str = "text", entities_key: str = "entity_ids", relationships_key: str = "relationship_ids", covariates_key: str = "covariate_ids", n_tokens_key: str = "n_tokens", document_ids_key: str = "document_ids", attributes_key: str = "attributes") -&gt; "TextUnit": Create a new TextUnit from the dict data.
  Args:
    cls: The class.
    d (dict[str, Any]): The source dictionary containing the values for the TextUnit fields.
    id_key (str): Key in d for the text unit's identifier. Defaults to "id".
    short_id_key (str): Key in d for the optional short identifier. Defaults to "human_readable_id".
    text_key (str): Key in d for the text content. Defaults to "text".
    entities_key (str): Key in d for the associated entity identifiers. Defaults to "entity_ids".
    relationships_key (str): Key in d for the related relationship identifiers. Defaults to "relationship_ids".
    covariates_key (str): Key in d for the associated covariate identifiers. Defaults to "covariate_ids".
    n_tokens_key (str): Key in d for the number of tokens. Defaults to "n_tokens".
    document_ids_key (str): Key in d for related document identifiers. Defaults to "document_ids".
    attributes_key (str): Key in d for additional attributes. Defaults to "attributes".
  Returns:
    TextUnit: New TextUnit instance constructed from the provided data.
  Raises:
    (Depending on input) ValueError, KeyError, or TypeError if the input data are invalid or incomplete.

## Classes

- [`TextUnit`](../api/classes/graphrag-data-model-text-unit-textunit)

## Functions

- [`from_dict`](../api/functions/graphrag-data-model-text-unit-from-dict)

