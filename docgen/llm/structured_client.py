"""Structured LLM client using LangChain's with_structured_output()."""

import os
import time
import logging
from typing import TypeVar

from pydantic import BaseModel

from docgen.utils.config import DEBUG
from docgen.llm.langfuse_client import track_llm_generation
from docgen.llm.client import _token_usage

logger = logging.getLogger("docgen")

T = TypeVar("T", bound=BaseModel)

# Retry configuration
MAX_RETRIES = 3
RETRY_DELAY_BASE = 2  # seconds, exponential backoff


def _get_max_tokens() -> int | None:
    """Get max tokens from environment, or None to use model default."""
    max_tokens_str = os.getenv("LLM_MAX_TOKENS")
    if max_tokens_str:
        try:
            return int(max_tokens_str)
        except ValueError:
            logger.warning(f"Invalid LLM_MAX_TOKENS value: {max_tokens_str}, using model default")
    return None


def _get_llm(provider: str, model: str):
    """Get LangChain chat model for the specified provider."""
    max_tokens = _get_max_tokens()

    match provider:
        case "openai":
            from langchain_openai import ChatOpenAI
            return ChatOpenAI(model=model, api_key=os.getenv("OPENAI_API_KEY"), max_tokens=max_tokens)
        case "anthropic":
            from langchain_anthropic import ChatAnthropic
            return ChatAnthropic(model=model, api_key=os.getenv("ANTHROPIC_API_KEY"), max_tokens=max_tokens)
        case "deepseek":
            from langchain_openai import ChatOpenAI
            base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
            return ChatOpenAI(model=model, api_key=os.getenv("DEEPSEEK_API_KEY"), base_url=base_url, max_tokens=max_tokens)
        case "ollama":
            from langchain_ollama import ChatOllama
            base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
            # ChatOllama uses num_predict instead of max_tokens
            return ChatOllama(model=model, base_url=base_url, num_predict=max_tokens)
        case "gemini":
            api_key = os.getenv("GOOGLE_API_KEY")
            project_id = os.getenv("GOOGLE_PROJECT_ID")

            if api_key:
                from langchain_google_genai import ChatGoogleGenerativeAI
                return ChatGoogleGenerativeAI(
                    model=model,
                    api_key=api_key,
                    temperature=0,
                    max_output_tokens=max_tokens
                )
            elif project_id:
                from langchain_google_vertexai import ChatVertexAI
                location = os.getenv("GOOGLE_LOCATION", "us-central1")
                return ChatVertexAI(
                    model=model,
                    project=project_id,
                    location=location,
                    temperature=0,
                    max_output_tokens=max_tokens
                )
            else:
                raise ValueError("Either GOOGLE_API_KEY or GOOGLE_PROJECT_ID must be set for Gemini provider")
        case _:
            raise ValueError(f"Unknown provider: {provider}. Supported: openai, anthropic, ollama, gemini, deepseek")


def call_llm_structured(
    prompt: str,
    schema: type[T],
    *,
    generation_name: str | None = None,
    metadata: dict | None = None,
) -> T:
    """Call LLM with structured output, returning a validated Pydantic model.
    
    Uses LangChain's with_structured_output() which handles provider differences:
    - OpenAI: response_format with JSON schema
    - Anthropic: tool calling
    - Ollama: tool calling (requires compatible model like llama3.1+)
    
    Args:
        prompt: The prompt to send
        schema: Pydantic model class defining the expected output
        generation_name: Optional name for Langfuse tracking
        metadata: Optional metadata dict for Langfuse tracking
        
    Returns:
        Parsed and validated Pydantic model instance
        
    Raises:
        ValueError: If provider is unknown or not configured
        ValidationError: If LLM output doesn't match schema
    """
    provider = os.getenv("LLM_PROVIDER", "openai").lower()
    model = _get_model_for_provider(provider)
    
    if DEBUG:
        logger.debug(f"STRUCTURED LLM CALL ({provider}/{model})\nSchema: {schema.__name__}\n" + "="*80 + "\n" + prompt + "\n" + "="*80)
    
    llm = _get_llm(provider, model)
    # DeepSeek doesn't support JSON schema response_format, use function calling instead
    if provider == "deepseek":
        structured_llm = llm.with_structured_output(schema, include_raw=True, method="function_calling")
    else:
        structured_llm = llm.with_structured_output(schema, include_raw=True)

    # Retry loop for transient failures
    last_error = None
    for attempt in range(MAX_RETRIES):
        try:
            raw_result = structured_llm.invoke(prompt)
            result = raw_result.get("parsed")
            raw_msg = raw_result.get("raw")
            parsing_error = raw_result.get("parsing_error")

            # Extract token usage from AIMessage
            token_usage = None
            if raw_msg:
                usage = getattr(raw_msg, "usage_metadata", None)
                if usage:
                    token_usage = {
                        "prompt_tokens": usage.get("input_tokens", 0),
                        "completion_tokens": usage.get("output_tokens", 0),
                        "total_tokens": usage.get("total_tokens", 0),
                    }
                    _token_usage["llm"]["prompt_tokens"] += token_usage["prompt_tokens"]
                    _token_usage["llm"]["completion_tokens"] += token_usage["completion_tokens"]
                    _token_usage["llm"]["total_tokens"] += token_usage["total_tokens"]
                    _token_usage["llm"]["calls"] += 1

            # Handle parsing failure with detailed error info
            if result is None:
                raw_content = ""
                if raw_msg:
                    # Try to get content from message content first
                    raw_content = getattr(raw_msg, "content", "")
                    # For tool-calling providers, content may be in tool_calls
                    if not raw_content:
                        tool_calls = getattr(raw_msg, "tool_calls", [])
                        if tool_calls:
                            raw_content = str(tool_calls[0].get("args", {}))[:1000]
                        else:
                            # Try additional_kwargs for some providers
                            additional = getattr(raw_msg, "additional_kwargs", {})
                            if additional:
                                raw_content = str(additional)[:1000]
                    if not raw_content:
                        raw_content = str(raw_msg)

                error_detail = ""
                if parsing_error:
                    error_detail = f" Parsing error: {parsing_error}"

                # Check for common failure patterns
                if raw_content and len(raw_content) > 10000:
                    error_detail += " (Response may have been truncated due to length)"

                last_error = ValueError(
                    f"LLM failed to parse response into {schema.__name__} schema.{error_detail} "
                    f"Raw response preview: {str(raw_content)[:500]}..."
                )

                # Retry on parsing failure
                if attempt < MAX_RETRIES - 1:
                    delay = RETRY_DELAY_BASE ** attempt
                    logger.warning(f"Parsing failed (attempt {attempt + 1}/{MAX_RETRIES}), retrying in {delay}s...")
                    time.sleep(delay)
                    continue
                else:
                    raise last_error

            # Success - break out of retry loop
            break

        except ValueError:
            raise  # Re-raise our own ValueError
        except Exception as e:
            last_error = e
            if attempt < MAX_RETRIES - 1:
                delay = RETRY_DELAY_BASE ** attempt
                logger.warning(f"LLM call failed (attempt {attempt + 1}/{MAX_RETRIES}): {e}, retrying in {delay}s...")
                time.sleep(delay)
            else:
                raise ValueError(f"LLM call failed after {MAX_RETRIES} attempts: {last_error}")

    if DEBUG:
        logger.debug("STRUCTURED LLM RESPONSE:\n" + "="*80 + "\n" + result.model_dump_json(indent=2) + "\n" + "="*80)

    # Track in Langfuse
    if generation_name:
        track_llm_generation(
            prompt=prompt,
            response=result.model_dump_json(),
            model=model,
            provider=provider,
            metadata=metadata,
            token_usage=token_usage,
            generation_name=generation_name,
        )

    return result


def _get_model_for_provider(provider: str) -> str:
    """Get the model name for the given provider from environment."""
    match provider:
        case "openai":
            return os.getenv("OPENAI_MODEL", "gpt-4o")
        case "anthropic":
            return os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-20250514")
        case "deepseek":
            return os.getenv("DEEPSEEK_MODEL", "deepseek-chat")
        case "ollama":
            model = os.getenv("OLLAMA_MODEL")
            if not model:
                raise ValueError("OLLAMA_MODEL environment variable must be set")
            return model
        case "gemini":
            return os.getenv("GOOGLE_MODEL", "gemini-3-flash")
        case _:
            raise ValueError(f"Unknown provider: {provider}")
