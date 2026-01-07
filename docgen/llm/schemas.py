"""Pydantic schemas for structured LLM outputs."""

from pydantic import BaseModel, Field


class TechStack(BaseModel):
    """Technology stack identified in the repository."""
    languages: list[str] = Field(description="Programming languages (e.g., Python, TypeScript)")
    frameworks: list[str] = Field(description="Frameworks and libraries (e.g., FastAPI, React)")


class RepoSummary(BaseModel):
    """High-level summary of the repository."""
    purpose: str = Field(description="2-3 sentence summary of what this project does")
    tech_stack: TechStack
    

class Module(BaseModel):
    """A logical module/component in the repository."""
    name: str = Field(description="Descriptive module name (e.g., 'Code Analysis Engine')")
    description: str = Field(description="Brief description of the module's purpose")
    files: list[str] = Field(description="File paths belonging to this module")


class RepoAnalysis(BaseModel):
    """Complete repository analysis with structured summary and modules."""
    summary: RepoSummary
    modules: list[Module] = Field(description="3-8 logical modules grouping related files")


class RubricScore(BaseModel):
    """Individual rubric criterion score."""
    criterion: str = Field(description="Name of the criterion being evaluated")
    score: int = Field(description="Score 1-100 for this criterion", ge=1, le=100)
    feedback: str = Field(description="Specific feedback for this criterion")


class RepoAnalysisEvaluation(BaseModel):
    """Structured evaluation of repository analysis."""
    
    # Rubric scores (each 1-100)
    readability: RubricScore = Field(description="Is the analysis clear and well-structured?")
    component_allocation: RubricScore = Field(description="Are main components reasonably allocated to modules? Is there any redundant or missing components file?")
    no_duplicates: RubricScore = Field(description="Are there no duplicate/overly similar modules that should be combined?")
    completeness: RubricScore = Field(description="Are all important modules present? Nothing critical missing?")
    file_coverage: RubricScore = Field(description="Are all significant files assigned to exactly one module?")
    
    # Overall assessment
    overall_score: int = Field(description="Overall confidence score 1-100", ge=1, le=100)
    
    # Actionable feedback for next iteration
    suggestions: list[str] = Field(description="Concrete suggestions for improvement")


class Docstring(BaseModel):
    """A docstring for a function, class, file, or module."""
    docstring: str = Field(description="The docstring text. Should be plain text with no code blocks, no backticks, no markdown formatting. Keep it concise and comprehensive.")


class HowToGuide(BaseModel):
    """A how-to guide entry."""
    title: str = Field(description="Title of the how-to guide")
    content: str = Field(description="Step-by-step guide content")


class DocSubsection(BaseModel):
    """A subsection within a documentation section."""
    slug: str = Field(description="URL-friendly identifier (lowercase, hyphens)")
    title: str = Field(description="Subsection title")
    description: str = Field(description="Brief description (1 sentence)")


class DocSection(BaseModel):
    """A documentation section in the TOC with optional subsections."""
    slug: str = Field(description="URL-friendly identifier (lowercase, hyphens, e.g. 'quick-start')")
    title: str = Field(description="Human-readable section title (e.g. 'Quick Start')")
    description: str = Field(description="Brief description of what this section covers (1-2 sentences)")
    is_core: bool = Field(default=False, description="Whether this is a core section (Introduction, Quick Start, Architecture)")
    subsections: list[DocSubsection] = Field(default_factory=list, description="Optional nested subsections")


class ProposedTOC(BaseModel):
    """Proposed table of contents structure for documentation."""
    sections: list[DocSection] = Field(
        description="Ordered list of documentation sections with optional subsections. Include core sections (Introduction, Quick Start, Architecture) plus project-specific sections."
    )
    reasoning: str = Field(description="Brief explanation of why these sections were chosen based on the project type and codebase")


class SynthesisDoc(BaseModel):
    """Complete synthesis documentation for a repository."""
    introduction: str = Field(description="2-3 paragraph introduction explaining what this project is, who it's for, and what problems it solves. Be specific about capabilities and use cases.")
    why: str = Field(description="Explain the motivation behind this project. What problem does it solve? Why would someone choose this over alternatives? What are the key benefits?")
    quick_start: str = Field(description="Step-by-step instructions to get started with the project. Include installation, basic configuration, and a simple example. Use numbered steps.")
    architecture: str = Field(description="High-level architecture overview. Explain how the major components work together. Describe the data flow or processing pipeline if applicable.")
    key_concepts: str = Field(description="Define important terms, abstractions, and patterns used in the project. Help new users understand the mental model.")
    how_to_guides: list[HowToGuide] = Field(description="List of step-by-step guides for common use cases")


class DynamicSection(BaseModel):
    """A dynamically generated documentation section."""
    slug: str = Field(description="URL-friendly identifier matching the TOC")
    title: str = Field(description="Section title")
    content: str = Field(description="Full markdown content for this section")


class DynamicSynthesisDoc(BaseModel):
    """Dynamic synthesis documentation based on confirmed TOC."""
    sections: list[DynamicSection] = Field(description="Documentation sections in order matching the confirmed TOC")


class ConfidenceScore(BaseModel):
    """A confidence score from 1-100."""
    score: int = Field(description="Confidence score between 1 and 100", ge=1, le=100)


class DocstringEvaluation(BaseModel):
    """Structured evaluation of a docstring (function, class, file, or module).

    Based on docstring-specific quality criteria D1-D6 (adapted from Section 2.3):
    - D1: Clarity (Skaidrība) - easy to understand
    - D2: Actuality (Aktualitāte) - reflects current code state
    - D3: Structure (Struktūra) - well-organized sections (Args/Returns/Raises)
    - D4: Conciseness (Kodolīgums) - appropriate detail level, not verbose
    - D5: Precision (Precizitāte) - no hallucinations
    - D6: Consistency (Konsistence) - follows Google docstring style
    """

    # Rubric scores based on D1-D6 (each 1-100)
    clarity: RubricScore = Field(description="D1: Is the docstring clear and easy to understand without additional context?")
    actuality: RubricScore = Field(description="D2: Does the documentation accurately reflect the current code state (parameters, return types, behavior)?")
    structure: RubricScore = Field(description="D3: Is the docstring well-organized with clear sections (Args, Returns, Raises) in proper order?")
    conciseness: RubricScore = Field(description="D4: Is the docstring appropriately concise without being too brief or verbose?")
    precision: RubricScore = Field(description="D5: Is the technical information accurate with no hallucinations or invented details?")
    consistency: RubricScore = Field(description="D6: Does the docstring follow Google docstring style consistently?")

    # Overall assessment
    overall_score: int = Field(description="Overall quality score 1-100 (weighted average of D1-D6)", ge=1, le=100)

    # Actionable feedback for next iteration
    suggestions: list[str] = Field(description="Concrete suggestions for improvement based on lowest-scoring criteria")


class SynthesisEvaluation(BaseModel):
    """Structured evaluation of synthesis documentation (project-level).

    Based on synthesis-specific quality criteria S1-S6 (from Section 2.3):
    - S1: Clarity (Skaidrība) - clear and well-structured
    - S2: Actuality (Aktualitāte) - reflects current architecture
    - S3: Findability (Atrodamība) - navigation, cross-references
    - S4: Usefulness (Noderīgums) - practical value, getting started
    - S5: Precision (Precizitāte) - no hallucinations
    - S6: Consistency (Konsistence) - uniform terminology
    """

    # Rubric scores based on S1-S6 (each 1-100)
    clarity: RubricScore = Field(description="S1: Is the documentation clear and well-structured, easy to understand?")
    actuality: RubricScore = Field(description="S2: Does the documentation accurately reflect the current codebase architecture and features?")
    findability: RubricScore = Field(description="S3: Is information well-organized with clear navigation, sections, and cross-references?")
    usefulness: RubricScore = Field(description="S4: Does the documentation provide practical value for understanding and using the project?")
    precision: RubricScore = Field(description="S5: Is the technical information accurate with no hallucinations or fabricated details?")
    consistency: RubricScore = Field(description="S6: Does the documentation maintain consistent terminology, style, and formatting throughout?")

    # Overall assessment
    overall_score: int = Field(description="Overall quality score 1-100 (weighted average of S1-S6)", ge=1, le=100)

    # Actionable feedback for next iteration
    suggestions: list[str] = Field(description="Concrete suggestions for improvement based on lowest-scoring criteria")


class CodeExample(BaseModel):
    """A code example for a function."""
    code: str = Field(description="Standalone Python code example. Include necessary imports. No markdown code blocks.")


class CodeExampleValidation(BaseModel):
    """Validation result for a code example."""
    is_valid: bool = Field(description="Whether the example passes all validation checks")
    issues: list[str] = Field(
        default_factory=list,
        description="List of specific issues found, empty if valid"
    )


class ArchitectureComponent(BaseModel):
    """A component in the architecture diagram."""
    id: str = Field(description="Short identifier for the component (e.g., 'parser', 'llm_client')")
    name: str = Field(description="Display name for the component (e.g., 'Code Parser')")
    description: str = Field(description="One-sentence description of what this component does")


class ArchitectureDiagram(BaseModel):
    """Architecture diagram with Mermaid flowchart and component explanations."""
    mermaid: str = Field(description="Mermaid flowchart code (graph TB or graph LR). Use subgraphs for modules. Keep it simple with 5-15 nodes max.")
    components: list[ArchitectureComponent] = Field(description="List of components with brief explanations")
