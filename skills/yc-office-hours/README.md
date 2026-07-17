# YC Office Hours — Claude Code Skill

A Claude Code skill that runs structured business mentorship sessions modeled after Y Combinator partner office hours. Get direct, evidence-based feedback on business ideas, marketing campaigns, and go-to-market strategies.

Built from analysis of **19 YC partner videos** (Paul Graham, Sam Altman, Gustaf Alstromer, Kevin Hale, Des Traynor, and others) and inspired by [gstack](https://github.com/garrytan/gstack)'s office-hours and plan-ceo-review skill architecture.

## What It Does

Runs an 8-step mentorship session that challenges your assumptions and delivers a clear verdict:

1. **Opening** — "So, what are you working on?"
2. **Depth Ladder** — Escalating questions to peel away assumptions
3. **Deep Dive** — Mode-specific frameworks applied to your situation
4. **Premise Challenge** — Your core assumptions tested one by one
5. **Verdict** — PROCEED / TEST FIRST / PIVOT / KILL
6. **Action Plan** — One concrete, do-it-this-week assignment

### Three Modes

| Mode | Use When | Frameworks Applied |
|------|----------|-------------------|
| **IDEA** | Evaluating a new business concept | Problem Size x Frequency Matrix, Contrarian Insight Test, Founder-Market Fit, Schlep Blindness Scan |
| **GROWTH** | Scaling an existing business | PMF Evidence Demand, Revenue Per Employee, Consultancy Trap Test, Spending Discipline |
| **CAMPAIGN** | Reviewing a marketing campaign | One Core Message Rule, Audience Specificity Test, Channel-Market Fit, Content-First Audit |

### YC Partner Voice

The skill communicates like a YC partner — direct, evidence-demanding, anti-sycophantic. It will never say "interesting" or "you might consider." It takes positions.

## Installation

Copy the skill folder to your Claude Code skills directory:

```bash
# Clone
git clone https://github.com/crealwork/yc-office-hours.git

# Copy to Claude Code skills
cp -r yc-office-hours ~/.claude/skills/yc-office-hours
```

Or manually copy the 4 files into `~/.claude/skills/yc-office-hours/`:

```
~/.claude/skills/yc-office-hours/
├── SKILL.md              # Core workflow (8 steps)
├── question-bank.md      # 80+ questions organized by mode
├── evaluation-rubric.md  # Scoring frameworks and tarpit detection
└── partner-voice.md      # Communication style rules
```

## Usage

In Claude Code, type:

```
/yc-office-hours
```

Then describe your business idea, growth challenge, or marketing campaign.

## Key Frameworks

### From YC Partner Videos
- **Paul Graham's 8-Question Framework** — Naive opening, escalating depth, constraint hunting
- **Des Traynor's Problem Matrix** — 2x2 grid (Big/Small x Frequent/Rare) for instant viability filtering
- **Sam Altman's Contrarian Venn Diagram** — Ideas must sit at intersection of "viable" and "sounds bad"
- **Kevin Hale's UX Critique** — Live website teardowns, CTA clarity, volume calibration
- **"Doing Things That Don't Scale"** — Manual validation before automation

### From gstack Architecture
- Phase-based sequential workflow with AskUserQuestion gates
- Premise Challenge stage (one assumption at a time)
- Mandatory alternatives generation (never present only one option)
- Founder Signal tracking and scoring
- Anti-sycophancy communication rules

## Files

| File | Purpose | When Loaded |
|------|---------|-------------|
| `SKILL.md` | Core workflow — 8 steps, 3 modes, error handling | Always (on skill trigger) |
| `question-bank.md` | 80+ questions by mode/stage + action templates | Step 4 (Deep Dive) |
| `evaluation-rubric.md` | Problem Matrix, Signal Scorecard, Campaign Scorecard, Tarpits | Step 6 (Verdict) |
| `partner-voice.md` | Communication rules, banned phrases, questioning techniques | Step 1 (before first response) |

## Credits

- **YC Partners**: Paul Graham, Sam Altman, Gustaf Alstromer, Kevin Hale, Qasar Younis, Pete Koomen, Brad Flora, Nicolas Dessaigne, Des Traynor, and others whose office hours sessions informed the questioning frameworks
- **gstack** by Garry Tan: The office-hours and plan-ceo-review skill architecture that inspired the phased workflow structure
- **Claude Code Skill Spec**: [agentskills.io/specification](https://agentskills.io/specification)

## License

MIT
