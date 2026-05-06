# Polyformalism Turbo-Shell — MCP API Reference

Complete reference for the Model Context Protocol server.

## Installation

```bash
git clone https://github.com/SuperInstance/polyformalism-turbo-shell
cd polyformalism-turbo-shell
pip install mcp httpx
```

## Running the Server

### stdio transport (default — for Claude Desktop, OpenClaw)

```bash
python mcp/server.py
```

### SSE transport (for remote/web clients)

```bash
python mcp/server.py --transport sse --port 8080
```

### Claude Desktop Configuration

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

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

### OpenClaw Configuration

The shell can be used as an OpenClaw skill by placing it in your workspace skills directory:

```bash
cp -r polyformalism-turbo-shell ~/.openclaw/workspace/skills/
```

---

## Tools Reference

### `polyformalism_route`

Route to the appropriate polyformalism technique based on problem state.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `problem` | string | ✅ | The problem or concept being explored |
| `current_state` | string | ❌ | One of: `starting`, `stuck`, `too_many_ideas`, `one_dominant_idea`, `clear_goal_unclear_path`, `converging_too_fast` |

**State → Technique Mapping:**

| State | Technique | Brain Analog |
|-------|-----------|-------------|
| `starting` | Ignorant-but-Brilliant | DMN-only |
| `stuck` | Ignorant-but-Brilliant | DMN-only |
| `too_many_ideas` | Socratic Teacher | Salience → ECN |
| `one_dominant_idea` | Devil's Advocate | ECN conflict monitoring |
| `clear_goal_unclear_path` | Reverse Actualization | BVS reward recoding |
| `converging_too_fast` | Inject Contrarian | Salience intervention |

**Example:**

```python
result = await session.call_tool("polyformalism_route", {
    "problem": "Design a cache invalidation strategy for distributed systems",
    "current_state": "stuck"
})
# Returns: technique details + prompt template for generation
```

---

### `polyformalism_generate`

Generate ideas in DMN (generative) mode using a specific technique.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `problem` | string | ✅ | The problem to generate ideas for |
| `technique` | string | ❌ | One of: `ignorant_brilliant`, `socratic_teacher`, `devils_advocate`, `reverse_actualization`, `inject_contrarian` |
| `num_ideas` | integer | ❌ | Number of ideas to generate (default: 5) |

**Example:**

```python
result = await session.call_tool("polyformalism_generate", {
    "problem": "How to detect emerging systemic risks before they cascade",
    "technique": "ignorant_brilliant",
    "num_ideas": 7
})
# Returns: structured generation prompt + brain state + warning (don't evaluate yet)
```

---

### `polyformalism_evaluate`

Evaluate an idea in ECN (evaluative) mode.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `idea` | string | ✅ | The idea to evaluate |
| `constraints` | array\<string\> | ❌ | List of constraints to check against |

**Example:**

```python
result = await session.call_tool("polyformalism_evaluate", {
    "idea": "Use topological persistence diagrams to detect phase transitions in the risk landscape",
    "constraints": ["must work in real-time", "latency < 100ms", "false positive rate < 5%"]
})
# Returns: structured evaluation prompt + adequacy-focused scoring instructions
```

---

### `polyformalism_score`

Score an insight on novelty and adequacy dimensions.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `novelty` | integer | ✅ | 0-5 scale (0=restatement, 5=redefines the problem) |
| `adequacy` | integer | ✅ | 0-5 scale (0=wrong, 5=correct+elegant+generalizable) |
| `alpha` | float | ❌ | Novelty weight 0-1 (default: 0.6). Higher=more creative, lower=more precise |

**Scoring Formula:**

```
Insight Score = α × Novelty + (1-α) × Adequacy
```

**Recommended α values:**

| Use Case | α | Rationale |
|----------|---|-----------|
| Creative exploration | 0.7-0.8 | Maximize novel connections |
| General polyformalism | 0.6 | Balanced (default) |
| Engineering decisions | 0.3-0.4 | Prioritize correctness |
| Safety-critical systems | 0.1-0.2 | Adequacy dominates |

**Example:**

```python
result = await session.call_tool("polyformalism_score", {
    "novelty": 4,
    "adequacy": 3,
    "alpha": 0.6
})
# Returns: {"novelty": 4, "adequacy": 3, "alpha": 0.6, "insight_score": 3.4, "quality": "strong"}
```

---

### `polyformalism_debate`

Run a full multi-round polyformalism debate protocol.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `topic` | string | ✅ | The topic to debate/explore |
| `rounds` | integer | ❌ | Number of rounds (1-5, default: 3) |
| `models` | array\<string\> | ❌ | Model names for roles |

**Protocol Structure:**

```
For each round R:
  Phase A: GENERATE — all generator models produce ideas using rotating technique
  Phase B: EVALUATE — evaluator models critique and score all generated ideas

Final Phase: SYNTHESIZE — cross-reference surviving ideas across rounds
  Find insights ONLY visible when combining perspectives
```

**Stopping Criteria:**
- Pairwise agreement > 0.7 → stop (past inverted-U peak)
- Insight scores plateau → stop
- Round 5 maximum → stop

**Example:**

```python
result = await session.call_tool("polyformalism_debate", {
    "topic": "Design a self-evolving constraint system for autonomous vehicles",
    "rounds": 4,
    "models": ["claude-3.5-sonnet", "gpt-4o", "gemini-pro"]
})
# Returns: full protocol with round-by-round structure + stopping criteria
```

---

### `polyformalism_linguistic`

Apply linguistic polyformalism — solve a problem through different language-thinking constraints.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `problem` | string | ✅ | The problem to solve |
| `languages` | array\<string\> | ❌ | Language keys (default: complete cognitive set) |

**Available Languages:**

| Key | Language | Constraint Type |
|-----|----------|----------------|
| `ancient_greek` | Ancient Greek | Boundary |
| `classical_chinese` | Classical Chinese | Pattern |
| `navajo` | Navajo | Process Shape |
| `arabic` | Arabic | Deep Structure |
| `finnish` | Finnish | Instrument |
| `quechua` | Quechua | Knowledge Source |
| `korean` | Korean | Social Structure |

**Example:**

```python
result = await session.call_tool("polyformalism_linguistic", {
    "problem": "How should a distributed system handle partial failures?",
    "languages": ["ancient_greek", "navajo", "finnish"]
})
# Returns: structured experiment with per-language prompts + synthesis instructions
```

---

## Integration Patterns

### Pattern 1: CLI Wrapper

```bash
# Quick generation
python -c "
from mcp.server import *
import asyncio
result = asyncio.run(polyformalism_generate.ainvoke({
    'problem': 'My problem here',
    'technique': 'ignorant_brilliant'
}))
print(result)
"
```

### Pattern 2: Python Library

```python
from polyformalism import TurboShell

shell = TurboShell()

# Route to technique
route = shell.route("My problem", current_state="stuck")

# Generate ideas
ideas = shell.generate("My problem", technique=route.technique, num_ideas=5)

# Evaluate each idea
for idea in ideas:
    eval_result = shell.evaluate(idea, constraints=["constraint1", "constraint2"])
    score = shell.score(novelty=eval_result.novelty, adequacy=eval_result.adequacy)
    print(f"{idea}: {score}")
```

### Pattern 3: Multi-Agent Orchestration

```python
from polyformalism import Debate

debate = Debate(
    topic="Design constraint-aware scheduling for real-time systems",
    rounds=3,
    generators=["deepseek-flash", "seed-mini"],
    evaluators=["deepseek-pro"],
    synthesizer="qwen397"
)

results = await debate.run()

for round_result in results.rounds:
    print(f"Round {round_result.number}: {len(round_result.surviving_ideas)} ideas survive")
    
print(f"Final insights: {len(results.insights)}")
for insight in results.insights:
    print(f"  [{insight.quality}] {insight.text} (N={insight.novelty}, A={insight.adequacy})")
```

---

## Error Handling

The MCP server returns standard MCP error codes:

| Code | Meaning | Fix |
|------|---------|-----|
| -32600 | Invalid request | Check JSON format |
| -32601 | Method not found | Use exact tool names from this reference |
| -32602 | Invalid params | Check required parameters |
| 429 | Rate limited | Back off and retry |

---

## Performance

Based on internal benchmarks:

| Operation | Latency | Notes |
|-----------|---------|-------|
| `route` | < 1ms | Pure computation, no model call |
| `generate` | 2-30s | Depends on model used |
| `evaluate` | 2-30s | Depends on model used |
| `score` | < 1ms | Pure computation |
| `debate` | 30s-5min | N rounds × (generate + evaluate) + synthesize |
| `linguistic` | 10s-3min | N languages × generate + synthesize |

---

## Changelog

### v1.0.0 (2026-05-06)
- Initial release
- 6 MCP tools
- stdio and SSE transports
- Neuroscience-informed protocol
- Integration with linguistic-polyformalism-shell
