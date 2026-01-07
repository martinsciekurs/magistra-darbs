---
sidebar_position: 174
---

# graphrag/prompt_tune/generator/entity_relationship.py

## Overview

Utilities for generating entity-relationship prompt examples for prompt tuning.

Purpose
Provide a helper to generate a list of entity/relationship examples to assist in configuring prompts for an entity-relationship model. Generation is performed via a ChatModel using the supplied persona, optional entity types, documentation strings, and a target language, with optional JSON formatting.

Key exports
- generate_entity_relationship_examples(model, persona, entity_types, docs, language, json_mode=False) -&gt; list[str]

Notes
This module defines a top-level constant MAX_EXAMPLES = 5 to limit the number of generated examples.

## Functions

- [`generate_entity_relationship_examples`](../api/functions/graphrag-prompt-tune-generator-entity-relationship-generate-entity-relationship-examples)

