# Fintech Dashboard Skill

An agent skill for building a mobile-first fintech dashboard and banking
app — balance, transactions and receipts, transfers with PIN confirmation,
linked cards, buy-only stocks, and tiered identity verification.

It is global and currency-agnostic: pick one currency once, store amounts
in the smallest unit, and format every amount from the same helper. It
works for any country. Money is simulated unless the project explicitly
says it moves real money.

## Who it is for

- Developers building a banking app, neobank, or money app with a
  coding agent
- Developers adding transfers, cards, stocks, verification tiers, or
  receipts to an existing finance app
- Anyone who wants a fintech build that follows the same rules every
  time: plan first, one money model, PIN before sending, never store
  full card or ID numbers, and verify production, not only preview

## What is inside

- `fintech-dashboard/SKILL.md` — the skill itself: a step-by-step
  procedure, checklists, common mistakes, and what not to do
- `fintech-dashboard/references/` — short files loaded on demand:
  dashboard, transfers, cards and stocks, verification and security,
  testing
- `fintech-dashboard/examples/transaction-receipt.md` — a worked
  receipt example, with success, failure, and wrong-PIN versions
- `fintech-dashboard/scripts/check-skill.py` — validates the skill
  before you publish it

The patterns in this skill were proven in a real build: a mobile-first
neobank simulation in TypeScript and Next.js, with a balance card and
hide-balance toggle, a portfolio donut, buy-only stocks, an external
bank picker with real brand logos, PIN confirmation before sending,
linked cards, and three verification tiers with daily limits. That
implementation is one example. The skill itself is not tied to it.

## Install

### Claude Code

Personal, available in every project:

```sh
mkdir -p ~/.claude/skills
cp -r fintech-dashboard ~/.claude/skills/
```

Project only, shared with the team:

```sh
mkdir -p .claude/skills
cp -r fintech-dashboard .claude/skills/
```

Restart Claude Code, then ask it to build a fintech dashboard. It
will load the skill when the request matches the description.

### Codex

Codex supports the same Agent Skills open standard. Copy the
`fintech-dashboard` folder into the skills directory Codex reads
for your setup, then restart Codex.

### Copilot

Copilot supports Agent Skills in the same format. Copy the
`fintech-dashboard` folder into the skills directory for your
Copilot setup, then restart Copilot.

### Verify the install

```sh
python3 fintech-dashboard/scripts/check-skill.py
```

It should print `PASSED: all checks passed`.

## Example prompts

Try these after installing:

- "Build a fintech dashboard with a balance card, recent activity, and a hide-balance toggle."
- "Add bank transfers with a bank picker, PIN confirmation, and a receipt."
- "Add linked cards with freeze, and show full card details only after a PIN check."
- "Add buy-only stocks with a 50 minimum order and a portfolio donut."
- "Add three verification tiers with daily limits of 500, 2,000, and 10,000, and a badge beside the user's name."

## Rules the skill enforces

- Plan first, work on a branch, open a pull request, merge only on yes
- One money model: one balance formula, one currency, one formatting helper
- PIN before every transfer and stock purchase
- Store only the last 4 digits of a card or ID number; never store a
  security code
- Real brand logos only, or a generic icon — never an invented logo
- Verify tests, type check, phone-width render, and the production
  deployment, not only a preview

## Sponsor

If this skill saves you time, you can sponsor the maintainer:

https://github.com/sponsors/jeffdrizzy

## License

MIT. See `LICENSE`.
