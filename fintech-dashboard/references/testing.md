# Testing and Verification

Load this file when verifying a fintech dashboard build, before
merging, and when checking a deployment.

## Type check and unit tests

- Run the type checker. Zero errors in changed files.
- Run the test suite. All tests pass.
- Add a test for every new money rule:
  - balance formula
  - daily limit, including split-payment bypass attempts
  - PIN block for transfers and stock purchases
  - frozen card block
  - minimum stock order
  - failed transaction has no minus sign implying money moved
- Do not merge with a failing test, even if the UI looks right.

## Render check

- Render the changed screens at phone width and look at them.
- Check the balance toggle hides every amount.
- Check the receipt, the PIN modal, and the green and red result
  screens.
- Check the bank picker at phone width. Every logo is either a
  sourced real mark or the generic icon.
- Check the verification badge colour matches the highest
  verified tier.

## Seeded data check

- If the app uses seeded demo data, use one seeded book so every
  number agrees.
- Dashboard total, portfolio total, and transaction list must all
  come from the same seeded data.
- If they disagree, fix the data, not the chart.
- Record the seed, the commit, and the expected totals in the
  pull request.

## Production check, not preview only

- After merging, check the production deployment, not only the
  preview deployment.
- Log in as a real user, load the dashboard, and complete one
  transfer.
- If the production deploy fails, is stale, or does not carry the
  merged commit, say so. Check the deploy log.
- If the first fix fails, change the approach. Do not repeat the
  same fix faster.
- Record what you checked: the commit, the test result, the type
  check result, and the production URL you checked.

## Before you merge — checklist

- [ ] Type check is clean in changed files
- [ ] Tests pass, including new money-rule tests
- [ ] Changed screens were rendered and checked at phone width
- [ ] Balance, portfolio, and transaction list agree
- [ ] PIN is required for transfers and stock purchases
- [ ] No full card number, government ID number, or security code
  is stored or logged
- [ ] Frozen cards cannot be used
- [ ] Daily limits are enforced on every money action
- [ ] Production deployment was checked, not only preview
