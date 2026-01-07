---
sidebar_position: 103
---

# graphrag/index/typing/pipeline.py

## Overview

Module providing a Pipeline container for named Workflow objects used in the graphrag index typing.

Purpose
    Provide a lightweight, ordered container that stores (name, Workflow) pairs and supports inspection and mutation of the pipeline.

Key exports
    Pipeline: Class that stores and manages the sequence of (name, Workflow) pairs and exposes operations to remove entries by name, iterate over entries, and retrieve names.

Brief summary
    The Pipeline maintains an internal list of (name, Workflow) tuples, preserving insertion order. It supports removing all entries with a given name, iterating over current entries (run), and retrieving the list of names (names).

Attributes
    workflows: list[tuple[str, Workflow]] - internal storage of the pipeline entries.

## Classes

- [`Pipeline`](../api/classes/graphrag-index-typing-pipeline-pipeline)

## Functions

- [`remove`](../api/functions/graphrag-index-typing-pipeline-remove)
- [`__init__`](../api/functions/graphrag-index-typing-pipeline-init)
- [`run`](../api/functions/graphrag-index-typing-pipeline-run)
- [`names`](../api/functions/graphrag-index-typing-pipeline-names)

