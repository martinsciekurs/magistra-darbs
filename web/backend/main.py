"""DocGen Web API - FastAPI backend for the documentation generator."""

import os
import sys
import subprocess
from pathlib import Path
from typing import Any

import yaml
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Add project root to path so we can import config
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from docgen.utils.config import (
    DEBUG,
    LOG_LEVEL,
    ENABLE_EMBEDDINGS,
    ENABLE_CODE_EXAMPLES,
    ENABLE_TOC_HITL,
    HITL_CONFIDENCE_THRESHOLD,
    REFLECTION_CONFIDENCE_THRESHOLD,
    MAX_REFLECTION_ITERATIONS,
    CODE_EXAMPLE_MAX_RETRIES,
    MAX_FILE_TREE_CONTENT_CHARS,
    MAX_MD_FILE_CHARS,
    MAX_TOTAL_MD_CONTEXT_CHARS,
)

app = FastAPI(title="DocGen API", version="1.0.0")

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DOCS_DIR = PROJECT_ROOT / ".docs"

# In-memory task storage (in production, use Redis or a database)
tasks: dict[str, dict[str, Any]] = {}

# Store running processes so we can cancel them
running_processes: dict[str, subprocess.Popen] = {}


class AnalyzeRequest(BaseModel):
    repo_url: str


class RepoSummary(BaseModel):
    name: str
    file_count: int
    function_count: int
    class_count: int
    status: str  # "complete", "in_progress", "error"
    has_site: bool


class RepoDetail(BaseModel):
    name: str
    files: list[str]
    functions: list[dict[str, Any]]
    classes: list[dict[str, Any]]


class ConfigValue(BaseModel):
    name: str
    value: Any
    description: str


def load_yaml(path: Path) -> Any:
    """Load YAML file."""
    if not path.exists():
        return None
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_file_tree(path: Path) -> list[str]:
    """Load file tree (plain text, one file per line)."""
    if not path.exists():
        return []
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    # Split by newlines and filter empty lines
    return [line.strip() for line in content.strip().split("\n") if line.strip()]


def get_repo_status(repo_path: Path) -> str:
    """Determine the status of a repo's documentation."""
    # Check if there's an active task
    repo_name = repo_path.name
    if repo_name in tasks and tasks[repo_name].get("status") == "running":
        return "in_progress"
    
    # Check if synthesis doc exists (final output)
    if (repo_path / "12_synthesis_doc.yaml").exists():
        return "complete"
    
    # Check if function docs exist (partial progress)
    if (repo_path / "5_function_docs.yaml").exists():
        return "complete"
    
    # Check if file tree exists (minimal progress)
    if (repo_path / "1_file_tree.yaml").exists():
        return "in_progress"
    
    return "error"


@app.get("/api/repos", response_model=list[RepoSummary])
async def list_repos():
    """List all analyzed repositories."""
    if not DOCS_DIR.exists():
        return []
    
    repos = []
    for repo_path in DOCS_DIR.iterdir():
        if not repo_path.is_dir():
            continue
        
        # Skip hidden directories
        if repo_path.name.startswith("."):
            continue
        
        # Count files
        file_tree = load_file_tree(repo_path / "1_file_tree.yaml")
        file_count = len(file_tree)
        
        # Count functions
        function_docs = load_yaml(repo_path / "5_function_docs.yaml")
        function_count = len(function_docs) if function_docs else 0
        
        # Count classes
        class_groups = load_yaml(repo_path / "6_class_groups.yaml")
        class_count = len(class_groups) if class_groups else 0
        
        # Check for Docusaurus site
        has_site = (repo_path / "site").exists()
        
        repos.append(RepoSummary(
            name=repo_path.name,
            file_count=file_count,
            function_count=function_count,
            class_count=class_count,
            status=get_repo_status(repo_path),
            has_site=has_site,
        ))
    
    return sorted(repos, key=lambda r: r.name)


@app.get("/api/repos/{repo_name}", response_model=RepoDetail)
async def get_repo(repo_name: str):
    """Get detailed information about a repository."""
    repo_path = DOCS_DIR / repo_name
    
    if not repo_path.exists():
        raise HTTPException(status_code=404, detail=f"Repository '{repo_name}' not found")
    
    # Load file tree (plain text format, one file per line)
    file_tree = load_file_tree(repo_path / "1_file_tree.yaml")
    
    # Load function docs
    function_docs = load_yaml(repo_path / "5_function_docs.yaml") or []
    
    # Simplify function data for frontend
    functions = []
    for func in function_docs:
        functions.append({
            "node_id": func.get("node_id", ""),
            "file": func.get("file", ""),
            "name": func.get("name", ""),
            "signature": func.get("signature", ""),
            "docstring": func.get("docstring", ""),
            "line_start": func.get("line_start"),
            "line_end": func.get("line_end"),
        })
    
    # Load class groups
    class_groups = load_yaml(repo_path / "6_class_groups.yaml") or []
    
    # Simplify class data for frontend
    classes = []
    for cls in class_groups:
        methods = cls.get("methods", [])
        classes.append({
            "class_id": cls.get("class_id", ""),
            "file": cls.get("file", ""),
            "name": cls.get("name", ""),
            "method_count": len(methods),
            "methods": [
                {
                    "name": m.get("name", ""),
                    "signature": m.get("signature", ""),
                    "docstring": m.get("docstring", ""),
                }
                for m in methods
            ],
        })
    
    return RepoDetail(
        name=repo_name,
        files=file_tree,
        functions=functions,
        classes=classes,
    )


def get_project_python() -> str:
    """Get the Python executable for the main project.
    
    Checks for a venv in the project root, otherwise uses system Python.
    """
    # Check for project venv
    venv_python = PROJECT_ROOT / "venv" / "bin" / "python"
    if venv_python.exists():
        return str(venv_python)
    
    # Check for .venv
    venv_python = PROJECT_ROOT / ".venv" / "bin" / "python"
    if venv_python.exists():
        return str(venv_python)
    
    # Fall back to python3 in PATH
    return "python3"


def run_analysis(repo_url: str, task_id: str):
    """Run the documentation analysis in a subprocess."""
    try:
        tasks[task_id]["status"] = "running"
        tasks[task_id]["started_at"] = __import__("time").time()
        
        # Get the correct Python for the main project
        python_executable = get_project_python()
        
        # Run the main.py script using Popen so we can cancel it
        # Use start_new_session=True to create a new process group for easier killing
        process = subprocess.Popen(
            [python_executable, str(PROJECT_ROOT / "main.py"), repo_url],
            cwd=PROJECT_ROOT,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env={**os.environ, "PYTHONUNBUFFERED": "1"},
            start_new_session=True,  # Create new process group
        )
        
        # Store the process so we can cancel it
        running_processes[task_id] = process
        
        # Wait for completion
        stdout, stderr = process.communicate()
        
        # Clean up process reference
        running_processes.pop(task_id, None)
        
        # Check if cancelled
        if tasks[task_id].get("status") == "cancelled":
            return
        
        if process.returncode == 0:
            tasks[task_id]["status"] = "complete"
            tasks[task_id]["output"] = stdout
        else:
            tasks[task_id]["status"] = "error"
            tasks[task_id]["error"] = stderr or stdout
    except Exception as e:
        running_processes.pop(task_id, None)
        if tasks[task_id].get("status") != "cancelled":
            tasks[task_id]["status"] = "error"
            tasks[task_id]["error"] = str(e)


@app.post("/api/repos")
async def analyze_repo(request: AnalyzeRequest, background_tasks: BackgroundTasks):
    """Start analyzing a new repository."""
    repo_url = request.repo_url.strip()
    
    if not repo_url:
        raise HTTPException(status_code=400, detail="Repository URL is required")
    
    # Extract repo name from URL for task ID
    if repo_url.startswith("http"):
        task_id = repo_url.rstrip("/").split("/")[-1].replace(".git", "")
    else:
        task_id = Path(repo_url).name
    
    # Check if already running
    if task_id in tasks and tasks[task_id].get("status") == "running":
        raise HTTPException(status_code=409, detail=f"Analysis for '{task_id}' is already running")
    
    # Initialize task
    tasks[task_id] = {
        "repo_url": repo_url,
        "status": "queued",
        "output": None,
        "error": None,
    }
    
    # Start background task
    background_tasks.add_task(run_analysis, repo_url, task_id)
    
    return {"task_id": task_id, "status": "queued"}


# Progress steps based on file creation order
PROGRESS_STEPS = [
    {"file": "repo", "step": "fetching", "label": "Fetching repository", "icon": "download"},
    {"file": "1_file_tree.yaml", "step": "analyzing", "label": "Analyzing file structure", "icon": "folder-tree"},
    {"file": "2_node_extraction.yaml", "step": "extracting", "label": "Extracting code elements", "icon": "code"},
    {"file": "3_doc_order.yaml", "step": "ordering", "label": "Building dependency graph", "icon": "git-branch"},
    {"file": "5_function_docs.yaml", "step": "documenting_functions", "label": "Documenting functions", "icon": "function-square"},
    {"file": "6_class_groups.yaml", "step": "documenting_classes", "label": "Documenting classes", "icon": "boxes"},
    {"file": "site", "step": "generating_site", "label": "Generating documentation site", "icon": "globe"},
]


def get_detailed_counts(repo_path: Path) -> dict:
    """Get detailed counts for functions, classes, files during processing."""
    counts = {
        "files": {"done": 0, "total": 0},
        "functions": {"done": 0, "total": 0},
        "classes": {"done": 0, "total": 0},
    }
    
    # Count total files from file tree
    file_tree_path = repo_path / "1_file_tree.yaml"
    if file_tree_path.exists():
        file_tree = load_file_tree(file_tree_path)
        counts["files"]["total"] = len(file_tree)
        counts["files"]["done"] = len(file_tree)  # File analysis is atomic
    
    # Count total functions from doc order (functions to document)
    doc_order_path = repo_path / "3_doc_order.yaml"
    if doc_order_path.exists():
        doc_order = load_yaml(doc_order_path) or []
        counts["functions"]["total"] = len(doc_order)
    
    # Count documented functions
    func_docs_path = repo_path / "5_function_docs.yaml"
    if func_docs_path.exists():
        func_docs = load_yaml(func_docs_path) or []
        counts["functions"]["done"] = len(func_docs)
    
    # Count classes from node extraction
    node_extraction_path = repo_path / "2_node_extraction.yaml"
    if node_extraction_path.exists():
        node_data = load_yaml(node_extraction_path) or []
        # Count unique classes across all files
        class_count = 0
        for file_info in node_data:
            functions = file_info.get("functions", [])
            for func in functions:
                if func.get("type") == "class":
                    class_count += 1
        counts["classes"]["total"] = class_count
    
    # Count documented classes
    class_groups_path = repo_path / "6_class_groups.yaml"
    if class_groups_path.exists():
        class_groups = load_yaml(class_groups_path) or []
        counts["classes"]["done"] = len(class_groups)
    
    return counts


def get_task_progress(task_id: str) -> dict:
    """Get detailed progress for a task by checking which files exist."""
    repo_path = DOCS_DIR / task_id
    
    completed_steps = []
    current_step = None
    
    for i, step_info in enumerate(PROGRESS_STEPS):
        file_path = repo_path / step_info["file"]
        if file_path.exists():
            completed_steps.append(step_info["step"])
        elif current_step is None:
            current_step = step_info
    
    # Calculate progress percentage
    total_steps = len(PROGRESS_STEPS)
    completed_count = len(completed_steps)
    progress_percent = int((completed_count / total_steps) * 100)
    
    # Get detailed counts
    details = get_detailed_counts(repo_path)
    
    # If all steps complete, we're done
    if completed_count == total_steps:
        current_step = {"step": "complete", "label": "Documentation complete!", "icon": "check-circle"}
        progress_percent = 100
    elif current_step is None:
        current_step = PROGRESS_STEPS[0]
    
    return {
        "completed_steps": completed_steps,
        "current_step": current_step,
        "progress_percent": progress_percent,
        "total_steps": total_steps,
        "completed_count": completed_count,
        "details": details,
    }


@app.get("/api/tasks")
async def list_tasks():
    """List all analysis tasks."""
    result = []
    for task_id, task_info in tasks.items():
        task_data = {"task_id": task_id, **task_info}
        if task_info.get("status") == "running":
            task_data["progress"] = get_task_progress(task_id)
        result.append(task_data)
    return result


@app.get("/api/tasks/{task_id}")
async def get_task(task_id: str):
    """Get status of a specific task."""
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail=f"Task '{task_id}' not found")
    
    task_data = {"task_id": task_id, **tasks[task_id]}
    
    # Add progress info if task is running
    if tasks[task_id].get("status") == "running":
        task_data["progress"] = get_task_progress(task_id)
    
    return task_data


@app.delete("/api/tasks/{task_id}")
async def cancel_task(task_id: str):
    """Cancel a running task."""
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail=f"Task '{task_id}' not found")
    
    if tasks[task_id].get("status") != "running":
        raise HTTPException(status_code=400, detail=f"Task '{task_id}' is not running")
    
    # Mark as cancelled
    tasks[task_id]["status"] = "cancelled"
    
    # Kill the process if it exists
    process = running_processes.get(task_id)
    if process:
        try:
            # Kill the entire process group (including child processes)
            # This is important for git operations that spawn subprocesses
            if hasattr(os, 'killpg'):
                try:
                    os.killpg(os.getpgid(process.pid), 15)  # SIGTERM to process group
                except (ProcessLookupError, OSError):
                    pass
            
            # Also try terminating the main process
            process.terminate()
            
            # Give it a moment to terminate gracefully
            try:
                process.wait(timeout=2)
            except subprocess.TimeoutExpired:
                # Force kill if it doesn't terminate
                if hasattr(os, 'killpg'):
                    try:
                        os.killpg(os.getpgid(process.pid), 9)  # SIGKILL to process group
                    except (ProcessLookupError, OSError):
                        pass
                process.kill()  # Fallback: kill main process
        except Exception as e:
            # Process might already be dead
            print(f"Error killing process: {e}")
        finally:
            running_processes.pop(task_id, None)
    
    return {"task_id": task_id, "status": "cancelled"}


@app.get("/api/config", response_model=list[ConfigValue])
async def get_config():
    """Get current configuration values (read-only)."""
    return [
        ConfigValue(
            name="DEBUG",
            value=DEBUG,
            description="Debug mode - print all prompts and responses to console"
        ),
        ConfigValue(
            name="LOG_LEVEL",
            value=LOG_LEVEL,
            description="Logging verbosity (DEBUG, INFO, WARNING, ERROR)"
        ),
        ConfigValue(
            name="ENABLE_EMBEDDINGS",
            value=ENABLE_EMBEDDINGS,
            description="Use embeddings for similar function search (RAG)"
        ),
        ConfigValue(
            name="ENABLE_CODE_EXAMPLES",
            value=ENABLE_CODE_EXAMPLES,
            description="Generate code examples from tests or function code"
        ),
        ConfigValue(
            name="ENABLE_TOC_HITL",
            value=ENABLE_TOC_HITL,
            description="Human-in-the-loop for documentation structure"
        ),
        ConfigValue(
            name="HITL_CONFIDENCE_THRESHOLD",
            value=HITL_CONFIDENCE_THRESHOLD,
            description="Minimum confidence score before prompting for human feedback"
        ),
        ConfigValue(
            name="REFLECTION_CONFIDENCE_THRESHOLD",
            value=REFLECTION_CONFIDENCE_THRESHOLD,
            description="Minimum score to exit reflection loop early"
        ),
        ConfigValue(
            name="MAX_REFLECTION_ITERATIONS",
            value=MAX_REFLECTION_ITERATIONS,
            description="Maximum reflection iterations before fallback"
        ),
        ConfigValue(
            name="CODE_EXAMPLE_MAX_RETRIES",
            value=CODE_EXAMPLE_MAX_RETRIES,
            description="Maximum retries for code example generation"
        ),
        ConfigValue(
            name="MAX_FILE_TREE_CONTENT_CHARS",
            value=MAX_FILE_TREE_CONTENT_CHARS,
            description="Maximum file tree content size for LLM context"
        ),
        ConfigValue(
            name="MAX_MD_FILE_CHARS",
            value=MAX_MD_FILE_CHARS,
            description="Maximum size for a single markdown file in LLM context"
        ),
        ConfigValue(
            name="MAX_TOTAL_MD_CONTEXT_CHARS",
            value=MAX_TOTAL_MD_CONTEXT_CHARS,
            description="Maximum total markdown context for LLM"
        ),
    ]


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
