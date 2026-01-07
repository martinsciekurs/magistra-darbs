---
sidebar_position: 103
---

# run

**File:** `graphrag/index/operations/embed_text/strategies/openai.py` (lines 26-76)

## Signature

```python
def run(
    input: list[str],
    callbacks: WorkflowCallbacks,
    cache: PipelineCache,
    args: dict[str, Any],
) -> TextEmbeddingResult
```

## Description

Run the Claim extraction chain.

Args:
    input: list[str] The input texts to process.
    callbacks: WorkflowCallbacks The callbacks interface for progress and other hooks.
    cache: PipelineCache The cache to use for model embeddings and related data.
    args: dict[str, Any] Additional arguments for configuring the run (e.g., batch_size, batch_max_tokens, llm).

Returns:
    TextEmbeddingResult The embedding results for the input texts, or embeddings=None if the input is null.

Raises:
    None

## Dependencies

This function calls:

- `graphrag/config/models/language_model_config.py::LanguageModelConfig`
- `graphrag/index/operations/embed_text/strategies/openai.py::_create_text_batches`
- `graphrag/index/operations/embed_text/strategies/openai.py::_execute`
- `graphrag/index/operations/embed_text/strategies/openai.py::_get_splitter`
- `graphrag/index/operations/embed_text/strategies/openai.py::_prepare_embed_texts`
- `graphrag/index/operations/embed_text/strategies/openai.py::_reconstitute_embeddings`
- `graphrag/index/operations/embed_text/strategies/typing.py::TextEmbeddingResult`
- `graphrag/index/utils/is_null.py::is_null`
- `graphrag/language_model/manager.py::ModelManager`
- `graphrag/logger/progress.py::progress_ticker`

