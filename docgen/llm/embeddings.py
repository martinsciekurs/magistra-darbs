"""Embeddings and vector storage using ChromaDB."""

import os
import logging
from pathlib import Path
from typing import List, Optional

import chromadb
from chromadb.utils import embedding_functions
from chromadb.api.types import EmbeddingFunction, Embeddings

try:
    import requests
except ImportError:
    requests = None

from docgen.llm.client import track_embedding_tokens
from docgen.llm.langfuse_client import track_embedding_generation
from docgen.utils.config import ENABLE_EMBEDDINGS

logger = logging.getLogger("docgen")


class OpenAIEmbeddingFunctionWithTracking(EmbeddingFunction):
    """Custom OpenAI embedding function with token usage tracking."""
    
    def __init__(self, api_key: str, model_name: str, repo_name: str = None):
        """
        Initialize OpenAI embedding function with tracking.
        
        Args:
            api_key: OpenAI API key
            model_name: Name of the OpenAI embedding model to use
            repo_name: Optional repository name for session grouping
        """
        self.api_key = api_key
        self.model_name = model_name
        self.repo_name = repo_name
    
    def __call__(self, input: List[str]) -> Embeddings:
        """
        Generate embeddings for a list of texts.
        
        Args:
            input: List of texts to embed
            
        Returns:
            List of embedding vectors
        """
        try:
            from openai import OpenAI
        except ImportError:
            raise ImportError("openai package is required for OpenAI embeddings. Install with: pip install openai")
        
        client = OpenAI(api_key=self.api_key)
        
        # Batch call: OpenAI supports multiple inputs per request.
        response = client.embeddings.create(
            model=self.model_name,
            input=input
        )

        embeddings: list[list[float]] = []
        if getattr(response, "data", None):
            embeddings = [item.embedding for item in response.data if getattr(item, "embedding", None)]

        # Track token usage (OpenAI returns batch usage for embeddings)
        total_prompt_tokens = 0
        total_tokens_sum = 0
        if hasattr(response, "usage") and response.usage:
            total_prompt_tokens = response.usage.prompt_tokens or 0
            total_tokens_sum = response.usage.total_tokens or total_prompt_tokens
        
        # Track tokens for all embeddings in this batch
        if total_prompt_tokens > 0:
            track_embedding_tokens(total_prompt_tokens, total_tokens_sum if total_tokens_sum > 0 else None)
        
        # Track in Langfuse if enabled
        if embeddings:
            token_usage = {
                "tokens": total_tokens_sum if total_tokens_sum > 0 else total_prompt_tokens,
                "prompt_tokens": total_prompt_tokens
            }
            metadata = {"phase": "embeddings"}
            if self.repo_name:
                metadata["repo_name"] = self.repo_name
            
            track_embedding_generation(
                input_texts=input,
                embeddings=embeddings,
                model=self.model_name,
                provider="openai",
                metadata=metadata,
                token_usage=token_usage,
                generation_name="openai_embedding"
            )
        
        return embeddings


class GoogleEmbeddingFunctionWithTracking(EmbeddingFunction):
    """Custom Google Gemini embedding function with token usage tracking (API key auth)."""

    def __init__(self, api_key: str, model_name: str, repo_name: str = None):
        """
        Initialize Google embedding function with tracking.

        Args:
            api_key: Google API key
            model_name: Name of the Google embedding model to use
            repo_name: Optional repository name for session grouping
        """
        self.api_key = api_key
        self.model_name = model_name
        self.repo_name = repo_name

    def __call__(self, input: List[str]) -> Embeddings:
        """
        Generate embeddings for a list of texts.

        Args:
            input: List of texts to embed

        Returns:
            List of embedding vectors
        """
        try:
            import google.generativeai as genai
        except ImportError:
            raise ImportError("google-generativeai package is required for Google embeddings. Install with: pip install google-generativeai")

        genai.configure(api_key=self.api_key)

        embeddings: list[list[float]] = []
        total_prompt_tokens = 0

        # Google's embed_content can handle batches
        for text in input:
            result = genai.embed_content(
                model=self.model_name,
                content=text,
                task_type="retrieval_document"
            )
            if result and "embedding" in result:
                embeddings.append(result["embedding"])
                # Note: Google doesn't always return token counts for embeddings
                # We estimate based on text length (~4 chars per token)
                total_prompt_tokens += len(text) // 4

        # Track tokens for all embeddings in this batch
        if total_prompt_tokens > 0:
            track_embedding_tokens(total_prompt_tokens)

        # Track in Langfuse if enabled
        if embeddings:
            token_usage = {
                "tokens": total_prompt_tokens,
                "prompt_tokens": total_prompt_tokens
            }
            metadata = {"phase": "embeddings"}
            if self.repo_name:
                metadata["repo_name"] = self.repo_name

            track_embedding_generation(
                input_texts=input,
                embeddings=embeddings,
                model=self.model_name,
                provider="gemini",
                metadata=metadata,
                token_usage=token_usage,
                generation_name="google_embedding"
            )

        return embeddings


class GoogleVertexEmbeddingFunctionWithTracking(EmbeddingFunction):
    """Custom Google Vertex AI embedding function with token usage tracking (ADC/gcloud auth)."""

    def __init__(self, project_id: str, location: str, model_name: str, repo_name: str = None):
        """
        Initialize Google Vertex AI embedding function with tracking.

        Args:
            project_id: Google Cloud project ID
            location: Google Cloud region (e.g., us-central1)
            model_name: Name of the embedding model to use
            repo_name: Optional repository name for session grouping
        """
        self.project_id = project_id
        self.location = location
        self.model_name = model_name
        self.repo_name = repo_name

    def __call__(self, input: List[str]) -> Embeddings:
        """
        Generate embeddings for a list of texts using Vertex AI.

        Args:
            input: List of texts to embed

        Returns:
            List of embedding vectors
        """
        try:
            import vertexai
            from vertexai.language_models import TextEmbeddingModel
        except ImportError:
            raise ImportError("google-cloud-aiplatform package is required for Vertex AI embeddings. Install with: pip install google-cloud-aiplatform")

        vertexai.init(project=self.project_id, location=self.location)
        model = TextEmbeddingModel.from_pretrained(self.model_name)

        embeddings: list[list[float]] = []
        total_prompt_tokens = 0

        # Vertex AI supports batch embedding
        results = model.get_embeddings(input)
        for i, embedding_result in enumerate(results):
            embeddings.append(embedding_result.values)
            # Estimate tokens based on text length (~4 chars per token)
            total_prompt_tokens += len(input[i]) // 4

        # Track tokens for all embeddings in this batch
        if total_prompt_tokens > 0:
            track_embedding_tokens(total_prompt_tokens)

        # Track in Langfuse if enabled
        if embeddings:
            token_usage = {
                "tokens": total_prompt_tokens,
                "prompt_tokens": total_prompt_tokens
            }
            metadata = {"phase": "embeddings"}
            if self.repo_name:
                metadata["repo_name"] = self.repo_name

            track_embedding_generation(
                input_texts=input,
                embeddings=embeddings,
                model=self.model_name,
                provider="gemini-vertex",
                metadata=metadata,
                token_usage=token_usage,
                generation_name="vertex_embedding"
            )

        return embeddings


class OllamaEmbeddingFunctionWithOptions(EmbeddingFunction):
    """Custom Ollama embedding function with num_ctx option support."""
    
    def __init__(self, url: str, model_name: str, options: dict = None, repo_name: str = None):
        """
        Initialize Ollama embedding function.
        
        Args:
            url: Base URL for Ollama API (e.g., "http://localhost:11434/api/embeddings")
            model_name: Name of the Ollama model to use
            repo_name: Optional repository name for session grouping
            options: Additional options to pass to Ollama (e.g., {"num_ctx": 8192})
        """
        self.url = url
        self.model_name = model_name
        self.options = options or {}
        self.repo_name = repo_name
    
    def __call__(self, input: List[str]) -> Embeddings:
        """
        Generate embeddings for a list of texts.
        
        Args:
            input: List of texts to embed
            
        Returns:
            List of embedding vectors
        """
        if requests is None:
            raise ImportError("requests package is required for Ollama embeddings. Install with: pip install requests")
        
        embeddings = []
        total_prompt_tokens = 0
        
        # Get context window size from options (default to 8192 if not specified)
        num_ctx = self.options.get("num_ctx", 8192)
        # Conservative estimate: code can have variable token-to-char ratio (2-4 chars/token)
        # Account for overhead and model-specific limits by using ~60% of token limit
        # For num_ctx=8192: 8192 * 0.6 * 2.5 = ~12,288 chars theoretical max
        # But since 7641 chars failed, use more conservative limit: 5000 chars
        # This ensures we stay well under the limit even with dense code and overhead
        max_safe_chars = min(5000, int(num_ctx * 0.6 * 2.5))
        
        for text in input:
            # Defensive truncation: ensure text never exceeds safe character limit
            # This is a safety net even if upstream truncation missed something
            original_len = len(text)
            if len(text) > max_safe_chars:
                text = text[:max_safe_chars]
                if original_len > max_safe_chars:
                    text += "\n\n[... code truncated for embedding ...]"
            
            payload = {
                "model": self.model_name,
                "prompt": text,
                "options": self.options
            }
            
            response = requests.post(self.url, json=payload, timeout=60)
            
            # Check status and log full error response if failed
            if not response.ok:
                error_detail = f"Status: {response.status_code}, Response: {response.text}"
                logger.error(f"Ollama embedding error: {error_detail}")
                response.raise_for_status()
            
            result = response.json()
            if "embedding" in result:
                embeddings.append(result["embedding"])
                # Track token usage from Ollama response
                # Ollama returns prompt_eval_count which is the number of tokens processed
                prompt_eval_count = result.get("prompt_eval_count", 0)
                if prompt_eval_count > 0:
                    total_prompt_tokens += prompt_eval_count
            else:
                raise ValueError(f"Unexpected response format from Ollama: {result}")
        
        # Track tokens for all embeddings in this batch
        if total_prompt_tokens > 0:
            track_embedding_tokens(total_prompt_tokens)
        
        # Track in Langfuse if enabled
        if embeddings:
            token_usage = {
                "tokens": total_prompt_tokens,
                "prompt_tokens": total_prompt_tokens
            }
            metadata = {"phase": "embeddings"}
            if self.repo_name:
                metadata["repo_name"] = self.repo_name
            
            track_embedding_generation(
                input_texts=input,
                embeddings=embeddings,
                model=self.model_name,
                provider="ollama",
                metadata=metadata,
                token_usage=token_usage,
                generation_name="ollama_embedding"
            )
        
        return embeddings


def get_embedding_function(repo_name: str = None):
    """Get the appropriate embedding function based on LLM_PROVIDER.
    
    Args:
        repo_name: Optional repository name for session grouping
    """
    provider = os.getenv("LLM_PROVIDER", "openai").lower()
    
    if provider == "openai":
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set")
        model = os.getenv("OPENAI_EMBEDDING_MODEL")
        if not model:
            raise ValueError("OPENAI_EMBEDDING_MODEL environment variable not set")
        return OpenAIEmbeddingFunctionWithTracking(api_key=api_key, model_name=model, repo_name=repo_name)
    elif provider == "ollama":
        base_url = os.getenv("OLLAMA_BASE_URL")
        if not base_url:
            raise ValueError("OLLAMA_BASE_URL environment variable not set")
        model = os.getenv("OLLAMA_EMBEDDING_MODEL")
        if not model:
            raise ValueError("OLLAMA_EMBEDDING_MODEL environment variable not set")
        
        if requests is None:
            raise ImportError("requests package is required for Ollama connection check. Install with: pip install requests")
        
        try:
            check_url = f"{base_url}/api/tags"
            response = requests.get(check_url, timeout=5)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise ConnectionError(
                f"Cannot connect to Ollama at {base_url}. "
                f"Make sure Ollama is running. Error: {e}"
            )
        
        return OllamaEmbeddingFunctionWithOptions(
            url=f"{base_url}/api/embeddings",
            model_name=model,
            options={"num_ctx": 8192},
            repo_name=repo_name
        )
    elif provider == "gemini":
        api_key = os.getenv("GOOGLE_API_KEY")
        project_id = os.getenv("GOOGLE_PROJECT_ID")

        if api_key:
            model = os.getenv("GOOGLE_EMBEDDING_MODEL", "text-embedding-004")
            return GoogleEmbeddingFunctionWithTracking(api_key=api_key, model_name=model, repo_name=repo_name)
        elif project_id:
            location = os.getenv("GOOGLE_LOCATION", "us-central1")
            model = os.getenv("GOOGLE_EMBEDDING_MODEL", "text-embedding-005")
            return GoogleVertexEmbeddingFunctionWithTracking(
                project_id=project_id, location=location, model_name=model, repo_name=repo_name
            )
        else:
            raise ValueError("Either GOOGLE_API_KEY or GOOGLE_PROJECT_ID must be set for Gemini provider")
    elif provider in ("deepseek", "anthropic"):
        # DeepSeek and Anthropic don't have embedding models, fall back to OpenAI embeddings
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError(
                f"{provider.capitalize()} doesn't provide embedding models. "
                "Set OPENAI_API_KEY for embeddings, or disable embeddings with ENABLE_EMBEDDINGS=false"
            )
        model = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")
        return OpenAIEmbeddingFunctionWithTracking(api_key=api_key, model_name=model, repo_name=repo_name)
    else:
        raise ValueError(f"Unknown LLM provider: {provider}. Supported: openai, ollama, gemini, deepseek, anthropic")


def init_chroma(repo_name: str, docs_base_dir: str = ".docs") -> Optional[chromadb.Collection]:
    """
    Initialize ChromaDB with persistent storage for a repository.
    Uses provider-specific subfolders (openai/ollama) based on LLM_PROVIDER.
    
    Args:
        repo_name: Name of the repository
        docs_base_dir: Base directory for docs (default: .docs)
        
    Returns:
        ChromaDB collection for functions, or None if embeddings are disabled
    """
    if not ENABLE_EMBEDDINGS:
        return None
    
    # Get provider name for subfolder organization
    provider = os.getenv("LLM_PROVIDER", "openai").lower()
    if provider not in ["openai", "ollama", "gemini"]:
        provider = "ollama"  # Default fallback

    # Create provider-specific subfolder path
    chroma_path = Path(docs_base_dir) / repo_name / "chromadb" / provider
    chroma_path.mkdir(parents=True, exist_ok=True)
    
    client = chromadb.PersistentClient(path=str(chroma_path))
    embedding_fn = get_embedding_function(repo_name=repo_name)

    collection = client.get_or_create_collection(
        name="functions",
        embedding_function=embedding_fn,
        metadata={"hnsw:space": "cosine"}
    )
    
    return collection


def embed_functions(extracted_code_elements: list[dict], collection: Optional[chromadb.Collection], batch_size: int = 1) -> int:
    """
    Embed all functions from node extraction results into ChromaDB.
    
    Args:
        extracted_code_elements: List of file dicts from 2_node_extraction.yaml
        collection: ChromaDB collection to store embeddings (None if embeddings disabled)
        batch_size: Number of functions to embed per batch (default: 1 - strictly sequential for stability)
        
    Returns:
        Number of functions embedded
    """
    if collection is None:
        return 0
    import time

    provider = os.getenv("LLM_PROVIDER", "openai").lower()
    # If caller didn't choose batching, allow larger default for OpenAI/Gemini (robust, fewer requests).
    if batch_size == 1 and provider in ["openai", "gemini"]:
        batch_size = 32

    def embed_batch(docs, doc_ids, metas, is_retry=False):
        max_retries = 3 if provider == "ollama" else 2
        for attempt in range(max_retries):
            try:
                # Add delay before request to let Ollama recover (longer delay on retries)
                if provider == "ollama":
                    delay = 1.0 if attempt > 0 else 0.5
                    time.sleep(delay)
                
                collection.add(
                    documents=docs,
                    ids=doc_ids,
                    metadatas=metas
                )
                return True
            except Exception as e:
                error_msg = str(e)
                is_server_error = "500" in error_msg or "Internal Server Error" in error_msg
                
                if attempt == max_retries - 1:
                    # Final attempt failed
                    if len(doc_ids) == 1:
                        logger.error(f"Failed after {max_retries} attempts: {doc_ids[0]}")
                        logger.error(f"Length: {len(docs[0])} chars, Error: {error_msg}")
                        return False
                    else:
                        # For multi-item batches that fail, try embedding individually
                        if not is_retry:
                            logger.warning(f"Batch failed, retrying {len(doc_ids)} items individually...")
                            success_count = 0
                            for doc, doc_id, meta in zip(docs, doc_ids, metas):
                                if embed_batch([doc], [doc_id], [meta], is_retry=True):
                                    success_count += 1
                            if success_count > 0:
                                logger.info(f"Successfully embedded {success_count}/{len(doc_ids)} items")
                            return success_count > 0
                        logger.error(f"Batch failed after {max_retries} attempts: {error_msg}")
                        return False
                
                # Retry with exponential backoff for server errors
                sleep_time = (attempt + 1) * 2 if is_server_error else (attempt + 1)
                logger.warning(f"Error embedding batch (attempt {attempt + 1}/{max_retries}). Retrying in {sleep_time}s...")
                time.sleep(sleep_time)
        return False

    # First pass: count functions that need embedding
    functions_to_embed = []
    for extracted_element in extracted_code_elements:
        file_name = extracted_element["file_name"]
        for func in extracted_element.get("functions", []):
            node_id = func["node_id"]
            code = func.get("code", "")
            
            if not code or not code.strip():
                continue
            
            # Skip if already embedded
            existing = collection.get(ids=[node_id])
            if existing["ids"]:
                continue
            
            functions_to_embed.append({
                "node_id": node_id,
                "code": code,
                "file_name": file_name,
                "name": func["name"],
                "start_line": func["start_line"],
                "end_line": func["end_line"]
            })
    
    total_to_embed = len(functions_to_embed)
    if total_to_embed == 0:
        return 0
    
    logger.info(f"Embedding {total_to_embed} functions")

    # Second pass: embed functions with progress tracking
    documents = []
    ids = []
    metadatas = []
    total_embedded = 0
    current_index = 0

    for func_data in functions_to_embed:
        node_id = func_data["node_id"]
        code = func_data["code"]
        file_name = func_data["file_name"]
        
        # Truncate code to prevent Ollama crashes on large inputs
        # Conservative truncation for Ollama: code has ~3-4 chars per token
        # For num_ctx=8192, safe limit is ~6000 chars (70% of 8192 tokens * 3 chars/token)
        # OpenAI can handle larger inputs, so only truncate if needed
        max_chars = 6000 if provider == "ollama" else 16000
        if len(code) > max_chars:
            code = code[:max_chars]
            if provider == "ollama":
                # Add note that code was truncated
                code += "\n\n[... code truncated for embedding ...]"
                
        documents.append(code)
        ids.append(node_id)
        metadatas.append({
            "node_id": node_id,
            "name": func_data["name"],
            "file": file_name,
            "start_line": func_data["start_line"],
            "end_line": func_data["end_line"]
        })
        current_index += 1
        
        if len(documents) >= batch_size:
            # Print progress with 1/x format
            if batch_size == 1:
                logger.debug(f"[{current_index}/{total_to_embed}] {ids[0]} ({len(documents[0])} chars)")
            
            if embed_batch(documents, ids, metadatas):
                total_embedded += len(documents)
            else:
                logger.warning(f"Skipping {ids[0]} due to repeated errors")
            
            documents = []
            ids = []
            metadatas = []
    
    # Add any remaining functions
    if documents:
        if batch_size == 1:
            logger.debug(f"[{current_index}/{total_to_embed}] {ids[0]} ({len(documents[0])} chars)")
        if embed_batch(documents, ids, metadatas):
            total_embedded += len(documents)
        else:
            logger.warning(f"Skipping final batch of {len(documents)} functions")
    
    return total_embedded


def get_similar(
    node_id: str,
    collection: Optional[chromadb.Collection],
    k: int = 3,
    max_distance: float | None = None
) -> list[dict]:
    """
    Find similar functions to a given function.
    
    Args:
        node_id: The node_id of the function to find similar ones for
        collection: ChromaDB collection (None if embeddings disabled)
        k: Number of similar functions to return
        max_distance: Maximum distance threshold (lower = more similar). 
                      For cosine distance, typically 0.0-1.0. If None, no filtering.
        
    Returns:
        List of dicts with node_id, file, name, code, and similarity score
    """
    if collection is None:
        return []
    # Get the function's embedding
    result = collection.get(ids=[node_id], include=["embeddings", "documents"])
    
    if result["embeddings"].size == 0:
        return []
    
    # Query for similar (k+1 because the function itself will be included)
    query_result = collection.query(
        query_embeddings=result["embeddings"],
        n_results=k + 1,
        include=["documents", "metadatas", "distances"]
    )
    
    similar = []
    # query_result["ids"] is a list of lists, one per query
    ids_list = query_result["ids"][0] if query_result["ids"] else []
    metadatas_list = query_result["metadatas"][0] if query_result["metadatas"] else []
    documents_list = query_result["documents"][0] if query_result["documents"] else []
    distances_list = query_result["distances"][0] if query_result.get("distances") else []
    
    for i, doc_id in enumerate(ids_list):
        # Skip the function itself - ensure both are strings for comparison
        if str(doc_id) == str(node_id):
            continue
        
        distance = distances_list[i] if distances_list and i < len(distances_list) else None
        
        # Filter by distance threshold if specified
        if max_distance is not None and distance is not None and distance > max_distance:
            continue
        
        similar.append({
            "node_id": str(doc_id),
            "file": metadatas_list[i].get("file", "unknown") if metadatas_list else "unknown",
            "name": metadatas_list[i].get("name", "unknown") if metadatas_list else "unknown",
            "code": documents_list[i] if documents_list else "",
            "distance": distance
        })
    
    return similar[:k]


def get_similar_by_text(
    query_text: str,
    collection: Optional[chromadb.Collection],
    k: int = 3,
    max_distance: float | None = None
) -> list[dict]:
    """
    Find similar functions by querying with text (function name, code snippet, or description).
    
    Args:
        query_text: Text to search for (e.g., function name, code snippet, description)
        collection: ChromaDB collection (None if embeddings disabled)
        k: Number of similar functions to return
        max_distance: Maximum distance threshold (lower = more similar). 
                      For cosine distance, typically 0.0-1.0. If None, no filtering.
        
    Returns:
        List of dicts with node_id, file, name, code, and similarity score
    """
    if collection is None:
        return []
    # Query by text - ChromaDB will automatically embed the text
    query_result = collection.query(
        query_texts=[query_text],
        n_results=k,
        include=["documents", "metadatas", "distances"]
    )
    
    similar = []
    # query_result["ids"] is a list of lists, one per query
    ids_list = query_result["ids"][0] if query_result["ids"] else []
    metadatas_list = query_result["metadatas"][0] if query_result["metadatas"] else []
    documents_list = query_result["documents"][0] if query_result["documents"] else []
    distances_list = query_result["distances"][0] if query_result.get("distances") else []
    
    for i, doc_id in enumerate(ids_list):
        distance = distances_list[i] if distances_list and i < len(distances_list) else None
        
        # Filter by distance threshold if specified
        if max_distance is not None and distance is not None and distance > max_distance:
            continue
        
        similar.append({
            "node_id": str(doc_id),
            "file": metadatas_list[i].get("file", "unknown") if metadatas_list else "unknown",
            "name": metadatas_list[i].get("name", "unknown") if metadatas_list else "unknown",
            "code": documents_list[i] if documents_list else "",
            "distance": distance
        })
    
    return similar


def get_function_embedding(node_id: str, collection: Optional[chromadb.Collection]) -> list[float] | None:
    """
    Get the embedding vector for a specific function.
    
    Args:
        node_id: The node_id of the function
        collection: ChromaDB collection (None if embeddings disabled)
        
    Returns:
        Embedding vector or None if not found
    """
    if collection is None:
        return None
    result = collection.get(ids=[node_id], include=["embeddings"])
    if result["embeddings"]:
        return result["embeddings"][0]
    return None
