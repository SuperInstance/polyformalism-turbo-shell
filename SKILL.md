---
name: polyformalism-turbo-shell
description: Multi-model creative cognition engine. Don this shell to think through multiple formalisms simultaneously. Includes neuroscience-informed debate protocol, salience routing, and insight detection.
---

# Polyformalism Turbo-Shell 🐚🔧

## What This Shell Does

Transforms any agent into a **creative cognition engine** that produces novel insights through multi-formalism thinking. Based on neuroscience research showing creativity requires dynamic switching between generative (DMN) and evaluative (ECN) networks.

**Any agent can don this shell.** No special training required. The shell provides the protocol, routing, and evaluation — the agent brings the content knowledge.

## Quick Start

```
# As an agent, to don this shell:
1. Read this SKILL.md
2. Follow the PROTOCOL for your assigned role
3. Use the ROUTING TABLE to decide which technique to use when
4. Use the INSIGHT DETECTION rubric to evaluate outputs
```

## The Neuroscience Basis (Why This Works)

Creativity in the brain requires:
1. **DMN (Default Mode Network)**: Spontaneous, generative, associative thinking
2. **ECN (Executive Control Network)**: Evaluative, analytical, constraint-checking
3. **Salience Network**: Routes between DMN and ECN based on task demands
4. **BVS (Brain Valuation System)**: Encodes subjective value = novelty × adequacy

**Key findings from N=2,433 study (Chen et al. 2025):**
- Dynamic DMN↔ECN switching predicts creativity (NOT intelligence)
- Inverted-U: moderate switching balance = optimal. Too much = rigid. Too little = noise.
- 3-5 rounds is the sweet spot

## The Protocol

### Phase 1: GENERATE (DMN mode)
- Use generative models or brainstorming techniques
- NO evaluation allowed — suppress the inner critic (hypofrontality)
- Produce 5-10 candidate ideas/concepts/solutions
- Use "ignorant-but-brilliant" perspective: approach as naive outsider

### Phase 2: ROUTE (Salience mode)
- The orchestrator selects which ideas are interesting (relevance detection)
- Flag 2-3 candidates for deeper exploration
- Assign evaluation techniques to each candidate

### Phase 3: EVALUATE (ECN mode)
- Apply devil's advocate critique to flagged candidates
- Check adequacy (correctness, feasibility, constraint satisfaction)
- Use formal verification where possible

### Phase 4: SYNTHESIZE (Integrated mode)
- Cross-reference surviving ideas across formalisms
- Detect insights that are ONLY visible when combining perspectives
- Apply valuation: novelty × adequacy → insight score

### Phase 5: STOP or ITERATE
- If insight score still rising AND rounds < 5 → go to Phase 1
- If agreement > 70% between evaluators → stop (past inverted-U peak)
- If insight score plateaued → stop

## Technique Selection (Routing Table)

| Situation | Technique | Brain Analog | What To Do |
|-----------|-----------|-------------|------------|
| Stuck, no ideas | Ignorant-but-Brilliant | DMN-only (hypofrontality) | Approach as total outsider, ask "dumb" questions |
| Too many weak ideas | Socratic Teacher | Salience → ECN | Ask probing questions that narrow the space |
| One dominant idea, no alternatives | Devil's Advocate | ECN conflict monitoring | Attack the idea from every angle |
| Clear goal, unclear path | Reverse Actualization | BVS reward recoding | Work backwards from the desired outcome |
| Converging too fast | Inject Contrarian | Salience intervention | Force a perspective 180° from current direction |

## Insight Detection Rubric

Score each output on two dimensions:

**Novelty (0-5):**
- 0: Exact restatement of input
- 1: Paraphrase of known concept
- 2: Novel combination of known elements
- 3: Genuinely new perspective on the problem
- 4: Discovers a hidden dimension not in the original framing
- 5: Redefines the problem itself

**Adequacy (0-5):**
- 0: Factually wrong
- 1: Vague direction, not actionable
- 2: Partially correct, needs significant refinement
- 3: Correct and actionable
- 4: Correct, actionable, and elegant
- 5: Correct, actionable, elegant, and generalizable

**Insight Score = α × Novelty + (1-α) × Adequacy**

Default α = 0.6 (slight novelty bias, based on neuroscience showing novelty-weighting produces more creative output).

## Multi-Model Orchestration

When multiple AI models are available:

| Role | Model Type | α Value | Example Models |
|------|-----------|---------|---------------|
| Generator | Fast, creative | 0.8 | DeepSeek-v4-flash, Seed-2.0-mini, Hermes-70B |
| Evaluator | Slow, precise | 0.3 | DeepSeek-v4-pro, Qwen3-397B |
| Orchestrator | Balanced | 0.5-0.6 | Any model with good routing |
| Valuer | Task-specific | 0.5 | Domain-specific model |

## The 3-Rewrite Rule

Minimum 3 rewrites through different formalisms before concluding:
1. Rewrite 1: Express in a formal notation (math, logic, code)
2. Rewrite 2: Express in a natural language with different structure (Chinese, Navajo, Finnish)
3. Rewrite 3: Express in a domain-specific language (music, architecture, cooking)

Each rewrite MUST produce at least one insight that the previous form could not express.

## Bundled Resources

- `references/neuroscience-synthesis.md` — Full neuroscience mapping
- `references/technique-guide.md` — Detailed technique instructions
- `scripts/route.py` — Automated salience routing script
- `scripts/insight-score.py` — Insight detection scorer
- `mcp/server.py` — MCP server for remote access

## Using as MCP Server

See `mcp/server.py` for the full MCP implementation. Exposes these tools:

1. `polyformalism_generate` — Generate ideas in DMN mode
2. `polyformalism_evaluate` — Evaluate ideas in ECN mode
3. `polyformalism_route` — Route to appropriate technique
4. `polyformalism_score` — Score insight quality
5. `polyformalism_debate` — Run full multi-round debate protocol
6. `polyformalism_linguistic` — Apply linguistic polyformalism (see linguistic-polyformalism-shell)

## Citation

If you use this shell in published work:
```
Digennaro, C. & Forgemaster (2026). Polyformalism Turbo-Shell: 
A neuroscience-informed multi-formalism creative cognition engine.
https://github.com/SuperInstance/polyformalism-turbo-shell
```
