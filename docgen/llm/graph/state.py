"""State definitions for the DocGen LangGraph pipeline."""

from typing import TypedDict, Annotated
from operator import add


class DocGenState(TypedDict, total=False):
    """State that flows through the documentation generation graph."""
    # Input configuration (required)
    repo_path: str
    repo_name: str
    
    # Error tracking (accumulated across nodes)
    errors: Annotated[list[str], add]
    
    # Force mode: if True, skip all cache checks and regenerate everything
    force: bool
    
    # HITL (Human-In-The-Loop) fields
    confidence_score: int  # Confidence score 1-100 from repo analysis
    user_feedback: str  # Optional user feedback to improve repo analysis
    
    # Reflection loop tracking
    reflection_iteration: int  # Current iteration (1, 2, or 3)
    reflection_feedback: str  # Accumulated feedback from evaluations
    reflection_history: list[dict]  # History of iterations for transparency
    
    # TOC (Table of Contents) generation fields
    proposed_toc: list[dict]  # Proposed TOC sections from LLM
    confirmed_toc: list[dict]  # User-confirmed TOC sections
    toc_user_feedback: str  # User feedback for TOC refinement
    toc_confirmed: bool  # Whether TOC has been confirmed by user
