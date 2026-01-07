---
sidebar_position: 32
---

# graphrag/config/models/vector_store_schema_config.py

## Overview

Configures and validates the mapping of schema field names used by the vector store.

Purpose
- Centralizes the configuration of field names for id, vector, text, and attributes and provides validation to ensure field names are safe and valid.

Key exports
- DEFAULT_VECTOR_SIZE: int constant for default vector size (1536)
- VALID_IDENTIFIER_REGEX: compiled regular expression enforcing valid identifiers
- VectorStoreSchemaConfig: class that defines and validates the mapping of schema field names used by the vector store
- _validate_model(self): method to validate the model after the initial schema validation
- is_valid_field_name(field: str) -&gt; bool: function to check whether a field name is valid for CosmosDB
- _validate_schema(self) -&gt; None: method to validate the schema and raise ValueError if any unsafe or invalid field names are found

Brief summary
This module provides configuration and validation utilities for the vector store schema, enabling safe and consistent field naming across the vector store integration.

## Classes

- [`VectorStoreSchemaConfig`](../api/classes/graphrag-config-models-vector-store-schema-config-vectorstoreschemaconfig)

## Functions

- [`_validate_model`](../api/functions/graphrag-config-models-vector-store-schema-config-validate-model)
- [`is_valid_field_name`](../api/functions/graphrag-config-models-vector-store-schema-config-is-valid-field-name)
- [`_validate_schema`](../api/functions/graphrag-config-models-vector-store-schema-config-validate-schema)

