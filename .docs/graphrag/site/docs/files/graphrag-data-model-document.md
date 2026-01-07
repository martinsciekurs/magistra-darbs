---
sidebar_position: 37
---

# graphrag/data_model/document.py

## Overview

Data model and factory for GraphRag Document.

Purpose:
Provide a dataclass-based model for a GraphRag Document and a factory to build it from a dictionary with configurable key mappings.

Exports:
- Document: Dataclass representing a document with fields such as id, human_readable_id, title, type, text, text_units, and attributes.
- Document.from_dict: Classmethod to construct a Document from a dictionary using key mappings.

Summary:
The Document class encapsulates identifiers, metadata, and content for a document and supports construction from a dictionary, enabling flexible deserialization from diverse input shapes.

## Classes

- [`Document`](../api/classes/graphrag-data-model-document-document)

## Functions

- [`from_dict`](../api/functions/graphrag-data-model-document-from-dict)

