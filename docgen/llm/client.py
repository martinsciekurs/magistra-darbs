"""LLM client for calling Ollama, OpenAI, and Google Gemini APIs."""

import os
import logging
from docgen.utils.config import DEBUG
from docgen.llm.langfuse_client import track_llm_generation

logger = logging.getLogger("docgen")

# Global token usage tracking
_token_usage = {
    "llm": {
        "prompt_tokens": 0,
        "completion_tokens": 0,
        "total_tokens": 0,
        "calls": 0
    },
    "embeddings": {
        "tokens": 0,
        "calls": 0
    }
}


def get_token_usage():
    """Get accumulated token usage statistics.
    
    Returns:
        dict with keys: llm (dict with prompt_tokens, completion_tokens, total_tokens, calls),
                        embeddings (dict with tokens, calls)
    """
    return {
        "llm": _token_usage["llm"].copy(),
        "embeddings": _token_usage["embeddings"].copy()
    }


def reset_token_usage():
    """Reset token usage statistics."""
    global _token_usage
    _token_usage = {
        "llm": {
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "total_tokens": 0,
            "calls": 0
        },
        "embeddings": {
            "tokens": 0,
            "calls": 0
        }
    }


def track_embedding_tokens(prompt_tokens: int, total_tokens: int | None = None):
    """Track token usage for embedding API calls.
    
    Args:
        prompt_tokens: Number of tokens in the input text
        total_tokens: Total tokens used (defaults to prompt_tokens if None)
    """
    global _token_usage
    tokens_to_track = total_tokens if total_tokens is not None else prompt_tokens
    _token_usage["embeddings"]["tokens"] += tokens_to_track
    _token_usage["embeddings"]["calls"] += 1


def call_llm(prompt: str, generation_name: str = None, metadata: dict = None) -> str:
    """Call LLM API (OpenAI or Ollama) with the given prompt.
    
    Args:
        prompt: The prompt to send to the LLM
        generation_name: Optional name for Langfuse tracking
        metadata: Optional metadata dict for Langfuse tracking (include "phase" for grouping)
        
    Returns:
        The LLM's response text
    """
    if DEBUG:
        logger.debug("LLM PROMPT:\n" + "="*80 + "\n" + prompt + "\n" + "="*80)
    
    provider = os.getenv("LLM_PROVIDER", "openai").lower()
    
    if provider == "openai":
        response, token_usage, model = _call_openai(prompt)
    elif provider == "ollama":
        response, token_usage, model = _call_ollama(prompt)
    elif provider == "gemini":
        response, token_usage, model = _call_gemini(prompt)
    elif provider == "deepseek":
        response, token_usage, model = _call_deepseek(prompt)
    else:
        logger.error(f"Unknown LLM provider: {provider}. Supported providers: openai, ollama, gemini, deepseek")
        response = ""
        token_usage = None
        model = None
    
    if DEBUG:
        logger.debug("LLM RESPONSE:\n" + "="*80 + "\n" + response + "\n" + "="*80)
    
    # Track in Langfuse if enabled
    if response and model:
        track_llm_generation(
            prompt=prompt,
            response=response,
            model=model,
            provider=provider,
            metadata=metadata,
            token_usage=token_usage,
            generation_name=generation_name
        )
    
    return response


def _call_openai(prompt: str) -> tuple[str, dict | None, str | None]:
    """Call OpenAI API with the given prompt.
    
    Args:
        prompt: The prompt to send to OpenAI
        
    Returns:
        Tuple of (response_text, token_usage_dict, model_name)
        token_usage_dict contains: prompt_tokens, completion_tokens, total_tokens
    """
    try:
        from openai import OpenAI
    except ImportError:
        logger.error("openai package not installed. Install it with: pip install openai")
        return "", None, None
    
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        logger.error("OPENAI_API_KEY environment variable not set")
        return "", None, None
    
    model = os.getenv("OPENAI_MODEL", "gpt-5-nano")
    
    client = OpenAI(api_key=api_key)
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            timeout=300.0
        )
        
        # Track token usage
        token_usage = None
        if hasattr(response, 'usage') and response.usage:
            global _token_usage
            prompt_tokens = response.usage.prompt_tokens or 0
            completion_tokens = response.usage.completion_tokens or 0
            total_tokens = response.usage.total_tokens or 0
            
            _token_usage["llm"]["prompt_tokens"] += prompt_tokens
            _token_usage["llm"]["completion_tokens"] += completion_tokens
            _token_usage["llm"]["total_tokens"] += total_tokens
            _token_usage["llm"]["calls"] += 1
            
            token_usage = {
                "prompt_tokens": prompt_tokens,
                "completion_tokens": completion_tokens,
                "total_tokens": total_tokens
            }
        
        return response.choices[0].message.content or "", token_usage, model
    except Exception as e:
        logger.error(f"Error calling OpenAI: {e}")
        return "", None, None


def _call_ollama(prompt: str) -> tuple[str, dict | None, str | None]:
    """Call Ollama API with the given prompt.
    
    Args:
        prompt: The prompt to send to Ollama
        
    Returns:
        Tuple of (response_text, token_usage_dict, model_name)
        token_usage_dict contains: prompt_tokens, completion_tokens, total_tokens (if available)
    """
    import requests
    
    base_url = os.getenv("OLLAMA_BASE_URL")
    model = os.getenv("OLLAMA_MODEL")
    
    if not base_url or not model:
        logger.error("OLLAMA_BASE_URL and OLLAMA_MODEL environment variables must be set")
        return "", None, None
    
    url = f"{base_url}/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "temperature": 0
    }
    
    try:
        response = requests.post(url, json=payload, timeout=300)
        response.raise_for_status()
        result = response.json()
        
        response_text = result.get("response", "")
        
        # Extract token usage if available from Ollama response
        token_usage = None
        prompt_eval_count = result.get("prompt_eval_count")
        eval_count = result.get("eval_count")
        
        if prompt_eval_count is not None:
            # Ollama provides prompt_eval_count and eval_count
            total_tokens = (prompt_eval_count or 0) + (eval_count or 0)
            token_usage = {
                "prompt_tokens": prompt_eval_count or 0,
                "completion_tokens": eval_count or 0,
                "total_tokens": total_tokens
            }
            
            # Track in global usage
            global _token_usage
            _token_usage["llm"]["prompt_tokens"] += prompt_eval_count or 0
            _token_usage["llm"]["completion_tokens"] += eval_count or 0
            _token_usage["llm"]["total_tokens"] += total_tokens
            _token_usage["llm"]["calls"] += 1
        
        return response_text, token_usage, model
    except requests.exceptions.RequestException as e:
        logger.error(f"Error calling Ollama: {e}")
        return "", None, None


def _call_gemini(prompt: str) -> tuple[str, dict | None, str | None]:
    """Call Google Gemini API with the given prompt.

    Supports two authentication methods:
    - API Key: Set GOOGLE_API_KEY environment variable
    - Vertex AI (ADC): Set GOOGLE_PROJECT_ID (uses gcloud CLI credentials)

    Args:
        prompt: The prompt to send to Gemini

    Returns:
        Tuple of (response_text, token_usage_dict, model_name)
        token_usage_dict contains: prompt_tokens, completion_tokens, total_tokens
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    project_id = os.getenv("GOOGLE_PROJECT_ID")

    if api_key:
        return _call_gemini_api_key(prompt, api_key)
    elif project_id:
        return _call_gemini_vertex(prompt, project_id)
    else:
        logger.error("Either GOOGLE_API_KEY or GOOGLE_PROJECT_ID must be set for Gemini provider")
        return "", None, None


def _call_gemini_api_key(prompt: str, api_key: str) -> tuple[str, dict | None, str | None]:
    """Call Gemini using API key authentication."""
    try:
        import google.generativeai as genai
    except ImportError:
        logger.error("google-generativeai package not installed. Install it with: pip install google-generativeai")
        return "", None, None

    model_name = os.getenv("GOOGLE_MODEL", "gemini-2.0-flash")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name)

    try:
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(temperature=0),
            request_options={"timeout": 300}
        )

        response_text = response.text if response.text else ""

        # Track token usage
        token_usage = None
        if hasattr(response, 'usage_metadata') and response.usage_metadata:
            global _token_usage
            prompt_tokens = response.usage_metadata.prompt_token_count or 0
            completion_tokens = response.usage_metadata.candidates_token_count or 0
            total_tokens = response.usage_metadata.total_token_count or 0

            _token_usage["llm"]["prompt_tokens"] += prompt_tokens
            _token_usage["llm"]["completion_tokens"] += completion_tokens
            _token_usage["llm"]["total_tokens"] += total_tokens
            _token_usage["llm"]["calls"] += 1

            token_usage = {
                "prompt_tokens": prompt_tokens,
                "completion_tokens": completion_tokens,
                "total_tokens": total_tokens
            }

        return response_text, token_usage, model_name
    except Exception as e:
        logger.error(f"Error calling Gemini: {e}")
        return "", None, None


def _call_gemini_vertex(prompt: str, project_id: str) -> tuple[str, dict | None, str | None]:
    """Call Gemini using Vertex AI with Application Default Credentials (gcloud CLI)."""
    try:
        import vertexai
        from vertexai.generative_models import GenerativeModel, GenerationConfig
    except ImportError:
        logger.error("google-cloud-aiplatform package not installed. Install it with: pip install google-cloud-aiplatform")
        return "", None, None

    model_name = os.getenv("GOOGLE_MODEL", "gemini-3-flash")
    location = os.getenv("GOOGLE_LOCATION", "us-central1")

    vertexai.init(project=project_id, location=location)
    model = GenerativeModel(model_name)

    try:
        response = model.generate_content(
            prompt,
            generation_config=GenerationConfig(temperature=0),
        )

        response_text = response.text if response.text else ""

        # Track token usage
        token_usage = None
        if hasattr(response, 'usage_metadata') and response.usage_metadata:
            global _token_usage
            prompt_tokens = response.usage_metadata.prompt_token_count or 0
            completion_tokens = response.usage_metadata.candidates_token_count or 0
            total_tokens = response.usage_metadata.total_token_count or 0

            _token_usage["llm"]["prompt_tokens"] += prompt_tokens
            _token_usage["llm"]["completion_tokens"] += completion_tokens
            _token_usage["llm"]["total_tokens"] += total_tokens
            _token_usage["llm"]["calls"] += 1

            token_usage = {
                "prompt_tokens": prompt_tokens,
                "completion_tokens": completion_tokens,
                "total_tokens": total_tokens
            }

        return response_text, token_usage, model_name
    except Exception as e:
        logger.error(f"Error calling Gemini via Vertex AI: {e}")
        return "", None, None


def _call_deepseek(prompt: str) -> tuple[str, dict | None, str | None]:
    """Call DeepSeek API with the given prompt.

    DeepSeek provides an OpenAI-compatible API.

    Args:
        prompt: The prompt to send to DeepSeek

    Returns:
        Tuple of (response_text, token_usage_dict, model_name)
        token_usage_dict contains: prompt_tokens, completion_tokens, total_tokens
    """
    try:
        from openai import OpenAI
    except ImportError:
        logger.error("openai package not installed. Install it with: pip install openai")
        return "", None, None

    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        logger.error("DEEPSEEK_API_KEY environment variable not set")
        return "", None, None

    model = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")
    base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")

    client = OpenAI(api_key=api_key, base_url=base_url)

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            timeout=300.0
        )

        # Track token usage
        token_usage = None
        if hasattr(response, 'usage') and response.usage:
            global _token_usage
            prompt_tokens = response.usage.prompt_tokens or 0
            completion_tokens = response.usage.completion_tokens or 0
            total_tokens = response.usage.total_tokens or 0

            _token_usage["llm"]["prompt_tokens"] += prompt_tokens
            _token_usage["llm"]["completion_tokens"] += completion_tokens
            _token_usage["llm"]["total_tokens"] += total_tokens
            _token_usage["llm"]["calls"] += 1

            token_usage = {
                "prompt_tokens": prompt_tokens,
                "completion_tokens": completion_tokens,
                "total_tokens": total_tokens
            }

        return response.choices[0].message.content or "", token_usage, model
    except Exception as e:
        logger.error(f"Error calling DeepSeek: {e}")
        return "", None, None
