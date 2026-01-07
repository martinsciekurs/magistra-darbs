---
sidebar_position: 36
---

# graphrag/data_model/covariate.py

## Overview

Covariate data model for graph-based covariates linked to subjects.

Purpose:
Defines the Covariate data model used to represent a covariate associated with a subject in the graph-based data model. The Covariate includes an identity (inherited from Identified), a covariate_type, a human_readable_id, related text_unit_ids, and additional attributes.

Exports:
- Covariate: The Covariate model class
- Covariate.from_dict: Classmethod to construct a Covariate from a dictionary

Summary:
The module exposes the Covariate class and a factory method from_dict to build Covariate instances from dictionaries by reading keys such as id_key, subject_id_key, covariate_type_key, short_id_key, text_unit_ids_key, and attributes_key.

## Classes

- [`Covariate`](../api/classes/graphrag-data-model-covariate-covariate)

## Functions

- [`from_dict`](../api/functions/graphrag-data-model-covariate-from-dict)

