---
sidebar_position: 165
---

# graphrag/language_model/response/base.pyi

## Overview

GraphRAG language model response interfaces and type definitions.

Key exports:
- ModelOutput: Represents the outcome produced by a language model, providing access to the textual content and the complete raw payload when available.
- ModelResponse: Protocol describing a model response produced by the GraphRAG language model integration. This Protocol exposes three properties: parsed_response, history, and output, and is generic over _T, the type of the parsed_response.
- BaseModelOutput: BaseModelOutput stores the result produced by a language model, including the main content and an optional full_response payload.
- BaseModelResponse: BaseModelResponse is a generic container for the response produced by a base language model. It pairs the raw model output with optional parsed content and related metadata, and is parameterized by the type _T of the parsed response.

Brief summary:
This module defines the core data structures used to represent raw model outputs, the full payload, and an optional parsed interpretation, enabling convenient access to content, metadata, and history.

Args:
  None

Returns:
  None

Raises:
  None

## Classes

- [`ModelOutput`](../api/classes/graphrag-language-model-response-basei-modeloutput)
- [`ModelResponse`](../api/classes/graphrag-language-model-response-basei-modelresponse)
- [`BaseModelOutput`](../api/classes/graphrag-language-model-response-basei-basemodeloutput)
- [`BaseModelResponse`](../api/classes/graphrag-language-model-response-basei-basemodelresponse)

## Functions

- [`full_response`](../api/functions/graphrag-language-model-response-basei-full-response)
- [`parsed_response`](../api/functions/graphrag-language-model-response-basei-parsed-response)
- [`content`](../api/functions/graphrag-language-model-response-basei-content)
- [`__init__`](../api/functions/graphrag-language-model-response-basei-init)
- [`history`](../api/functions/graphrag-language-model-response-basei-history)
- [`__init__`](../api/functions/graphrag-language-model-response-basei-init)
- [`output`](../api/functions/graphrag-language-model-response-basei-output)

