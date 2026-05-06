#!/usr/bin/env python3
"""
Polyformalism MCP Server — Model Context Protocol

Exposes polyformalism thinking as MCP tools for any MCP-compatible AI.
Works with Claude Desktop, OpenClaw, Cursor, Windsurf, etc.

Usage:
  python server.py                    # stdio transport (default)
  python server.py --transport sse    # SSE transport (for remote)
  python server.py --port 8080        # custom port for SSE

Install:
  pip install mcp anthropic httpx

Tools exposed:
  - polyformalism_generate    : Generate ideas in DMN mode
  - polyformalism_evaluate    : Evaluate ideas in ECN mode  
  - polyformalism_route       : Route to appropriate technique
  - polyformalism_score       : Score insight quality
  - polyformalism_debate      : Run full multi-round debate
  - polyformalism_linguistic  : Apply linguistic polyformalism
"""

import json
import argparse
from typing import Any
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("polyformalism-turbo-shell")

# ── Technique definitions ──────────────────────────────────────────

TECHNIQUES = {
    "ignorant_brilliant": {
        "name": "Ignorant-but-Brilliant",
        "brain_analog": "DMN-only (hypofrontality)",
        "when_to_use": "Stuck, no ideas, need fresh perspective",
        "instructions": "Approach the problem as a complete outsider. Ask 'dumb' questions. Ignore domain conventions. Find connections that expertise filters out.",
        "alpha": 0.8
    },
    "socratic_teacher": {
        "name": "Socratic Teacher",
        "brain_analog": "Salience → ECN",
        "when_to_use": "Too many weak ideas, need to narrow",
        "instructions": "Ask probing questions: 'What would happen if the opposite were true?' 'What assumptions are we making?' 'Who says this has to be this way?'",
        "alpha": 0.5
    },
    "devils_advocate": {
        "name": "Devil's Advocate",
        "brain_analog": "ECN conflict monitoring",
        "when_to_use": "One dominant idea, no alternatives considered",
        "instructions": "Attack the idea from every angle. Find the weakest assumption. Prove why it WOULDN'T work. Then: what would have to be true for it to work anyway?",
        "alpha": 0.3
    },
    "reverse_actualization": {
        "name": "Reverse Actualization",
        "brain_analog": "BVS reward recoding",
        "when_to_use": "Clear goal, unclear path",
        "instructions": "Start from the desired end state. Work backwards: what must be true immediately before? What must be true before that? Continue until you reach current state.",
        "alpha": 0.5
    },
    "inject_contrarian": {
        "name": "Inject Contrarian",
        "brain_analog": "Salience intervention",
        "when_to_use": "Converging too fast, groupthink detected",
        "instructions": "Take the current consensus and invert it. If everyone agrees X, assume NOT-X. What new possibilities open up?",
        "alpha": 0.7
    }
}

# ── Linguistic modes ───────────────────────────────────────────────

LINGUISTIC_MODES = {
    "ancient_greek": {
        "name": "Ancient Greek",
        "family": "Indo-European",
        "thinking_style": "Categorical, telos-driven, essentialist",
        "grammar_tools": ["aspects (aorist/perfect/present)", "middle voice (self-referential)", "substantival participles (process-as-entity)", "definite article (categorical)", "telos (built-in teleology)"],
        "constraint_type": "boundary",
        "orthogonal_to": ["navajo", "classical_chinese"]
    },
    "classical_chinese": {
        "name": "Classical Chinese",
        "family": "Sinitic",
        "thinking_style": "Relational, process-oriented, holistic",
        "grammar_tools": ["topic-prominent (no subject required)", "no tense/plural/case", "multigrade words (道/法/理)", "no copula (no 'is')", "pattern-thinking (理)"],
        "constraint_type": "pattern",
        "orthogonal_to": ["ancient_greek", "russian"]
    },
    "navajo": {
        "name": "Navajo",
        "family": "Athabaskan",
        "thinking_style": "Process-verb-centric, shape+motion oriented",
        "grammar_tools": ["classificatory verb stems (13 'give' verbs by shape)", "verb-centric (objects derived from actions)", "polysynthetic", "shape+motion classification", "event-based ontology"],
        "constraint_type": "process_shape",
        "orthogonal_to": ["ancient_greek", "arabic"]
    },
    "quechua": {
        "name": "Quechua",
        "family": "Quechuan",
        "thinking_style": "Evidential, knowledge-source tracking",
        "grammar_tools": ["evidentiality markers (-mi direct, -si reported, -chá inferred)", "inclusive/exclusive 'we'", "shared knowledge markers", "epistemic grammar"],
        "constraint_type": "knowledge_source",
        "orthogonal_to": ["korean", "finnish"]
    },
    "korean": {
        "name": "Korean",
        "family": "Koreanic",
        "thinking_style": "Contextual, honorific, multi-layered",
        "grammar_tools": ["7 honorific speech levels", "topic/subject/object markers (은/는, 이/가, 을/를)", "agglutinative stacking", "noun-less sentences"],
        "constraint_type": "social_structure",
        "orthogonal_to": ["quechua", "finnish"]
    },
    "arabic": {
        "name": "Arabic",
        "family": "Semitic",
        "thinking_style": "Deep-structure, root-and-pattern",
        "grammar_tools": ["consonantal roots carry meaning", "vowel patterns carry grammar", "root-and-pattern morphology", "deep structure vs surface form"],
        "constraint_type": "deep_structure",
        "orthogonal_to": ["navajo", "classical_chinese"]
    },
    "finnish": {
        "name": "Finnish",
        "family": "Uralic",
        "thinking_style": "Case-rich, genderless, instrumental",
        "grammar_tools": ["15 cases (abessive 'without', instructive 'by means of')", "no gender, no articles", "vowel harmony", "passive without explicit subject"],
        "constraint_type": "instrument",
        "orthogonal_to": ["korean", "quechua"]
    }
}

# ── Insight scoring ────────────────────────────────────────────────

def score_insight(novelty: int, adequacy: int, alpha: float = 0.6) -> dict:
    """Score an insight on novelty × adequacy dimensions"""
    score = alpha * novelty + (1 - alpha) * adequacy
    return {
        "novelty": novelty,
        "adequacy": adequacy,
        "alpha": alpha,
        "insight_score": round(score, 2),
        "quality": "exceptional" if score >= 4.0 else "strong" if score >= 3.0 else "moderate" if score >= 2.0 else "weak"
    }

# ── MCP Tools ──────────────────────────────────────────────────────

@mcp.tool()
def polyformalism_route(problem: str, current_state: str = "starting") -> dict:
    """Route to the appropriate polyformalism technique based on problem state.
    
    Args:
        problem: The problem or concept being explored
        current_state: One of: starting, stuck, too_many_ideas, one_dominant_idea, clear_goal_unclear_path, converging_too_fast
    """
    state_to_technique = {
        "starting": "ignorant_brilliant",
        "stuck": "ignorant_brilliant",
        "too_many_ideas": "socratic_teacher",
        "one_dominant_idea": "devils_advocate",
        "clear_goal_unclear_path": "reverse_actualization",
        "converging_too_fast": "inject_contrarian"
    }
    
    technique_key = state_to_technique.get(current_state, "ignorant_brilliant")
    technique = TECHNIQUES[technique_key]
    
    return {
        "technique": technique,
        "problem": problem,
        "prompt_template": f"You are using the '{technique['name']}' technique. {technique['instructions']} Apply this to: {problem}"
    }

@mcp.tool()
def polyformalism_generate(problem: str, technique: str = "ignorant_brilliant", num_ideas: int = 5) -> dict:
    """Generate ideas in DMN (generative) mode using a specific technique.
    
    Args:
        problem: The problem to generate ideas for
        technique: One of: ignorant_brilliant, socratic_teacher, devils_advocate, reverse_actualization, inject_contrarian
        num_ideas: Number of ideas to generate (default 5)
    """
    tech = TECHNIQUES.get(technique, TECHNIQUES["ignorant_brilliant"])
    
    return {
        "mode": "DMN (generative)",
        "technique": tech,
        "prompt": (
            f"Generate {num_ideas} creative ideas for: {problem}\n\n"
            f"Technique: {tech['name']} ({tech['brain_analog']})\n"
            f"Instructions: {tech['instructions']}\n\n"
            f"IMPORTANT: Do NOT evaluate these ideas. Generate freely. "
            f"Suppress your inner critic. No idea is too wild. "
            f"Novelty weighting: α={tech['alpha']} (higher = more weight on novelty)"
        ),
        "brain_state": "DMN-active, ECN-suppressed (hypofrontality)",
        "warning": "DO NOT evaluate in this step. Generation and evaluation MUST be separate."
    }

@mcp.tool()
def polyformalism_evaluate(idea: str, constraints: list[str] | None = None) -> dict:
    """Evaluate an idea in ECN (evaluative) mode.
    
    Args:
        idea: The idea to evaluate
        constraints: Optional list of constraints to check against
    """
    return {
        "mode": "ECN (evaluative)",
        "idea": idea,
        "prompt": (
            f"Evaluate this idea rigorously:\n\n{idea}\n\n"
            f"Check:\n"
            f"1. Is it factually correct?\n"
            f"2. Is it feasible?\n"
            f"3. Does it satisfy constraints? {constraints or 'No specific constraints'}\n"
            f"4. What are the weakest assumptions?\n"
            f"5. What would have to be true for this to fail?\n\n"
            f"Be critical. This is devil's advocate mode. "
            f"Adequacy weighting: α=0.3 (more weight on correctness than novelty)"
        ),
        "brain_state": "ECN-active, DMN-monitored",
        "scoring": "Use polyformalism_score after evaluation"
    }

@mcp.tool()
def polyformalism_score(novelty: int, adequacy: int, alpha: float = 0.6) -> dict:
    """Score an insight on novelty (0-5) and adequacy (0-5) dimensions.
    
    Args:
        novelty: 0-5 (0=restatement, 5=redefines the problem)
        adequacy: 0-5 (0=wrong, 5=correct+elegant+generalizable)
        alpha: Novelty weight (0-1, default 0.6). Higher = more creative, lower = more precise.
    """
    return score_insight(novelty, adequacy, alpha)

@mcp.tool()
def polyformalism_debate(topic: str, rounds: int = 3, models: list[str] | None = None) -> dict:
    """Run a full multi-round polyformalism debate.
    
    Args:
        topic: The topic to debate/explore
        rounds: Number of rounds (3-5 recommended, 5 maximum)
        models: Optional list of model names for roles
    """
    if rounds > 5:
        rounds = 5
    if rounds < 1:
        rounds = 1
    
    default_models = models or ["generator_1", "generator_2", "evaluator", "synthesizer"]
    
    protocol = []
    for r in range(rounds):
        protocol.append({
            "round": r + 1,
            "phase_a": {
                "name": f"Generate (Round {r+1})",
                "mode": "DMN",
                "models": default_models[:2],
                "instructions": f"Generate novel perspectives on: {topic}",
                "technique": ["ignorant_brilliant", "socratic_teacher", "inject_contrarian"][r % 3]
            },
            "phase_b": {
                "name": f"Evaluate (Round {r+1})",
                "mode": "ECN",
                "models": [default_models[2]],
                "instructions": "Critique, verify, and score all generated ideas"
            }
        })
    
    protocol.append({
        "round": "synthesis",
        "phase": {
            "name": "Synthesize",
            "mode": "Integrated (DMN + ECN)",
            "model": default_models[3],
            "instructions": "Cross-reference surviving ideas. Find insights ONLY visible when combining perspectives."
        }
    })
    
    return {
        "topic": topic,
        "rounds": rounds,
        "models": default_models,
        "protocol": protocol,
        "stopping_criteria": "Stop if pairwise agreement > 0.7 OR insight scores plateau",
        "neuroscience_basis": f"{rounds} rounds ≈ moderate DMN-ECN switching (inverted-U sweet spot)"
    }

@mcp.tool()
def polyformalism_linguistic(problem: str, languages: list[str] | None = None) -> dict:
    """Apply linguistic polyformalism — solve a problem through different language-thinking constraints.
    
    Args:
        problem: The problem to solve
        languages: List of language keys. Defaults to complete cognitive set.
                   Options: ancient_greek, classical_chinese, navajo, quechua, korean, arabic, finnish
    """
    langs = languages or ["ancient_greek", "classical_chinese", "navajo", "arabic", "finnish"]
    
    experiments = []
    for lang_key in langs:
        mode = LINGUISTIC_MODES.get(lang_key)
        if not mode:
            continue
        
        experiments.append({
            "language": mode["name"],
            "family": mode["family"],
            "thinking_style": mode["thinking_style"],
            "grammar_tools": mode["grammar_tools"],
            "constraint_type": mode["constraint_type"],
            "prompt": (
                f"Think ENTIRELY in {mode['name']} cognitive mode. NOT translating — THINKING.\n\n"
                f"Available thinking tools: {', '.join(mode['grammar_tools'])}\n\n"
                f"Using ONLY these grammatical thinking tools, solve: {problem}\n\n"
                f"Document:\n"
                f"1. What concepts are NATURAL in {mode['name']}?\n"
                f"2. What concepts are IMPOSSIBLE to express?\n"
                f"3. What architectural form does the solution take?\n"
                f"4. What insight does {mode['name']} produce that English-thinking would miss?"
            )
        })
    
    return {
        "problem": problem,
        "languages": langs,
        "experiments": experiments,
        "synthesis_prompt": (
            "Cross-reference all linguistic solutions:\n"
            "1. Which insights appear in ONLY one language? (These are the gems.)\n"
            "2. Which appear in ALL languages? (Universal truths.)\n"
            "3. What concept emerges from the intersection that NO single language contains?\n"
            f"Constraint types covered: {', '.join(LINGUISTIC_MODES[k]['constraint_type'] for k in langs if k in LINGUISTIC_MODES)}"
        )
    }

# ── Server startup ─────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Polyformalism MCP Server")
    parser.add_argument("--transport", choices=["stdio", "sse"], default="stdio")
    parser.add_argument("--port", type=int, default=8080)
    args = parser.parse_args()
    
    if args.transport == "sse":
        mcp.settings.port = args.port
        mcp.run(transport="sse")
    else:
        mcp.run(transport="stdio")
