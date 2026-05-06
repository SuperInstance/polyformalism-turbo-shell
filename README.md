# Polyformalism Turbo-Shell 🐚🔧

**A neuroscience-informed MCP server that turns any AI agent into a creative cognition engine.**

Multi-formalism creative thinking, backed by real brain network research. Your agent generates ideas, evaluates them, routes between techniques, and scores insights — all through a structured protocol that mirrors how the human brain actually produces creative breakthroughs.

## Why It Works

Creative cognition isn't magic — it's a measurable brain state. Research from a 2,433-subject study (Chen et al., 2025) showed that **dynamic switching between the Default Mode Network (DMN) and Executive Control Network (ECN)** predicts creative output better than intelligence. The key insight: moderate switching produces optimal results. Too much switching → rigidity. Too little → noise.

This shell operationalizes that finding as a protocol:

| Brain Network | Mode | What It Does | Shell Phase |
|--------------|------|-------------|-------------|
| DMN | Generative | Free association, wild ideas | GENERATE |
| Salience Network | Routing | Detects what's worth exploring | ROUTE |
| ECN | Evaluative | Critical analysis, constraint checking | EVALUATE |
| Brain Valuation System | Scoring | Novelty × Adequacy → value | SYNTHESIZE |

The Brain Valuation System (BVS) encodes subjective value as `novelty × adequacy` — the same formula this shell uses for insight scoring.

**Key references:**
- Chen et al. (2025). Dynamic reconfiguration of DMN and ECN during creative thinking. *Nature Communications*. N=2,433.
- Beaty et al. (2016). Creativity and the default network. *Current Opinion in Neurobiology*.
- Moreno-Rodriguez et al. (2024). Salience network gating in creative ideation.

## Quick Start

### 1. MCP Client (Claude Desktop, Cursor, etc.)

Add to your MCP config:

```json
{
  "mcpServers": {
    "polyformalism": {
      "command": "python",
      "args": ["/path/to/polyformalism-turbo-shell/mcp/server.py"]
    }
  }
}
```

Then ask your AI: *"Use polyformalism_debate to explore whether REST APIs are fundamentally limited for real-time systems."*

### 2. Python Import

```python
from mcp.server.fastmcp import FastMCP
# Or use the scoring function directly:
from mcp_server import score_insight

result = score_insight(novelty=4, adequacy=3, alpha=0.6)
# → {"insight_score": 3.60, "quality": "strong"}
```

### 3. CLI (stdio)

```bash
pip install mcp anthropic httpx
python mcp/server.py                    # stdio transport
python mcp/server.py --transport sse    # SSE transport on port 8080
python mcp/server.py --transport sse --port 3000
```

## Architecture

```
┌──────────────────────────────────────────────────────────┐
│                   MCP Client (any AI)                     │
│              Claude / Cursor / OpenClaw / etc.            │
└──────────────┬───────────────────────────────┬───────────┘
               │                               │
    ┌──────────▼──────────┐         ┌──────────▼──────────┐
    │   polyformalism_    │         │   polyformalism_    │
    │     generate()      │         │     evaluate()      │
    │                     │         │                     │
    │  DMN Mode: free     │         │  ECN Mode: critical │
    │  association, wild  │         │  analysis, constraint│
    │  ideas, no filter   │         │  checking, devil's  │
    │                     │         │  advocate           │
    └──────────┬──────────┘         └──────────┬──────────┘
               │                               │
    ┌──────────▼───────────────────────────────▼───────────┐
    │                polyformalism_route()                  │
    │                                                       │
    │   Salience Network: detects which ideas are worth     │
    │   pursuing, selects technique, assigns α weight       │
    └───────────────────────────┬──────────────────────────┘
                                │
               ┌────────────────▼────────────────┐
               │       polyformalism_score()      │
               │                                  │
               │   BVS: novelty × adequacy →      │
               │   insight score (0-5 scale)      │
               └────────────────┬─────────────────┘
                                │
               ┌────────────────▼─────────────────┐
               │      polyformalism_debate()       │
               │                                  │
               │   Orchestrates full multi-round   │
               │   protocol: generate → evaluate   │
               │   → route → score → iterate       │
               └──────────────────────────────────┘
```

## MCP Tools Reference

### `polyformalism_generate`

Generate ideas in DMN (generative) mode.

```python
polyformalism_generate(
    problem="How to handle backpressure in distributed event streams",
    technique="ignorant_brilliant",  # ignorant_brilliant | socratic_teacher | devils_advocate | reverse_actualization | inject_contrarian
    num_ideas=5
)
```

Returns a structured prompt in DMN mode with the selected technique's instructions and novelty weighting (α). **Never evaluates — generation and evaluation must be separate.**

### `polyformalism_evaluate`

Evaluate an idea in ECN (evaluative) mode.

```python
polyformalism_evaluate(
    idea="Use a token-bucket per consumer with adaptive drain rate",
    constraints=["latency < 100ms", "no single point of failure"]
)
```

Returns a critical analysis prompt checking correctness, feasibility, constraint satisfaction, and failure modes. Adequacy-weighted (α=0.3).

### `polyformalism_route`

Route to the appropriate technique based on your current state.

```python
polyformalism_route(
    problem="Database schema for polymorphic event storage",
    current_state="one_dominant_idea"  # starting | stuck | too_many_ideas | one_dominant_idea | clear_goal_unclear_path | converging_too_fast
)
```

State-to-technique mapping:

| State | Technique | Brain Analog |
|-------|-----------|-------------|
| `starting` / `stuck` | Ignorant-but-Brilliant | DMN hypofrontality |
| `too_many_ideas` | Socratic Teacher | Salience → ECN |
| `one_dominant_idea` | Devil's Advocate | ECN conflict monitoring |
| `clear_goal_unclear_path` | Reverse Actualization | BVS reward recoding |
| `converging_too_fast` | Inject Contrarian | Salience intervention |

### `polyformalism_score`

Score an insight on novelty (0-5) and adequacy (0-5).

```python
polyformalism_score(novelty=4, adequacy=3, alpha=0.6)
# → {"insight_score": 3.60, "quality": "strong"}
```

**Novelty scale:**

| Score | Meaning |
|-------|---------|
| 0 | Exact restatement of input |
| 1 | Paraphrase of known concept |
| 2 | Novel combination of known elements |
| 3 | Genuinely new perspective |
| 4 | Discovers a hidden dimension |
| 5 | Redefines the problem itself |

**Adequacy scale:**

| Score | Meaning |
|-------|---------|
| 0 | Factually wrong |
| 1 | Vague, not actionable |
| 2 | Partially correct, needs work |
| 3 | Correct and actionable |
| 4 | Correct, actionable, elegant |
| 5 | Correct, actionable, elegant, generalizable |

### `polyformalism_debate`

Run a full multi-round debate protocol with multiple model roles.

```python
polyformalism_debate(
    topic="Should microservices communicate via events or RPC?",
    rounds=3,
    models=["gpt-4", "claude-3", "deepseek-pro", "qwen-397b"]
)
```

Returns a structured protocol with generate/evaluate phases per round, plus a final synthesis phase. Rounds capped at 5 (inverted-U sweet spot from neuroscience).

**Stopping criteria:** Pairwise agreement > 0.7 OR insight scores plateau.

### `polyformalism_linguistic`

Apply linguistic polyformalism — solve a problem through different language-thinking constraints.

```python
polyformalism_linguistic(
    problem="What is a constraint?",
    languages=["ancient_greek", "navajo", "finnish"]
)
```

See the [linguistic-polyformalism-shell](https://github.com/SuperInstance/linguistic-polyformalism-shell) for the full cross-linguistic protocol.

## The 5-Phase Protocol

```
Phase 1: GENERATE (DMN)
    │   Produce 5-10 candidate ideas
    │   NO evaluation — suppress the inner critic
    │   Use "ignorant-but-brilliant" perspective
    ▼
Phase 2: ROUTE (Salience)
    │   Select 2-3 promising candidates
    │   Assign evaluation techniques
    │   Set α weight per technique
    ▼
Phase 3: EVALUATE (ECN)
    │   Devil's advocate critique
    │   Check adequacy and feasibility
    │   Apply formal verification where possible
    ▼
Phase 4: SYNTHESIZE (Integrated)
    │   Cross-reference across formalisms
    │   Detect insights ONLY visible from combined perspectives
    │   Score: novelty × adequacy → insight value
    ▼
Phase 5: STOP or ITERATE
    │   Score rising + rounds < 5? → Phase 1
    │   Agreement > 70%? → Stop
    │   Scores plateaued? → Stop
    └──► Output final insights
```

## Insight Scoring Math

```
Insight Score = α × Novelty + (1 - α) × Adequacy

Where:
  α ∈ [0, 1]    — novelty weight (default 0.6)
  Novelty ∈ [0, 5]  — how new is this idea?
  Adequacy ∈ [0, 5] — how correct/useful is this idea?
```

The default α=0.6 slightly favors novelty, based on neuroscience showing novelty-weighted valuation produces more creative output (Chen et al., 2025).

**Quality bands:**

| Score | Quality |
|-------|---------|
| ≥ 4.0 | Exceptional |
| ≥ 3.0 | Strong |
| ≥ 2.0 | Moderate |
| < 2.0 | Weak |

## Multi-Model Orchestration

Different models have different strengths. Map them to roles:

| Role | Model Characteristics | α Value | Example Models |
|------|----------------------|---------|---------------|
| Generator | Fast, creative, broad | 0.8 | DeepSeek-flash, GPT-4o-mini, Llama-70B |
| Evaluator | Slow, precise, thorough | 0.3 | DeepSeek-reasoner, Claude Opus, Qwen-397B |
| Orchestrator | Balanced, good routing | 0.5-0.6 | Any capable model |
| Valuer | Domain-specific expertise | 0.5 | Domain-tuned models |

**Example setup with 4 models:**

```python
polyformalism_debate(
    topic="Design a constraint specification language",
    rounds=3,
    models=[
        "deepseek-flash",      # Generator 1 (fast, creative)
        "qwen-72b",            # Generator 2 (different perspective)
        "deepseek-reasoner",   # Evaluator (slow, precise)
        "claude-sonnet"        # Synthesizer (balanced)
    ]
)
```

## Configuration

### Transport Options

| Transport | Use Case | Command |
|-----------|----------|---------|
| stdio | Local MCP client (default) | `python server.py` |
| SSE | Remote/HTTP access | `python server.py --transport sse` |
| SSE + custom port | Custom deployment | `python server.py --transport sse --port 3000` |

### Dependencies

```
pip install mcp anthropic httpx
```

### Custom α Values

Pass `alpha` to `polyformalism_score` to tune the novelty/adequacy balance:

```python
# Heavily favor novelty (exploration mode)
polyformalism_score(novelty=5, adequacy=2, alpha=0.8)  # → 4.40

# Heavily favor adequacy (production mode)
polyformalism_score(novelty=5, adequacy=2, alpha=0.2)  # → 2.60

# Balanced (default)
polyformalism_score(novelty=5, adequacy=2, alpha=0.6)  # → 3.80
```

## Integration with Linguistic Polyformalism

The turbo-shell pairs with the [linguistic-polyformalism-shell](https://github.com/SuperInstance/linguistic-polyformalism-shell) for cross-linguistic insight production:

- **Turbo-shell** provides multi-model orchestration, technique routing, and insight scoring
- **Linguistic-shell** provides 14 human-language formalisms across 7 language families
- **Combined**: multi-model debate through human linguistic constraints

Use `polyformalism_linguistic` to invoke the linguistic protocol from within the turbo-shell, or install both shells and use them independently.

## The 3-Rewrite Rule

Before concluding any creative exploration, rewrite the result through three different formalisms:

1. **Formal notation** — Express in math, logic, or code
2. **Different language structure** — Express in a language with fundamentally different grammar (Chinese, Navajo, Finnish)
3. **Domain-specific language** — Express in an alien domain (music, architecture, cooking)

Each rewrite must produce at least one insight the previous form could not express. If it doesn't, you haven't genuinely changed formalisms — you've just translated.

## FAQ

**Q: Does this actually work, or is it just prompt engineering?**
It's structured prompt engineering grounded in neuroscience. The DMN/ECN switching pattern is real (N=2,433 study). The insight scoring formula (novelty × adequacy) mirrors actual brain valuation. The techniques map to specific brain network states. The 3-5 round sweet spot comes from the inverted-U relationship observed in the data.

**Q: Why is generation and evaluation separate?**
Because the brain does it that way. The DMN generates freely; the ECN evaluates critically. Activating both simultaneously produces mediocre output. The "hypofrontality" finding shows that suppressing the prefrontal cortex (your inner critic) during generation produces more creative ideas.

**Q: What's the inverted-U?**
The Chen et al. study found a non-linear relationship between DMN↔ECN switching frequency and creative output. Moderate switching = peak creativity. Too much switching = rigid, analytical output. Too little = random, unstructured output. That's why the protocol caps at 5 rounds.

**Q: Can I use this with a single model?**
Yes. The multi-model setup is optional. A single model can play all roles — generate, then switch to evaluate, then synthesize. Multiple models just provide more diverse perspectives.

**Q: What makes this different from brainstorming?**
Structure and scoring. Traditional brainstorming has no routing (what technique to use when), no scoring (how good is each idea), and no stopping criteria (when to stop). This shell adds all three, grounded in how the brain actually works.

**Q: What's a "shell"?**
A shell is an agent-downloadable skill package. Any AI agent can "don" this shell by reading the SKILL.md and following the protocol. The MCP server makes it accessible to any MCP-compatible client.

## Citation

```bibtex
@misc{digennaro2026polyformalism,
  author = {Digennaro, Casey and Forgemaster},
  title = {Polyformalism Turbo-Shell: A neuroscience-informed multi-formalism creative cognition engine},
  year = {2026},
  url = {https://github.com/SuperInstance/polyformalism-turbo-shell}
}
```

## License

MIT

## Links

- **Sister repo:** [linguistic-polyformalism-shell](https://github.com/SuperInstance/linguistic-polyformalism-shell) — Cross-linguistic insight production
- **Key reference:** Chen et al. (2025). Dynamic reconfiguration of large-scale brain networks during creative thinking. *Nature Communications*.
- **Key reference:** Beaty et al. (2016). Creativity and the default network: A functional connectivity perspective. *Current Opinion in Neurobiology*.
