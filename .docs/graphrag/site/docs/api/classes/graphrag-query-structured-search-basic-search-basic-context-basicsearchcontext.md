---
sidebar_position: 62
---

# BasicSearchContext

**File:** `graphrag/query/structured_search/basic_search/basic_context.py`

## Overview

Builds and manages the context used by the basic search mode in graphrag.

Purpose:
The BasicSearchContext encapsulates the logic to construct a coherent, compact context for a user query by leveraging an embedding model and a vector store of text units. It can incorporate optional conversation history and token constraints when building the context via build_context, coordinating with the BasicContextBuilder to produce a ContextBuilderResult.

Attributes:
text_embedder: EmbeddingModel
text_unit_embeddings: BaseVectorStore
text_units: list[TextUnit] | None
tokenizer: Tokenizer | None
embedding_vectorstore_key: str

Args:
text_embedder (EmbeddingModel): The embedding model used to embed text for similarity search
text_unit_embeddings (BaseVectorStore): The vector store containing embeddings for text units
text_units (list[TextUnit] | None): Optional list of text units to consider
tokenizer (Tokenizer | None): Optional tokenizer to use
embedding_vectorstore_key (str): The key in the vector store that identifies items (default "id")

Returns:
None

Raises:
AttributeError: If any text unit is missing 'id' or 'short_id' attributes when mapping ids via _map_ids

## Methods

### `_map_ids`

```python
def _map_ids(self) -> dict[str, str]
```

### `build_context`

```python
def build_context(
        self,
        query: str,
        conversation_history: ConversationHistory | None = None,
        k: int = 10,
        max_context_tokens: int = 12_000,
        context_name: str = "Sources",
        column_delimiter: str = "|",
        text_id_col: str = "source_id",
        text_col: str = "text",
        **kwargs,
    ) -> ContextBuilderResult
```

### `__init__`

```python
def __init__(
        self,
        text_embedder: EmbeddingModel,
        text_unit_embeddings: BaseVectorStore,
        text_units: list[TextUnit] | None = None,
        tokenizer: Tokenizer | None = None,
        embedding_vectorstore_key: str = "id",
    )
```

