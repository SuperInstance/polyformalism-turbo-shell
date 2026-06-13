# Polyformalism Turbo-Shell

**Polyformalism Turbo-Shell** is a neuroscience-informed MCP server that turns any AI agent into a creative cognition engine — alternating between Default Mode Network (DMN) and Executive Control Network (ECN) techniques at a calibrated frequency to produce optimal creative output.

## Why It Matters

Research from a 2,433-subject study (Chen et al., 2025) showed that **dynamic switching between the DMN and ECN** predicts creative output better than intelligence. The key finding: moderate switching frequency produces optimal results — too much switching causes rigidity, too little produces noise. Turbo-Shell operationalizes this research by providing seven creative cognitive states that map to brain network activation patterns, allowing any AI agent to produce structured creative thinking rather than random brainstorming.

## How It Works

### The 7 Creative Cognitive States

Each state maps to a specific brain network and creative technique:

| State | Network | Technique | Operation |
|-------|---------|-----------|-----------|
| Generate | DMN | Divergent | Produce many ideas |
| Associate | DMN | Analogical | Connect distant domains |
| Hybridize | DMN | Combination | Merge unrelated concepts |
| Constrain | ECN | Inversion | Identify what's impossible |
| Evaluate | ECN | Critical | Score and filter |
| Refine | ECN | Elaboration | Develop promising ideas |
| Route | Salience | Meta-cognition | Switch between networks |

### DMN-ECN Switching

The optimal switching frequency follows an inverted-U curve:

```
Creativity(frequency) = α·f - β·f²   (optimal at f = α/(2β))
```

Too high frequency (>4 switches/min): cognitive rigidity, no deep exploration.
Too low frequency (<0.5 switches/min): noise without evaluation.
Optimal: ~1-2 switches/min — matching measured brain dynamics in highly creative subjects.

### MCP Protocol

The server exposes creative operations via MCP (Model Context Protocol):

```python
# Server runs as an MCP server (server.py)
# Agents call creative operations as MCP tools
```

Each operation generates, evaluates, or routes ideas through the 7-state cycle.

### Insight Scoring

Ideas are scored on novelty (distance from known solutions), usefulness (constraint satisfaction), and surprise (entropy relative to expectations):

```
insight = w₁·novelty + w₂·usefulness + w₃·surprise
```

Weights are calibrated per domain. Scoring: **O(N)** where N = number of constraint dimensions.

## Quick Start

```bash
# Start the MCP server
cd polyformalism-turbo-shell
python3 mcp/server.py

# In your agent configuration, add the MCP server endpoint
# The server exposes creative cognition tools to any connected agent
```

```python
# Example MCP tool call (from connected agent)
# generate(domain="architecture", constraints=["sustainable", "modular"])
# → returns divergent ideas scored by insight potential
```

## API

| Component | Description |
|-----------|-------------|
| `mcp/server.py` | MCP server exposing 7 creative cognitive operations |
| `docs/API-REFERENCE.md` | Full API documentation |
| `docs/FUTURE-INTEGRATION.md` | Integration roadmap |
| `SKILL.md` | Skill definition for agent integration |
| `EILEEN-VERSION-KIMI-NEGATIVE-SPACE.md` | Negative space variant configuration |

## Architecture Notes

Polyformalism Turbo-Shell provides the creative cognition layer in the SuperInstance ecosystem. In γ + η = C, DMN states (generate, associate, hybridize) drive γ (growth — exploring new idea spaces) while ECN states (constrain, evaluate, refine) provide η (avoidance — rejecting ideas that violate constraints). The salience network's routing function implements the balance between exploration and avoidance. Integrates with `negative-space-core` for avoidance-based idea filtering.

See [ARCHITECTURE.md](https://github.com/SuperInstance/SuperInstance/blob/main/ARCHITECTURE.md) for cognitive architecture.

## References

1. Chen, Q. et al. (2025). "Dynamic network switching predicts creative thinking." *Nature Human Behaviour*.
2. Beaty, R. E. et al. (2018). "Robust prediction of individual creative ability from brain functional connectivity." *PNAS*, 115(5), 1087–1092.
3. Jung, R. E. et al. (2010). "The structure of creative cognition in the human brain." *Frontiers in Human Neuroscience*, 4, 16.

## License

MIT
