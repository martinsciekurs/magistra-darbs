"""Prompt templates for LLM interactions."""

from pathlib import Path
from docgen.llm.client import call_llm
from docgen.utils.config import MAX_FILE_TREE_CONTENT_CHARS, MAX_REFLECTION_ITERATIONS
from docgen.llm.schemas import SynthesisDoc

GOOGLE_DOCSTRING_STYLE = """Use Google-style docstrings:
- First line: brief description
- Args: parameter descriptions (name: description)  
- Returns: return value description
- Raises: exceptions that may be raised"""

def get_repo_analysis_prompt(file_tree: str, existing_docs: str = "") -> str:
    """Get the prompt for repository analysis (used with structured output).
    
    Args:
        file_tree: The file tree listing
        existing_docs: Optional existing markdown documentation (README, etc.)
    
    Returns:
        The prompt string
    """
    existing_docs_section = ""
    if existing_docs:
        existing_docs_section = f"""
Existing Documentation:
{existing_docs}
"""
    
    return f"""You are a Senior Software Architect analyzing a codebase.

{existing_docs_section}
File Tree:
{file_tree}

Analyze this repository and provide:

1. **Summary**: Purpose, tech stack, and high-level architecture.

2. **Focus on Significance**: Map only files that constitute core logic, interfaces, and infrastructure.
   - Exclude: Unit tests, minor utility scripts, and boilerplate config (unless they define the architecture).

3. **Module Granularity**:
   - Create modules for distinct **Subsystems** or **Capabilities** (e.g., "Authentication", "API Layer", "Data Processing").
   - **Avoid Fragmentation**: No single-file modules unless it's a major standalone component.
   - **Avoid Over-Generalization**: Do not use generic names like "Utils" or "Helpers".
"""

def get_confidence_assessment_prompt(repo_analysis: str, file_tree: str) -> str:
    """Get prompt to assess confidence in repo analysis.
    
    Args:
        repo_analysis: The generated repository analysis YAML
        file_tree: The file tree listing
    
    Returns:
        Prompt string for confidence assessment
    """
    template = """You are assessing the confidence level of a repository analysis.

Repository Analysis:
{repo_analysis}

File Tree:
{file_tree}

Rate your confidence in this analysis on a scale of 1-100, where:
- 90-100: Very high confidence - clear structure, well-organized, obvious patterns
- 70-89: High confidence - good structure, mostly clear patterns
- 50-69: Moderate confidence - some ambiguity, unclear patterns
- 30-49: Low confidence - significant ambiguity, unclear structure
- 1-29: Very low confidence - highly ambiguous, minimal information

Consider:
- How clear is the repository structure?
- How confident are you about module groupings?
- How well can you infer purpose from file names?
- How much existing documentation is available?

Respond with ONLY a single integer between 1 and 100, nothing else.
"""
    return template.format(repo_analysis=repo_analysis, file_tree=file_tree)


def get_reflection_evaluation_prompt(
    repo_analysis: str,
    file_tree: str,
    iteration: int,
    previous_feedback: str = ""
) -> str:
    """Get prompt for evaluating repo analysis against a rubric.
    
    Args:
        repo_analysis: The repository analysis YAML to evaluate
        file_tree: The file tree listing
        iteration: Current iteration number (1, 2, or 3)
        previous_feedback: Feedback from previous iteration (if any)
    
    Returns:
        Prompt string for structured evaluation
    """
    previous_context = ""
    if previous_feedback:
        previous_context = f"""
## Previous Iteration Feedback (Iteration {iteration - 1}):
{previous_feedback}

Evaluate whether these issues were addressed.
"""
    
    return f"""You are evaluating the QUALITY of a generated repository analysis document.

IMPORTANT: You are NOT evaluating the source code itself. You are evaluating how well the GENERATED ANALYSIS DOCUMENT describes the repository. Your feedback should be about the analysis text, NOT suggestions to improve the actual codebase.

## File Tree (for reference):
{file_tree}

## Generated Repository Analysis to Evaluate:
{repo_analysis}
{previous_context}
## Evaluation Rubric

Score each criterion 1-100 based on the QUALITY OF THE GENERATED ANALYSIS (not the source code):

1. **Readability** (1-100): Is the generated analysis clear and well-written?
   - 90-100: Summary clearly explains purpose, module names are intuitive, descriptions are concise and informative
   - 70-89: Mostly clear with minor wording issues
   - 50-69: Vague descriptions, confusing terminology, or unclear explanations
   - Below 50: Hard to understand what modules do from reading the analysis

2. **Component Allocation** (1-100): Does the analysis group files into logical modules?
   - 90-100: The analysis groups related files together with clear boundaries and sensible module sizes
   - 70-89: Mostly logical groupings in the analysis
   - 50-69: The analysis groups unrelated files together or creates modules that are too large/small
   - Below 50: The analysis has arbitrary or confusing groupings

3. **No Duplicates** (1-100): Does the analysis define distinct, non-overlapping modules?
   - 90-100: Each module in the analysis has a distinct purpose, no generic "Utils" catch-alls
   - 70-89: Minor overlap between module descriptions
   - 50-69: The analysis has modules with similar/overlapping purposes
   - Below 50: The analysis has significant duplication or vague catch-all modules

4. **Completeness** (1-100): Does the analysis capture all important subsystems?
   - 90-100: The analysis identifies and describes all major functional areas of the codebase
   - 70-89: Most important subsystems are represented in the analysis
   - 50-69: The analysis is missing some important subsystems
   - Below 50: The analysis is missing critical parts of the codebase

5. **File Coverage** (1-100): Does the analysis assign significant files to exactly one module?
   - Note: Tests, minor utilities, and config files should be EXCLUDED from the analysis
   - 90-100: All significant source files appear in exactly one module, no duplicates, no orphans
   - 70-89: Most significant files are properly assigned in the analysis
   - 50-69: The analysis is missing some files or has duplicates
   - Below 50: Major file assignment issues in the analysis

## Instructions:
- Focus on improving THE GENERATED ANALYSIS DOCUMENT, not the source code
- Do NOT suggest changes to the actual codebase (like "move tests to a tests/ directory")

## Output Format Rules (STRICT):
- Each rubric score: 1 sentence max (e.g., "Readability: 85/100 - Module names are clear but summary is verbose.")
- Suggestions: Max 3, only if overall score < 85
- Only suggest things that CAN be done by rewriting the analysis text:
  - Reword/shorten descriptions
  - Rename modules
  - Reassign files between modules
  - Add/remove modules
- Do NOT suggest: diagrams, tables, glossaries, architecture changes, external artifacts

Iteration: {iteration}/3 ({"Final chance" if iteration == 3 else "Can improve"})
"""


def get_reflection_regeneration_prompt(
    file_tree: str,
    previous_analysis: str,
    evaluation_feedback: str,
    suggestions: list[str],
    existing_docs: str = ""
) -> str:
    """Get prompt for regenerating analysis based on reflection feedback.
    
    Args:
        file_tree: The file tree listing
        previous_analysis: The previous analysis YAML to improve
        evaluation_feedback: Detailed feedback from evaluation
        suggestions: List of suggestions for improvement
        existing_docs: Optional existing markdown documentation
    
    Returns:
        Prompt string for regeneration
    """
    existing_docs_section = ""
    if existing_docs:
        existing_docs_section = f"""
## Existing Documentation:
{existing_docs}
"""
    
    suggestions_text = "\n".join(f"- {s}" for s in suggestions) if suggestions else "- None"
    
    return f"""You are a Senior Software Architect improving a repository analysis based on evaluation feedback.

## Evaluation Feedback:
{evaluation_feedback}
{existing_docs_section}
## File Tree:
{file_tree}

## Previous Analysis (to improve):
{previous_analysis}

## Rules:
1. **Address the feedback**: Incorporate suggestions where applicable, keep accurate parts.
2. **Focus on Significance**: Only include core logic, interfaces, and infrastructure files.
   - Exclude: Tests, minor utilities, boilerplate config (unless they define architecture).
3. **Module Granularity**:
   - Create modules for distinct **Subsystems** or **Capabilities**.
   - **Avoid Fragmentation**: No single-file modules unless it's a major component.
   - **Avoid Over-Generalization**: No generic names like "Utils" or "Helpers".
4. **No Duplicates**: Each significant file belongs to exactly one module.

Generate an improved analysis."""


def generate_initial_analysis(repo_name: str, docs_base_dir: str = ".docs") -> str:
    """
    Generate initial repository analysis with modules from a saved file tree.
    This is a preliminary analysis based only on the file structure.

    Args:
        repo_name: Name of the repository.
        docs_base_dir: Root directory where docs are stored (default: .docs).

    Returns:
        Dict with 'summary' and 'modules' keys.

    Raises:
        FileNotFoundError: If the file tree does not exist.
    """
    # Use Pathlib for robust path handling
    base_path = Path(docs_base_dir)
    file_tree_path = base_path / repo_name / "1_file_tree.yaml"

    if not file_tree_path.exists():
        raise FileNotFoundError(f"File tree not found at {file_tree_path}")

    # Read file content
    try:
        file_tree_content = file_tree_path.read_text(encoding="utf-8").strip()
    except Exception as e:
        raise IOError(f"Failed to read file tree: {e}")

    # Safety Check: Truncate if tree is massive (LLMs have context limits)
    if len(file_tree_content) > MAX_FILE_TREE_CONTENT_CHARS:
        file_tree_content = file_tree_content[:MAX_FILE_TREE_CONTENT_CHARS] + "\n...[Tree Truncated]"

    # Generate Prompt
    prompt = get_repo_analysis_prompt(file_tree=file_tree_content)

    # Call LLM (Ensure your client handles timeouts/retries)
    return call_llm(
        prompt,
        generation_name="repo_analysis",
        metadata={"repo_name": repo_name, "stage": "repo_analysis"},
    )


def get_function_doc_prompt(
    repo_analysis: str,
    function_code: str,
    function_name: str,
    file_name: str,
    file_context: str,
    dependency_docs: list[dict],
    called_by: str,
    similar_functions: list[dict],
    *,
    signature: str = "",
    decorators: list[str] = None,
    raises: list[str] = None,
    visibility: str = "public",
    usage_snippets: list[str] = None,
) -> str:
    """Get the prompt template for function documentation."""
    # Format dependencies (increased truncation limit)
    dep_text = ""
    if dependency_docs:
        dep_lines = []
        for dep in dependency_docs:
            sig = dep.get("signature", dep.get("name", ""))
            doc = dep.get("docstring", "")
            dep_lines.append(f"  {sig}")
            if doc:
                dep_lines.append(f"    {doc[:500]}...")
        dep_text = "\n".join(dep_lines)
    
    # Format similar functions
    similar_text = ""
    if similar_functions:
        similar_lines = []
        for similar in similar_functions:
            sig = similar.get("signature", similar.get("name", ""))
            doc = similar.get("docstring", "")
            similar_lines.append(f"  {sig}")
            if doc:
                similar_lines.append(f"    {doc[:400]}...")
        similar_text = "\n".join(similar_lines)
    
    # Build prompt
    sections = []
    
    visibility_note = ""
    if visibility == "private":
        visibility_note = " This is a private/internal function - document briefly."
    elif visibility == "protected":
        visibility_note = " This is a protected function (internal API)."
    
    sections.append(f"""You are documenting a Python function.{visibility_note}
{GOOGLE_DOCSTRING_STYLE}
Use only provided data. Don't invent or hallucinate.""")
    
    # Function metadata
    func_meta = f"File: {file_name}\nName: {function_name}"
    if signature:
        func_meta += f"\nSignature: {signature}"
    if decorators:
        func_meta += f"\nDecorators: {', '.join(decorators)}"
    if raises:
        func_meta += f"\nRaises: {', '.join(raises)}"
    
    sections.append(f"Function:\n{func_meta}\n\n{function_code}")
    
    if file_context:
        sections.append(f"File Context:\n{file_context}")
    
    if dep_text:
        sections.append(f"Dependencies:\n{dep_text}")
    
    if called_by:
        sections.append(f"Called By:\n{called_by}")
    
    if usage_snippets:
        sections.append(f"Usage Examples (from codebase):\n" + "\n".join(f"  {s}" for s in usage_snippets[:3]))
    
    if similar_text:
        sections.append(f"Similar Functions (style reference):\n{similar_text}")
    
    output_parts = ["Purpose/description", "Parameters (with types)", "Returns (with type)"]
    if raises:
        output_parts.append(f"Raises ({', '.join(raises)})")
    
    sections.append(f"""Generate docstring. Include:
- {chr(10).join('- ' + p for p in output_parts[1:])}

Output ONLY the docstring. No backticks, no code blocks.""")
    
    return "\n\n".join(sections)


def get_class_doc_prompt(
    repo_analysis: str,
    class_name: str,
    file_name: str,
    file_context: str,
    methods: list[dict],
    *,
    decorators: list[str] = None,
) -> str:
    """Get the prompt template for class documentation."""
    methods_text = ""
    if methods:
        method_lines = []
        for method in methods:
            sig = method.get("signature", method.get("name", ""))
            doc = method.get("docstring", "")
            visibility = method.get("visibility", "public")
            prefix = "  " if visibility == "public" else "  [internal] "
            method_lines.append(f"{prefix}{sig}")
            if doc:
                doc_preview = doc[:400].replace("\n", " ")
                method_lines.append(f"    {doc_preview}...")
        methods_text = "\n".join(method_lines)
    
    sections = []
    sections.append(f"""You are documenting a Python class.
{GOOGLE_DOCSTRING_STYLE}
Use only provided data. Don't invent or hallucinate.""")
    
    class_meta = f"File: {file_name}\nClass: {class_name}"
    if decorators:
        class_meta += f"\nDecorators: {', '.join(decorators)}"
    
    sections.append(f"Class:\n{class_meta}")
    
    if file_context:
        sections.append(f"File Context:\n{file_context}")
    
    if methods_text:
        sections.append(f"Methods:\n{methods_text}")
    
    sections.append("""Generate class docstring. Include:
- Purpose/responsibility
- Key attributes (if inferable)
- Brief summary

Output ONLY the docstring. No backticks, no code blocks.""")
    
    return "\n\n".join(sections)


def get_file_doc_prompt(
    repo_analysis: str,
    file_name: str,
    file_context: str,
    functions: list[dict],
    classes: list[dict],
) -> str:
    """Get the prompt template for file/module documentation."""
    # Format functions (public first)
    functions_text = ""
    if functions:
        func_lines = []
        for func in sorted(functions, key=lambda f: f.get("visibility", "public") != "public"):
            sig = func.get("signature", func.get("name", ""))
            doc = func.get("docstring", "")
            visibility = func.get("visibility", "public")
            prefix = "  " if visibility == "public" else "  [internal] "
            func_lines.append(f"{prefix}{sig}")
            if doc:
                doc_preview = doc[:400].replace("\n", " ")
                func_lines.append(f"    {doc_preview}...")
        functions_text = "\n".join(func_lines)
    
    # Format classes
    classes_text = ""
    if classes:
        class_lines = []
        for cls in classes:
            name = cls.get("name", "")
            doc = cls.get("docstring", "")
            methods = cls.get("methods", [])
            class_lines.append(f"  class {name}:")
            if doc:
                doc_preview = doc[:400].replace("\n", " ")
                class_lines.append(f"    {doc_preview}...")
            if methods:
                public_methods = [m.get("name", "") for m in methods if not m.get("name", "").startswith("_")]
                if public_methods:
                    class_lines.append(f"    Public methods: {', '.join(public_methods[:8])}")
        classes_text = "\n".join(class_lines)
    
    sections = []
    sections.append(f"""You are documenting a Python file for a documentation site.
Use only provided data. Don't invent or hallucinate.""")

    sections.append(f"File: {file_name}")

    if file_context:
        sections.append(f"File Context:\n{file_context}")

    if functions_text:
        sections.append(f"Functions:\n{functions_text}")

    if classes_text:
        sections.append(f"Classes:\n{classes_text}")

    sections.append("""Generate a concise file overview (2-4 sentences). Include:
- Purpose of this file
- Key exports (main functions/classes)
- Technical details (algorithm names, data formats, config options)

Do NOT include Args/Returns/Raises sections (those go on individual functions, not file overviews).
Output ONLY the overview text. No backticks, no code blocks.""")
    
    return "\n\n".join(sections)


def get_module_doc_prompt(
    repo_analysis: str,
    module_name: str,
    module_description: str,
    files: list[dict],
    *,
    depends_on: list[str] = None,
) -> str:
    """Get the prompt template for module/package documentation."""
    files_text = ""
    if files:
        file_lines = []
        for f in files:
            file_name = f.get("file", "")
            doc = f.get("docstring", "")
            functions = f.get("functions", [])
            classes = f.get("classes", [])
            
            file_lines.append(f"  {file_name}:")
            if doc:
                doc_preview = doc[:300].replace("\n", " ")
                file_lines.append(f"    {doc_preview}...")
            if functions:
                file_lines.append(f"    Functions: {', '.join(functions[:8])}")
            if classes:
                file_lines.append(f"    Classes: {', '.join(classes[:5])}")
        files_text = "\n".join(file_lines)
    
    sections = []
    sections.append(f"""You are documenting a Python module/package for a documentation site.
Use only provided data. Don't invent or hallucinate.""")

    module_meta = f"Name: {module_name}\nDescription: {module_description}"
    if depends_on:
        module_meta += f"\nDepends on: {', '.join(depends_on)}"

    sections.append(f"Module:\n{module_meta}")

    if files_text:
        sections.append(f"Files:\n{files_text}")

    sections.append("""Generate module documentation. Structure with markdown headers:

### Architectural purpose
(1-2 sentences on the module's role in the system)

### Key components and responsibilities
(List main files/classes with brief descriptions. Focus on PUBLIC APIs only - skip private functions starting with _)

### Main entry points
(List the primary public functions/classes users should know about)

IMPORTANT:
- Do NOT repeat the module name or description at the start (it's already shown above)
- Do NOT include Args/Returns/Raises sections (this is module docs, not function docs)
- Preserve exact technical terms (algorithm names, data formats, config parameters)

Output ONLY the documentation content. No backticks wrapping the output.""")
    
    return "\n\n".join(sections)


def get_toc_proposal_prompt(
    repo_name: str,
    repo_analysis: str,
    module_docs: list[dict],
    file_tree: str,
    existing_docs: str = ""
) -> str:
    """Get prompt for proposing a documentation table of contents structure.
    
    Args:
        repo_name: Name of the repository
        repo_analysis: Repository analysis YAML text
        module_docs: List of module documentation dicts
        file_tree: File tree listing
        existing_docs: Existing markdown documentation from the repository
        
    Returns:
        The prompt template string
    """
    # Format module docs summary
    modules_text = ""
    if module_docs:
        module_lines = []
        for mod in module_docs[:10]:  # Limit to first 10 modules
            name = mod.get("module", "")
            desc = mod.get("description", "")
            module_lines.append(f"- {name}: {desc}")
        modules_text = "\n".join(module_lines)
    
    sections = []
    sections.append(f"""You are a Senior Technical Writer analyzing the "{repo_name}" project to propose an optimal documentation structure.

Based on the project analysis below, propose a table of contents (TOC) that would best serve users of this project.""")
    
    sections.append(f"""Repository Analysis:
{repo_analysis}""")
    
    if modules_text:
        sections.append(f"""Key Modules:
{modules_text}""")
    
    sections.append(f"""File Structure (excerpt):
{file_tree[:3000]}...""")
    
    if existing_docs:
        sections.append(f"""Existing Documentation (from repository):
{existing_docs[:5000]}

Analyze the existing documentation structure for inspiration on appropriate sections.""")
    
    sections.append("""## Instructions

Propose a documentation TOC with 6-12 top-level sections. Sections can have subsections.

1. **Core sections (always include):**
   - Introduction/Overview (slug: "introduction", is_core: true)
   - Quick Start/Getting Started (slug: "quick-start", is_core: true)  
   - Architecture (slug: "architecture", is_core: true)

2. **Project-specific sections based on what you see:**
   - For frameworks: Configuration, Plugins/Extensions, Deployment
   - For libraries: API Reference, Examples, Migration Guide
   - For CLIs: Commands, Configuration, Scripting
   - For SDKs: Authentication, API Reference, Error Handling
   - For ML/AI: Models, Training, Inference, Data Preparation

3. **Common optional sections:**
   - Key Concepts / Terminology
   - How-To Guides (with subsections for each guide)
   - Troubleshooting
   - FAQ
   - Changelog
   - Contributing

4. **Subsections:**
   - Use subsections to break down large topics (e.g., "Configuration" → "Environment Variables", "CLI Options")
   - Each subsection has: slug, title, description
   - Don't over-nest - only use subsections when the topic is large enough

Choose sections that make sense for THIS specific project.
Order logically (intro first, reference material later).
Use lowercase slugs with hyphens.""")
    
    return "\n\n".join(sections)


def get_toc_refinement_prompt(
    previous_toc: list[dict],
    user_feedback: str,
    repo_name: str,
    repo_analysis: str
) -> str:
    """Get prompt for refining TOC based on user feedback.
    
    Args:
        previous_toc: The previous TOC proposal as list of section dicts
        user_feedback: User's feedback on the TOC
        repo_name: Name of the repository
        repo_analysis: Repository analysis for context
        
    Returns:
        The prompt template string
    """
    # Format previous TOC
    toc_lines = []
    for i, section in enumerate(previous_toc):
        core_marker = " [CORE]" if section.get("is_core") else ""
        toc_lines.append(f"{i+1}. {section.get('title', '')} (slug: {section.get('slug', '')}){core_marker}")
        if section.get("description"):
            toc_lines.append(f"   {section.get('description', '')}")
    previous_toc_text = "\n".join(toc_lines)
    
    return f"""You are refining a documentation TOC based on user feedback.

## Previous TOC:
{previous_toc_text}

## User Feedback:
{user_feedback}

## Project Context:
Repository: {repo_name}
{repo_analysis[:2000]}...

## Instructions:

Update the TOC based on the user's feedback. You may:
- Add new sections the user requested
- Remove sections the user indicated are not needed
- Reorder sections as requested
- Rename sections for clarity
- Merge or split sections

Keep core sections (Introduction, Quick Start, Architecture) unless user explicitly removes them.
Maintain logical ordering (intro → concepts → guides → reference).
Use lowercase slugs with hyphens."""


def get_dynamic_synthesis_prompt(
    repo_name: str,
    confirmed_toc: list[dict],
    repo_analysis: str,
    module_docs: list[dict],
    file_tree: str,
    existing_docs: str = ""
) -> str:
    """Get prompt for generating documentation content based on confirmed TOC.
    
    Args:
        repo_name: Name of the repository
        confirmed_toc: The confirmed TOC structure
        repo_analysis: Repository analysis YAML text
        module_docs: List of module documentation dicts
        file_tree: File tree listing
        existing_docs: Existing markdown documentation
        
    Returns:
        The prompt template string
    """
    # Format TOC for prompt
    toc_lines = []
    for section in confirmed_toc:
        toc_lines.append(f"- {section.get('title', '')} (slug: {section.get('slug', '')}): {section.get('description', '')}")
    toc_text = "\n".join(toc_lines)
    
    # Format module docs
    modules_text = ""
    if module_docs:
        module_lines = []
        for mod in module_docs:
            name = mod.get("module", "")
            docstring = mod.get("docstring", "")[:500]
            module_lines.append(f"## {name}\n{docstring}...")
        modules_text = "\n".join(module_lines)
    
    sections = []
    sections.append(f"""You are a Senior Technical Writer creating documentation for "{repo_name}".

Generate comprehensive content for each section in the confirmed TOC below.
Use only provided data, don't invent or hallucinate.""")
    
    sections.append(f"""## Confirmed Table of Contents:
{toc_text}""")
    
    sections.append(f"""## Repository Analysis:
{repo_analysis}""")
    
    sections.append(f"""## File Structure:
{file_tree[:2000]}...""")
    
    if modules_text:
        sections.append(f"""## Module Documentation:
{modules_text}""")
    
    if existing_docs:
        sections.append(f"""## Existing Documentation (reference):
{existing_docs}

Use this to inform your content but reorganize into the confirmed TOC structure.""")
    
    sections.append("""## Instructions:

Generate content for EACH section in the TOC. For each section:
- Match the slug exactly as specified
- Write comprehensive, useful content (not placeholder text)
- Use markdown formatting appropriately
- Include code examples where relevant
- Be specific to this project, not generic
- Preserve exact technical terms from module docs (algorithm names like Kahn's algorithm, data formats, config parameters)

The output should be a list of sections with slug, title, and full content.""")
    
    return "\n\n".join(sections)


def get_synthesis_doc_prompt(
    repo_name: str,
    repo_analysis: str,
    module_docs: list[dict],
    file_tree: str,
    existing_docs: str = ""
) -> str:
    """Get the prompt template for synthesizing high-level documentation.
    
    This generates the Introduction, Why, Quick Start, Architecture Overview,
    and How-To guides by synthesizing all gathered context.
    
    Args:
        repo_name: Name of the repository
        repo_analysis: Repository analysis YAML text (from 4_llm_summary.yaml)
        module_docs: List of module documentation dicts (from 11_module_docs.yaml)
        file_tree: File tree listing (from 1_file_tree.yaml)
        existing_docs: Existing markdown documentation from the repository
        
    Returns:
        The prompt template string
    """
    # Format module docs summary
    modules_text = ""
    if module_docs:
        module_lines = []
        for mod in module_docs:
            name = mod.get("module", "")
            desc = mod.get("description", "")
            docstring = mod.get("docstring", "")[:800]
            files = mod.get("files", [])
            module_lines.append(f"## {name}")
            if desc:
                module_lines.append(f"Description: {desc}")
            if docstring:
                module_lines.append(f"Documentation: {docstring}...")
            if files:
                module_lines.append(f"Files: {', '.join(files)}")
            module_lines.append("")
        modules_text = "\n".join(module_lines)
    
    # Build prompt
    sections = []
    sections.append(f"""You are a Senior Technical Writer creating comprehensive documentation for the "{repo_name}" project.
Based on the analysis and documentation gathered below, generate a complete documentation guide.
Use only provided data, report only for what you are absolutely sure, don't invent or hallucinate anything else.""")
    
    sections.append(f"""Repository Analysis:
{repo_analysis}""")
    
    sections.append(f"""File Structure:
{file_tree}""")
    
    if modules_text:
        sections.append(f"""Module Documentation:
{modules_text}""")
    
    if existing_docs:
        sections.append(f"""Existing Documentation (from repository markdown files):
{existing_docs}

Use this existing documentation to inform your synthesis. IMPORTANT: Preserve exact technical terminology (algorithm names, format names, config options) from READMEs and docs - do not paraphrase technical terms.""")
    
    sections.append("""Generate comprehensive documentation with the following sections:

- introduction: A 2-3 paragraph introduction explaining what this project is, who it's for, and what problems it solves. Be specific about capabilities and use cases. Preserve exact technical terminology from module docs (algorithm names, format names, parameter names).

- why: Explain the motivation behind this project. What problem does it solve? Why would someone choose this over alternatives? What are the key benefits?

- quick_start: Step-by-step instructions to get started with the project. Include installation, basic configuration, and a simple example. Use numbered steps. Use ```bash for shell commands and ```python for Python code.

- architecture: High-level architecture overview. Explain how the major components work together. Describe the data flow, algorithms used, and processing pipeline if applicable.

- key_concepts: Define important terms, abstractions, and patterns used in the project. Help new users understand the mental model.

- how_to_guides: A list of step-by-step guides for common use cases. Each guide should have a clear title and detailed content.""")
    
    return "\n\n".join(sections)


def get_docstring_evaluation_prompt(
    docstring: str,
    doc_type: str,  # "function", "class", "file", or "module"
    context: str,  # The code/context being documented
    original_prompt: str,  # The base prompt used for generation
    iteration: int = 1,
    previous_feedback: str = ""
) -> str:
    """Get prompt for evaluating a docstring against a rubric.
    
    Args:
        docstring: The docstring to evaluate
        doc_type: Type of docstring ("function", "class", "file", "module")
        context: The code/context that was documented
        original_prompt: The base prompt used to generate this docstring
        iteration: Current iteration number
        previous_feedback: Feedback from previous iteration (if any)
    
    Returns:
        Prompt string for structured evaluation
    """
    previous_context = ""
    if previous_feedback:
        previous_context = f"""
## Previous Iteration Feedback (Iteration {iteration - 1}):
{previous_feedback}

Evaluate whether these issues were addressed.
"""
    
    return f"""Evaluate this {doc_type} docstring using quality criteria D1-D6. Be BRIEF.

## Code:
{context}

## Docstring to Evaluate:
{docstring}
{previous_context}
## Docstring Quality Rubric D1-D6 (score 1-100 each):

1. **D1 - Clarity**: Is the docstring clear and easy to understand without additional context?
2. **D2 - Actuality**: Does it accurately reflect the current code (parameters, return types, behavior)?
3. **D3 - Structure**: Is it well-organized with clear sections (Args, Returns, Raises) in proper order?
4. **D4 - Conciseness**: Is it appropriately concise without being too brief or verbose?
5. **D5 - Precision**: Is the technical information accurate with no hallucinations or invented details?
6. **D6 - Consistency**: Does it follow Google docstring style consistently?

## Rules:
- Feedback: 1 sentence max per criterion
- Suggestions: max 3, only if overall score < 85
- Focus on MAJOR issues only, skip nitpicks
- Weight D2 (Actuality) and D5 (Precision) highest - documentation must match code

Iteration: {iteration}/{MAX_REFLECTION_ITERATIONS}
"""


def get_docstring_regeneration_prompt(
    original_prompt: str,
    previous_docstring: str,
    evaluation_feedback: str,
    suggestions: list[str],
    context: str
) -> str:
    """Get prompt for regenerating a docstring based on evaluation feedback.
    
    Args:
        original_prompt: The original base prompt used for generation
        previous_docstring: The previous docstring to improve
        evaluation_feedback: Detailed feedback from evaluation
        suggestions: List of suggestions for improvement
        context: The code/context being documented
    
    Returns:
        Prompt string for regeneration
    """
    suggestions_text = "\n".join(f"- {s}" for s in suggestions) if suggestions else "- None"
    
    return f"""You are improving a docstring based on evaluation feedback.

## Evaluation Feedback:
{evaluation_feedback}

## Suggestions:
{suggestions_text}

## Code/Context Being Documented:
{context}

## Previous Docstring (to improve):
{previous_docstring}

## Original Generation Prompt (for reference):
{original_prompt}

## Instructions:
- Address the feedback and incorporate suggestions
- Keep accurate parts from the previous docstring
- Ensure consistency with the original prompt requirements
- Generate an improved docstring that addresses the identified issues
"""


def get_synthesis_evaluation_prompt(
    synthesis: SynthesisDoc,
    repo_analysis: str,
    module_docs: list[dict],
    file_tree: str,
    original_prompt: str,
    iteration: int = 1,
    previous_feedback: str = ""
) -> str:
    """Get prompt for evaluating synthesis documentation against a rubric.
    
    Args:
        synthesis: The synthesis documentation to evaluate
        repo_analysis: Repository analysis YAML
        module_docs: List of module documentation dicts
        file_tree: File tree listing
        original_prompt: The base prompt used for generation
        iteration: Current iteration number
        previous_feedback: Feedback from previous iteration (if any)
    
    Returns:
        Prompt string for structured evaluation
    """
    # Convert synthesis to text for evaluation
    synthesis_text = f"""Introduction:
{synthesis.introduction}

Why:
{synthesis.why}

Quick Start:
{synthesis.quick_start}

Architecture:
{synthesis.architecture}

Key Concepts:
{synthesis.key_concepts}

How-To Guides:
{chr(10).join(f"- {g.title}: {g.content[:200]}..." for g in synthesis.how_to_guides)}
"""
    
    previous_context = ""
    if previous_feedback:
        previous_context = f"""
## Previous Iteration Feedback (Iteration {iteration - 1}):
{previous_feedback}

Evaluate whether these issues were addressed.
"""
    
    return f"""You are a Senior Technical Writer reviewing synthesis documentation.

## Original Generation Prompt:
{original_prompt}

## Repository Analysis:
{repo_analysis}

## Module Documentation:
{chr(10).join(f"- {m.get('module', '')}: {m.get('docstring', '')[:200]}..." for m in module_docs[:5])}

## File Tree:
{file_tree[:1000]}...

## Generated Synthesis Documentation to Evaluate:
{synthesis_text}
{previous_context}
## Synthesis Quality Rubric S1-S6

Score each criterion 1-100 and provide specific feedback:

1. **S1 - Clarity** (1-100): Is the documentation clear and well-structured?
   - 90-100: Crystal clear, well-organized, easy to navigate
   - 70-89: Mostly clear with minor issues
   - 50-69: Some confusing or unclear sections
   - Below 50: Significant clarity issues

2. **S2 - Actuality** (1-100): Does the documentation accurately reflect the current codebase?
   - 90-100: Completely up-to-date, matches current architecture and features
   - 70-89: Mostly current with minor outdated elements
   - 50-69: Some outdated or mismatched information
   - Below 50: Significantly out of sync with codebase

3. **S3 - Findability** (1-100): Is information well-organized and easy to locate?
   - 90-100: Excellent structure, clear navigation, logical sections
   - 70-89: Good organization with minor findability issues
   - 50-69: Some information hard to locate
   - Below 50: Poor organization, information scattered

4. **S4 - Usefulness** (1-100): Does the documentation provide practical value?
   - 90-100: Extremely useful, helps users get started and understand the project
   - 70-89: Mostly useful with actionable guidance
   - 50-69: Somewhat useful but missing important practical information
   - Below 50: Not very useful for real-world usage

5. **S5 - Precision** (1-100): Is the technical information accurate with no hallucinations?
   - 90-100: Completely accurate, no invented or fabricated details
   - 70-89: Mostly accurate with minor imprecisions
   - 50-69: Some inaccuracies or hallucinated content
   - Below 50: Significant inaccuracies or fabrications

6. **S6 - Consistency** (1-100): Does the documentation maintain consistent style and terminology?
   - 90-100: Uniform style, consistent terminology throughout
   - 70-89: Mostly consistent with minor variations
   - 50-69: Noticeable inconsistencies in style or terms
   - Below 50: Inconsistent, confusing terminology/style

## Output Format Rules (STRICT):
- Each rubric score: 1 sentence max (e.g., "S1 Clarity: 85/100 - Well-structured but intro is verbose.")
- Suggestions: Max 3, only if overall score < 85
- Weight S2 (Actuality) and S5 (Precision) highest - documentation must match code
- Only suggest things that CAN be done by rewriting the synthesis text:
  - Reword/shorten sections
  - Add missing content
  - Fix inaccuracies or hallucinations
  - Improve consistency
- Do NOT suggest: diagrams, external tools, format changes, structural overhauls

Iteration: {iteration}/{MAX_REFLECTION_ITERATIONS} ({"Final chance" if iteration == MAX_REFLECTION_ITERATIONS else "Can improve"})
"""


def get_code_example_prompt_with_tests(
    function_name: str,
    function_signature: str,
    function_docstring: str,
    test_content: str,
    test_file_path: str,
    usage_snippets: list[str] = None,
) -> str:
    """Get prompt for generating code example from test file."""
    usage_section = ""
    if usage_snippets:
        usage_section = f"""
## Real Usage (from codebase)
{chr(10).join(usage_snippets)}
"""
    
    return f"""Generate a simple code example for this function.

## Function
Name: {function_name}
Signature: {function_signature}
Description: {function_docstring}
{usage_section}
## Test File (verified working examples)
File: {test_file_path}

```python
{test_content}
```

## Requirements
- Simplify the test patterns into a clean usage example (3-8 lines)
- Remove all test boilerplate (no pytest, assert, Mock, @patch, unittest)
- Start with the import statement for the function
- Use realistic input values from the tests or real usage above
- Add a brief comment showing expected output/behavior

## Formatting (STRICT)
- Avoid blank lines between statements - code must be compact
- Keep lines under 60 characters - wrap long literals/args
- Prefer one-liners: `data = {{"a": 1, "b": 2}}` not multi-line dicts
- Short variable names (e.g., `cfg`, `result`, `path`)
- Do NOT redefine the function or its dependencies

Output ONLY valid Python code. No explanations. No markdown code blocks."""


def get_code_example_prompt_from_code(
    function_name: str,
    function_signature: str,
    function_docstring: str,
    function_code: str,
    usage_snippets: list[str] = None,
) -> str:
    """Get prompt for generating code example from function code (no tests available)."""
    usage_section = ""
    if usage_snippets:
        usage_section = f"""
## Real Usage (from codebase)
{chr(10).join(usage_snippets)}

Use these real usage patterns as reference for your example.
"""
    
    return f"""Generate a simple code example for this function.

## Function
Name: {function_name}
Signature: {function_signature}

## Description
{function_docstring}
{usage_section}
## Full Implementation
```python
{function_code}
```

## Requirements
- Show how to import and use this function (3-8 lines)
- Start with the import statement (e.g., `from module import {function_name}`)
- Use realistic input values (from real usage above if available)
- Add a brief comment showing expected output/behavior

## Formatting (STRICT)
- Avoid blank lines between statements - code must be compact
- Keep lines under 60 characters - wrap long literals/args
- Prefer one-liners: `data = {{"a": 1, "b": 2}}` not multi-line dicts
- Short variable names (e.g., `cfg`, `result`, `path`)
- Do NOT redefine the function or its dependencies

Output ONLY valid Python code. No explanations. No markdown code blocks."""


def get_code_example_validation_prompt(
    code: str,
    function_name: str,
    function_signature: str,
) -> str:
    """
    Get prompt for validating a generated code example.
    
    Args:
        code: The generated code example
        function_name: Name of the function being documented
        function_signature: Function signature
        
    Returns:
        Prompt string
    """
    return f"""You are validating a code example for documentation quality.

## Function Being Documented
Name: {function_name}
Signature: {function_signature}

## Generated Code Example
```python
{code}
```

## Validation Checklist
Check each item carefully:

1. **Calls the function**: Does the example actually call `{function_name}`?
2. **Correct arguments**: Are the argument types and count plausible for the signature?
3. **Has import**: Does it start with an import statement for the function?
4. **No function redefinition**: Does it avoid redefining the function or its dependencies?
5. **No test artifacts**: No pytest, assert, Mock, unittest, @patch, fixtures?
6. **Realistic values**: Are input values realistic (not placeholders like "string", "value", 123)?
7. **Makes sense**: Does the example demonstrate meaningful, practical usage?
8. **Compact formatting**: Avoid blank lines, lines under 60 chars, one-liner style preferred?

If ANY check fails, mark is_valid as false and list the specific issues.
Be strict about quality - documentation examples should be exemplary."""


def get_code_example_retry_prompt(
    original_prompt: str,
    previous_code: str,
    issues: list[str],
) -> str:
    """
    Get prompt for retrying code example generation after validation failure.
    
    Args:
        original_prompt: The original generation prompt
        previous_code: The code that failed validation
        issues: List of issues from validation
        
    Returns:
        Updated prompt with feedback
    """
    issues_text = "\n".join(f"- {issue}" for issue in issues)
    
    return f"""{original_prompt}

## IMPORTANT: Previous attempt had issues
The previous code example was rejected for these reasons:
{issues_text}

Previous attempt:
```python
{previous_code}
```

Fix ALL the issues listed above in your new response.
Remember: NO blank lines, lines under 60 chars, compact one-liner style.
Output ONLY valid Python code. No explanations. No markdown code blocks."""


def get_architecture_diagram_prompt(
    repo_name: str,
    repo_analysis: str,
    module_docs: list[dict],
    file_tree: str,
) -> str:
    """Get prompt for generating architecture diagram in Mermaid format.
    
    Args:
        repo_name: Name of the repository
        repo_analysis: Repository analysis YAML text
        module_docs: List of module documentation dicts
        file_tree: File tree listing
        
    Returns:
        The prompt template string
    """
    # Format module docs summary
    modules_text = ""
    if module_docs:
        module_lines = []
        for mod in module_docs:
            name = mod.get("module", "")
            desc = mod.get("description", "")
            files = mod.get("files", [])
            module_lines.append(f"- {name}: {desc}")
            if files:
                module_lines.append(f"  Files: {', '.join(files[:5])}{'...' if len(files) > 5 else ''}")
        modules_text = "\n".join(module_lines)
    
    sections = []
    sections.append(f"""You are a Senior Software Architect creating a high-level architecture diagram for "{repo_name}".

Generate a simple Mermaid flowchart showing how the main components interact.""")
    
    sections.append(f"""## Repository Analysis:
{repo_analysis}""")
    
    if modules_text:
        sections.append(f"""## Modules:
{modules_text}""")
    
    sections.append(f"""## File Structure (excerpt):
{file_tree[:2000]}...""")
    
    sections.append("""## Instructions

Create a Mermaid flowchart (graph TB or graph LR) that shows:
1. **Main components/modules** as nodes (use short IDs like `parser`, `llm`, `output`)
2. **Data flow** between components with labeled arrows
3. **Subgraphs** for logical groupings (e.g., "Static Analysis", "LLM Pipeline")

Rules:
- Keep it SIMPLE: 5-15 nodes maximum
- Use clear, short labels
- Show the main flow, not every detail
- Use subgraph for module groupings
- Arrow labels should be brief (e.g., "parses", "generates", "calls")

Example format:
```
graph TB
    subgraph "Input"
        A[Source Files]
    end
    subgraph "Processing"  
        B[Parser] --> C[Analyzer]
    end
    A --> B
    C --> D[Output]
```

Also provide a brief explanation (1 sentence) for each component shown in the diagram.""")
    
    return "\n\n".join(sections)


def get_synthesis_regeneration_prompt(
    original_prompt: str,
    previous_synthesis: SynthesisDoc,
    evaluation_feedback: str,
    suggestions: list[str],
    repo_analysis: str,
    module_docs: list[dict],
    file_tree: str,
    existing_docs: str = ""
) -> str:
    """Get prompt for regenerating synthesis documentation based on evaluation feedback.
    
    Args:
        original_prompt: The original base prompt used for generation
        previous_synthesis: The previous synthesis to improve
        evaluation_feedback: Detailed feedback from evaluation
        suggestions: List of suggestions for improvement
        repo_analysis: Repository analysis YAML
        module_docs: List of module documentation dicts
        file_tree: File tree listing
        existing_docs: Existing markdown documentation
    
    Returns:
        Prompt string for regeneration
    """
    # Convert previous synthesis to text
    previous_text = f"""Introduction:
{previous_synthesis.introduction}

Why:
{previous_synthesis.why}

Quick Start:
{previous_synthesis.quick_start}

Architecture:
{previous_synthesis.architecture}

Key Concepts:
{previous_synthesis.key_concepts}

How-To Guides:
{chr(10).join(f"- {g.title}: {g.content}" for g in previous_synthesis.how_to_guides)}
"""
    
    suggestions_text = "\n".join(f"- {s}" for s in suggestions) if suggestions else "- None"
    
    return f"""You are improving synthesis documentation based on evaluation feedback.

## Evaluation Feedback:
{evaluation_feedback}

## Suggestions:
{suggestions_text}

## Repository Analysis:
{repo_analysis}

## Module Documentation:
{chr(10).join(f"- {m.get('module', '')}: {m.get('docstring', '')[:300]}..." for m in module_docs)}

## File Tree:
{file_tree}

## Previous Synthesis (to improve):
{previous_text}

## Original Generation Prompt (for reference):
{original_prompt}

## Instructions:
- Address the feedback and incorporate suggestions
- Keep accurate parts from the previous synthesis
- Ensure consistency with repository analysis and module docs
- Generate an improved synthesis that addresses the identified issues
- Follow the same structure and format as the original prompt requires
"""