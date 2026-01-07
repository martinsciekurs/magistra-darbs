---
sidebar_position: 463
---

# test_missing_openai_required_api_key

**File:** `tests/unit/config/test_config.py` (lines 24-42)

## Signature

```python
def test_missing_openai_required_api_key() -> None
```

## Description

Test that missing required API keys for OpenAI models raise ValidationError.

This test builds a model configuration lacking API keys for OpenAIChat and asserts that create_graphrag_config raises ValidationError. It then changes the chat model type to OpenAIEmbedding and asserts that a ValidationError is raised again, this time due to a missing API key for the embedding model.

## Dependencies

This function calls:

- `graphrag/config/create_graphrag_config.py::create_graphrag_config`

