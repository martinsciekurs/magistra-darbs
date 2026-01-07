---
sidebar_position: 39
---

# graphrag/data_model/relationship.py

## Overview

Relationship data model for graph relationships.

Purpose
Define the Relationship dataclass and provide a dictionary-based constructor to instantiate it from data commonly obtained from external sources.

Public API
- Relationship: Dataclass representing a relationship between two entities in the graph data model. It captures identifiers, source and target references, optional descriptive text, ranking and weight, related text units, and arbitrary attributes.

- Relationship.from_dict(cls, d, id_key='id', short_id_key='human_readable_id', source_key='source', target_key='target', description_key='description', rank_key='rank', weight_key='weight', text_unit_ids_key='text_unit_ids', attributes_key='attributes') -&gt; 'Relationship'
  Creates a new Relationship from the dictionary data.

Args
- cls (type): The class.
- d (dict[str, Any]): The source dictionary containing the values for the Relationship fields.
- id_key (str): Key in d for the relationship's identifier. Defaults to "id".
- short_id_key (str): Key in d for the optional short identifier. Defaults to "human_readable_id".
- source_key (str): Key in d for the source reference.
- target_key (str): Key in d for the target reference.
- description_key (str): Key in d for the description.
- rank_key (str): Key in d for the rank.
- weight_key (str): Key in d for the weight.
- text_unit_ids_key (str): Key in d for text_unit_ids.
- attributes_key (str): Key in d for attributes.

Returns
- 'Relationship': The Relationship instance created from the dictionary data.

Raises
- May raise exceptions if the input data is invalid or keys are missing or of unexpected types.

## Classes

- [`Relationship`](../api/classes/graphrag-data-model-relationship-relationship)

## Functions

- [`from_dict`](../api/functions/graphrag-data-model-relationship-from-dict)

