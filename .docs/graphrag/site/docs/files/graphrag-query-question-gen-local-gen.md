---
sidebar_position: 201
---

# graphrag/query/question_gen/local_gen.py

## Overview

Module for local question generation using a local context builder and a language model.

Overview:
This module defines LocalQuestionGen, which coordinates a LocalContextBuilder and a ChatModel to generate questions based on a history of previously asked questions and optional context data. It provides asynchronous and synchronous generation via agenerate and generate, respectively, and uses a configurable system prompt (defaulting to QUESTION_SYSTEM_PROMPT).

Exports:
- LocalQuestionGen: Class that orchestrates the local context building and model interaction
- agenerate: Async method to generate a question
- generate: Sync method to generate a question

Summary:
The LocalQuestionGen class offers a high-level API to produce follow-up questions by combining locally built context with a language model's generation capability.

## Classes

- [`LocalQuestionGen`](../api/classes/graphrag-query-question-gen-local-gen-localquestiongen)

## Functions

- [`agenerate`](../api/functions/graphrag-query-question-gen-local-gen-agenerate)
- [`generate`](../api/functions/graphrag-query-question-gen-local-gen-generate)
- [`__init__`](../api/functions/graphrag-query-question-gen-local-gen-init)

