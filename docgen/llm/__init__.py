"""LLM integration package for DocGen."""

from docgen.llm.client import call_llm
from docgen.llm.structured_client import call_llm_structured
from docgen.llm.schemas import RepoAnalysis, RepoSummary, Module, TechStack
from docgen.llm.prompts import generate_initial_analysis, get_synthesis_doc_prompt
from docgen.llm.embeddings import init_chroma, embed_functions, get_similar, get_similar_by_text

__all__ = [
    "call_llm",
    "call_llm_structured",
    "RepoAnalysis",
    "RepoSummary",
    "Module",
    "TechStack",
    "generate_initial_analysis",
    "get_synthesis_doc_prompt",
    "init_chroma",
    "embed_functions",
    "get_similar",
    "get_similar_by_text",
]

