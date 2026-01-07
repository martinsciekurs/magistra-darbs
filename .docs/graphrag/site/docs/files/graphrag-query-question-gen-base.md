---
sidebar_position: 200
---

# graphrag/query/question_gen/base.py

## Overview

Base question generation infrastructure for Graphrag.

Purpose:
Provide a common interface and shared setup for generating questions by coordinating a ChatModel with a context_builder (GlobalContextBuilder or LocalContextBuilder) and an optional Tokenizer. Subclasses implement the concrete generation logic.

Key exports:
- BaseQuestionGen: Abstract base class that wires together a language model, a context builder, and an optional tokenizer to enable question generation.

Summary:
This module defines the BaseQuestionGen class used by concrete question generators to produce questions from a question history and optional context data, delegating the actual generation to specialized implementations.

## Classes

- [`BaseQuestionGen`](../api/classes/graphrag-query-question-gen-base-basequestiongen)

## Functions

- [`generate`](../api/functions/graphrag-query-question-gen-base-generate)
- [`agenerate`](../api/functions/graphrag-query-question-gen-base-agenerate)
- [`__init__`](../api/functions/graphrag-query-question-gen-base-init)

