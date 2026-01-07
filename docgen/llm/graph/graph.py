"""Main DocGen graph definition using LangGraph."""

import sqlite3
from pathlib import Path
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.sqlite import SqliteSaver

from docgen.llm.graph.state import DocGenState
from docgen.llm.graph.nodes import (
    generate_repo_analysis_node,
    evaluate_repo_analysis_node,
    hitl_feedback_node,
    document_functions_node,
    group_classes_node,
    document_classes_node,
    group_files_node,
    document_files_node,
    group_modules_node,
    document_modules_node,
    generate_architecture_diagram_node,
    propose_toc_node,
    hitl_toc_node,
    synthesize_node,
)
from docgen.utils.config import REFLECTION_CONFIDENCE_THRESHOLD, MAX_REFLECTION_ITERATIONS, HITL_CONFIDENCE_THRESHOLD, ENABLE_TOC_HITL


def create_docgen_graph(checkpointer=None, repo_name=None):
    """Create the documentation generation graph with checkpointing.
    
    Args:
        checkpointer: Optional checkpointer for resume support. If None, creates SqliteSaver.
        repo_name: Repository name for default checkpoint path (required if checkpointer is None)
    
    Returns:
        Compiled LangGraph ready to invoke.
    """
    if checkpointer is None:
        if repo_name is None:
            raise ValueError("repo_name required when checkpointer is None")
        
        checkpoint_dir = Path(".docs") / repo_name / "checkpoints"
        checkpoint_dir.mkdir(parents=True, exist_ok=True)
        checkpoint_path = checkpoint_dir / "checkpoints.db"
        conn = sqlite3.connect(str(checkpoint_path), check_same_thread=False)
        checkpointer = SqliteSaver(conn)

    graph = StateGraph(DocGenState)
    
    # Add nodes
    graph.add_node("generate_repo_analysis", generate_repo_analysis_node)
    graph.add_node("evaluate_repo_analysis", evaluate_repo_analysis_node)
    graph.add_node("hitl_feedback", hitl_feedback_node)
    graph.add_node("document_functions", document_functions_node)
    graph.add_node("group_classes", group_classes_node)
    graph.add_node("doc_classes", document_classes_node)
    graph.add_node("group_files", group_files_node)
    graph.add_node("doc_files", document_files_node)
    graph.add_node("group_modules", group_modules_node)
    graph.add_node("doc_modules", document_modules_node)
    graph.add_node("gen_architecture", generate_architecture_diagram_node)
    graph.add_node("propose_toc", propose_toc_node)
    graph.add_node("hitl_toc", hitl_toc_node)
    graph.add_node("synthesize", synthesize_node)
    
    # Reflection loop router - decides whether to continue iterating, go to HITL, or proceed
    def reflection_router(state: DocGenState) -> str:
        """Route after evaluation based on iteration count and scores."""
        iteration = state.get("reflection_iteration", 1)
        confidence_score = state.get("confidence_score", 0)
        
        # First check: If below HITL threshold, always go to HITL (regardless of iteration count)
        if confidence_score < HITL_CONFIDENCE_THRESHOLD:
            return "hitl_feedback"
        
        # Second check: If acceptable (score >= reflection threshold), proceed to documentation
        # (This will only be reached if score >= HITL_CONFIDENCE_THRESHOLD)
        if confidence_score >= REFLECTION_CONFIDENCE_THRESHOLD:
            return "document_functions"
        
        # If max iterations reached, proceed (since we're above HITL threshold)
        if iteration >= MAX_REFLECTION_ITERATIONS:
            return "document_functions"
        
        # Otherwise, continue reflection loop
        return "generate_repo_analysis"
    
    # TOC router - decides whether to go to HITL TOC confirmation or directly to synthesis
    def toc_router(state: DocGenState) -> str:
        """Route after TOC proposal based on ENABLE_TOC_HITL config."""
        if ENABLE_TOC_HITL:
            return "hitl_toc"
        return "synthesize"
    
    # Flow with reflection loop
    graph.add_edge(START, "generate_repo_analysis")
    graph.add_edge("generate_repo_analysis", "evaluate_repo_analysis")
    graph.add_conditional_edges(
        "evaluate_repo_analysis",
        reflection_router,
        {
            "generate_repo_analysis": "generate_repo_analysis",  # Loop back for another iteration
            "hitl_feedback": "hitl_feedback",
            "document_functions": "document_functions"
        }
    )
    graph.add_edge("hitl_feedback", "document_functions")
    graph.add_edge("document_functions", "group_classes")
    graph.add_edge("group_classes", "doc_classes")
    graph.add_edge("doc_classes", "group_files")
    graph.add_edge("group_files", "doc_files")
    graph.add_edge("doc_files", "group_modules")
    graph.add_edge("group_modules", "doc_modules")
    graph.add_edge("doc_modules", "gen_architecture")
    graph.add_edge("gen_architecture", "propose_toc")
    
    # TOC confirmation flow
    graph.add_conditional_edges(
        "propose_toc",
        toc_router,
        {
            "hitl_toc": "hitl_toc",
            "synthesize": "synthesize"
        }
    )
    graph.add_edge("hitl_toc", "synthesize")
    graph.add_edge("synthesize", END)
    
    return graph.compile(checkpointer=checkpointer)
