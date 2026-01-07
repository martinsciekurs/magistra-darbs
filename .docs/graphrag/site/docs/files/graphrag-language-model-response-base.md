---
sidebar_position: 164
---

# graphrag/language_model/response/base.py

## Overview

Module providing typed containers for LLM provider responses.

Purpose
Provide typed containers to represent responses from a language model provider, including the textual output, the provider's full JSON response, and optional parsed model instances, along with a simple history of responses.

Exports
- ModelResponse: a generic container for responses from an LLM provider, parameterized by T
- ModelOutput: a container that bundles the textual content with the full JSON response
- T: TypeVar bound to BaseModel, used to type the parsed_response

Summary
This module defines ModelResponse[T] and ModelOutput to model LLM outputs in a type-safe way. ModelResponse holds the output, the complete provider response, an optional parsed model instance, and a history of responses. ModelOutput provides access to content and the complete raw response.

## Classes

- [`ModelResponse`](../api/classes/graphrag-language-model-response-base-modelresponse)
- [`ModelOutput`](../api/classes/graphrag-language-model-response-base-modeloutput)

## Functions

- [`output`](../api/functions/graphrag-language-model-response-base-output)
- [`history`](../api/functions/graphrag-language-model-response-base-history)
- [`parsed_response`](../api/functions/graphrag-language-model-response-base-parsed-response)
- [`content`](../api/functions/graphrag-language-model-response-base-content)
- [`full_response`](../api/functions/graphrag-language-model-response-base-full-response)

