"""Langfuse integration for LLM observability and tracking.

SDK v3 approach:
- Each LLM/embedding call creates its own trace
- Traces are grouped by session_id (repo_name)
- Each trace has a meaningful name
"""

import os
import re
import logging
from typing import Optional, Dict, Any

logger = logging.getLogger("docgen")

# Global Langfuse client instance
_langfuse_client = None
_langfuse_enabled = False
_pending_tracked_calls = 0


def _flush_every_n() -> int:
    """How often we flush Langfuse events. Defaults to 10."""
    try:
        return int(os.getenv("LANGFUSE_FLUSH_EVERY", "10"))
    except Exception:
        return 10


def _redact_text(text: str) -> str:
    """Very simple redaction for secrets before sending to Langfuse."""
    if not text:
        return text

    # Common "KEY=VALUE" patterns
    text = re.sub(r"(?im)^(OPENAI_API_KEY\s*=\s*).+$", r"\1[REDACTED]", text)
    text = re.sub(r"(?im)^(LANGFUSE_PUBLIC_KEY\s*=\s*).+$", r"\1[REDACTED]", text)
    text = re.sub(r"(?im)^(LANGFUSE_SECRET_KEY\s*=\s*).+$", r"\1[REDACTED]", text)

    # Common token-like patterns
    text = re.sub(r"\bsk-[A-Za-z0-9]{10,}\b", "sk-[REDACTED]", text)
    text = re.sub(r"\bpk-lf-[A-Za-z0-9\-_]{10,}\b", "pk-lf-[REDACTED]", text)
    text = re.sub(r"\bsk-lf-[A-Za-z0-9\-_]{10,}\b", "sk-lf-[REDACTED]", text)

    return text


def _maybe_flush(client) -> None:
    """Flush Langfuse events every N tracked calls."""
    global _pending_tracked_calls
    n = _flush_every_n()
    if n <= 0:
        return
    if _pending_tracked_calls >= n:
        try:
            client.flush()
        finally:
            _pending_tracked_calls = 0


def _init_langfuse():
    """Initialize Langfuse client using SDK v3 API."""
    global _langfuse_client, _langfuse_enabled
    
    if _langfuse_client is not None:
        return _langfuse_client
    
    public_key = os.getenv("LANGFUSE_PUBLIC_KEY")
    secret_key = os.getenv("LANGFUSE_SECRET_KEY")
    
    if not public_key or not secret_key:
        _langfuse_enabled = False
        return None
    
    try:
        from langfuse import get_client
        
        host = os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com")
        os.environ.setdefault("LANGFUSE_HOST", host)
        
        logger.info(f"Initializing Langfuse client (host: {host})...")
        
        _langfuse_client = get_client()
        _langfuse_enabled = True
        logger.info("Langfuse client initialized successfully")
        return _langfuse_client
    except ImportError:
        logger.warning("langfuse package not installed. Install with: pip install langfuse")
        _langfuse_enabled = False
        return None
    except Exception as e:
        logger.warning(f"Failed to initialize Langfuse: {e}")
        _langfuse_enabled = False
        return None


def is_langfuse_enabled() -> bool:
    """Check if Langfuse is enabled and configured."""
    if _langfuse_client is None:
        _init_langfuse()
    return _langfuse_enabled


def get_langfuse_client():
    """Get the Langfuse client instance, initializing if necessary."""
    if _langfuse_client is None:
        _init_langfuse()
    return _langfuse_client


def flush_and_end():
    """Flush all data. Call at end of CLI run."""
    client = get_langfuse_client()
    
    if client:
        try:
            client.flush()
        except Exception:
            pass


def track_llm_generation(
    prompt: str,
    response: str,
    model: str,
    provider: str,
    metadata: Optional[Dict[str, Any]] = None,
    token_usage: Optional[Dict[str, int]] = None,
    generation_name: Optional[str] = None
) -> None:
    """Track an LLM generation call in Langfuse (SDK v3).
    
    Creates a separate trace for each call, grouped by session_id (repo_name).
    """
    client = get_langfuse_client()
    if not client:
        return
    
    try:
        # Get repo_name from metadata for session_id grouping
        repo_name = metadata.get("repo_name") if metadata else None
        
        # Prepare metadata
        gen_metadata = {
            "provider": provider,
            "model": model,
            "type": "generation",
        }
        if metadata:
            gen_metadata.update(metadata)
        
        # Prepare usage
        usage_details = None
        if token_usage:
            usage_details = {
                "input_tokens": token_usage.get("prompt_tokens", 0),
                "output_tokens": token_usage.get("completion_tokens", 0),
                "total_tokens": token_usage.get("total_tokens", 0),
            }
        
        # Redact before sending
        prompt = _redact_text(prompt)
        response = _redact_text(response)

        # Determine trace name
        trace_name = generation_name or "llm_call"
        if repo_name and not generation_name:
            trace_name = f"llm_call-{repo_name}"
        
        # Create a new trace for this generation
        # Use start_as_current_observation with as_type="generation" to create a trace
        with client.start_as_current_observation(
            as_type="generation",
            name=trace_name,
            model=model,
            input=prompt,
            output=response,
            metadata=gen_metadata
        ) as generation:
            # Set usage details if available
            if usage_details:
                generation.update(usage_details=usage_details)
            
            # Set trace-level attributes: name and session_id for grouping
            if repo_name:
                generation.update_trace(
                    name=trace_name,
                    session_id=repo_name
                )
            else:
                generation.update_trace(name=trace_name)
        
        # Batch flush
        global _pending_tracked_calls
        _pending_tracked_calls += 1
        _maybe_flush(client)
        
    except Exception as e:
        logger.warning(f"Langfuse LLM tracking failed: {e}")


def track_embedding_generation(
    input_texts: list[str],
    embeddings: list[list[float]],
    model: str,
    provider: str,
    metadata: Optional[Dict[str, Any]] = None,
    token_usage: Optional[Dict[str, int]] = None,
    generation_name: Optional[str] = None
) -> None:
    """Track an embedding generation call in Langfuse (SDK v3).
    
    Creates a separate trace for each call, grouped by session_id (repo_name).
    """
    client = get_langfuse_client()
    if not client:
        return
    
    try:
        # Get repo_name from metadata for session_id grouping
        repo_name = metadata.get("repo_name") if metadata else None
        
        # Prepare metadata
        gen_metadata = {
            "provider": provider,
            "model": model,
            "type": "embedding",
            "input_count": len(input_texts),
            "embedding_dimension": len(embeddings[0]) if embeddings else 0,
        }
        if metadata:
            gen_metadata.update(metadata)
        
        # Summarize input (first 500 chars of first 5 texts)
        input_summary = "\n".join([
            text[:500] + ("..." if len(text) > 500 else "")
            for text in input_texts[:5]
        ])
        if len(input_texts) > 5:
            input_summary += f"\n... and {len(input_texts) - 5} more texts"
        input_summary = _redact_text(input_summary)
        
        # Prepare usage
        usage_details = None
        if token_usage:
            tokens = token_usage.get("tokens") or token_usage.get("prompt_tokens", 0)
            usage_details = {"input_tokens": tokens, "total_tokens": tokens}
        
        # Determine trace name
        trace_name = generation_name or "embedding_call"
        if repo_name and not generation_name:
            trace_name = f"embedding_call-{repo_name}"
        
        output_msg = f"Generated {len(embeddings)} embeddings of dimension {len(embeddings[0]) if embeddings else 0}"
        
        # Create a new trace for this embedding generation
        # Use start_as_current_observation with as_type="span" for embeddings
        with client.start_as_current_observation(
            as_type="span",
            name=trace_name,
            input=input_summary,
            output=output_msg,
            metadata=gen_metadata
        ) as span:
            # Set usage details if available
            if usage_details:
                span.update(usage_details=usage_details)
            
            # Set trace-level attributes: name and session_id for grouping
            if repo_name:
                span.update_trace(
                    name=trace_name,
                    session_id=repo_name
                )
            else:
                span.update_trace(name=trace_name)
        
        # Batch flush
        global _pending_tracked_calls
        _pending_tracked_calls += 1
        _maybe_flush(client)
        
    except Exception as e:
        logger.warning(f"Langfuse embedding tracking failed: {e}")
