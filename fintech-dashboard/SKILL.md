---
name: fintech-dashboard
description: Build or extend a mobile-first fintech dashboard and banking app with a balance card, transactions and receipts, transfers with PIN confirmation, linked cards, buy-only stocks, and tiered identity verification. Use when someone asks to build a banking app, build a neobank, build a fintech dashboard, build a money app, add transfers, add cards, add stocks, add verification tiers, or add transaction receipts to an existing app.
---

# Fintech Dashboard

Build a mobile-first fintech dashboard that looks and behaves like a real banking app, without moving real money unless the project explicitly says so.

## When to use this skill

Use this skill when the user asks for any of these:

- Build a banking app, neobank, fintech dashboard, or money app
- Add a dashboard, balance, transactions, or activity feed to a finance app
- Add transfers, send money, bank transfers, or external bank selection
- Add linked cards, card details, freeze, or card PIN flows
- Add stocks, investing, portfolio, buy stocks, or market prices
- Add identity verification, verification tiers, daily limits, or KYC-style checks
- Add transaction receipts, payment results, or success and failure screens

Do not use this skill for a generic admin dashboard, a shop checkout, or a
marketing landing page. Those need different patterns.

## Rules that apply to every build

1. Plan first, then build. Show the plan, the files to change, and the
   verification steps before writing code. Do not start with code.
2. Work on a separate branch. Open a pull request for review. Merge only
   when the user explicitly says yes.
3. Money is simulated unless the project explicitly says it moves real
   money. Never invent a real payment provider, a real bank connection,
   or a real payout. Say clearly when balances and transfers are simulated.
4. One currency at a time. Pick the app currency once, store amounts in
   the smallest unit (for example cents), and format every amount from
   the same helper. Never hard-code a currency symbol in five places.
5. One source of truth for money. Every screen, chart, and table must
   derive from the same seeded data or the same database query. If the
   dashboard says one total and the transactions page says another, the
   build is wrong.
6. Never store sensitive data in full. Store only the last 4 digits of a
   card number or account number. Never store a full card number, a full
   government ID number, or a security code (CVV / CVC). See
   `references/verification-security.md`.
7. Never invent a brand logo. Use only a real, sourced logo, or a generic
   bank icon. See step 8.
8. Verify the production deployment, not only a preview build. A preview
   link passing does not prove the production app works.

## Procedure

Work through the steps in order. Do not skip step 1. Each step ends with
a check; do not move on until the check passes.

### Step 1 — Define the money model first

Before any UI, write down the model in plain language and get agreement:

- Who is a user, and what is an account?
- What is a transaction? List the types: deposit, transfer out, transfer
  in, card purchase, stock purchase, reward, fee, refund.
- What is a balance? Define it as a single formula, for example:
  opening balance plus all settled credits minus all settled debits.
  Pending transactions do not change the available balance.
- What is the currency, and what is the smallest unit?
- What is a daily limit, and which verification tier changes it?
- Is money simulated or real? If simulated, say so in the UI and in
  the README. Never let a simulated balance look like a real bank balance
  without a label.

Check: you can state the balance formula in one sentence, and you can
list every transaction type. If you cannot, stop and define them.

### Step 2 — Dashboard

Build the home screen first. It is the screen users judge the whole app by.

1. Balance card at the top: available balance, account label, and a
   hide-balance toggle. The toggle hides every amount on the screen,
   not only the main balance.
2. Quick actions under the balance: Send, Deposit, Activity, and one
   more action the app actually supports. Every button must go somewhere
   real. No dead buttons.
3. Recent activity: the latest 5 to 10 transactions, newest first, with
   name, date, amount, and a clear in / out sign. Tapping a row opens
   its detail.
4. Portfolio or holdings summary if the app has stocks: total value,
   a donut or breakdown by holding, and a link to the full Stocks tab.
5. A small markets or highlights box if the app has stocks. Keep it
   small on the dashboard; the full list lives on the Stocks tab.

Check: load the dashboard on a phone-width screen. Balance, actions,
and activity are all visible without horizontal scrolling. Hiding the
balance hides all amounts.

Reference: `references/dashboard.md`.

### Step 3 — Transactions and receipts

1. Transaction list: newest first, grouped by date, with search or
   filter by type if there are more than 20 transactions.
2. Transaction detail: open a full detail view on tap. Show amount,
   date and time, status, sender or recipient, reference, and the
   running balance after that transaction if the app tracks it.
3. Receipt: after a payment, show a receipt, not only a toast. The
   receipt must show amount, recipient, date, status, and reference.
   See `examples/transaction-receipt.md`.
4. Result screens: use a full-screen green result for success and a
   full-screen red result for failure. The result must state what
   happened, the amount, and the next step. Never show a success screen
   for a failed payment.
5. Status is explicit: SUCCESS, PENDING, or FAILED. A failed row shows
   no minus sign confusion: show the amount without implying money
   moved. A pending row must not count toward the available balance.

Check: complete one deposit and one transfer end to end. Both appear
in the list, both have a detail view, and the receipt matches the list.

Reference: `references/dashboard.md` and
`examples/transaction-receipt.md`.

### Step 4 — Transfers with PIN confirmation

Transfers are where most fintech builds fail. Follow this order exactly.

1. Transfer hub: list the transfer types the app supports, for example
   internal transfer, bank transfer, and external transfer. Each type
   leads to its own flow.
2. Recipient step: for bank transfer, show a bank picker. Use real
   brand marks only when you have a sourced SVG for that bank. If you
   do not have one, use the same generic bank icon for every bank.
   Never draw a look-alike logo.
3. Amount step: amount field, balance check, and a clear fee line
   (even if the fee is zero). Block the transfer if the amount is over
   the available balance or over the user's daily limit. Say why.
4. PIN step: ask for the PIN in a modal before sending, every time.
   The PIN is never shown on screen, never logged, and never stored
   in plain text. A wrong PIN blocks the transfer and says so.
5. Confirm step: show recipient, bank, amount, fee, and total on one
   screen before the final send. The user must confirm from that screen.
6. Result step: show the green or red full-screen result from step 3.
   A transfer is not done until the result screen has been shown.

Check: try to send without a PIN, with a wrong PIN, and with an amount
over the balance. All three must be blocked with a clear message.

Reference: `references/transfers.md`.

### Step 5 — Linked cards

1. Card list: show each linked card as a card face, with brand, last
   4 digits, expiry, and a frozen badge if frozen. Never show a full
   card number in a list.
2. Add card: collect the card details, validate them, and store only
   the last 4 digits plus brand, expiry, and a token or reference from
   the payment provider. Never store the full number or the security code.
3. Card details: show full details only after a PIN check, and only to
   the card owner. Show the full number and security code on the back
   of the card view, and hide them again when the user leaves.
4. Freeze, unfreeze, and delete: each action applies to the selected
   card only. A frozen card is greyed out, shows a Frozen badge, and
   cannot be used for a transfer or a payment.
5. Legacy cards: if an old card was stored before the current rules,
   show a clear re-add note instead of pretending its details exist.

Check: add a card, view its details after PIN, freeze it, and confirm
it cannot be used. The list never shows a full number.

Reference: `references/cards-stocks.md`.

### Step 6 — Stocks, buy-only

Keep stocks simple. Buy-only is a complete feature; selling, shorting,
and margin are separate features.

1. Stock list: a fixed list the app can support, for example 100
   stocks. Each row shows symbol, name, price, and change. Prices
   come from one price source, refreshed on a schedule, and cached
   so the list does not hammer the provider.
2. Search: search filters the full list by symbol or name, including
   stocks not yet loaded on screen. Tapping a stock row scrolls to
   the buy panel.
3. Buy panel: any stock, any amount, with a minimum order amount
   (for example 50 in the app currency). Show the estimated shares,
   the fee if any, and the total before confirming.
4. PIN: ask for the PIN before a stock purchase, the same way as a
   transfer. A purchase without a PIN must be blocked.
5. Portfolio: holdings list, total value, and a donut by holding.
   Portfolio value must equal the sum of holdings. If it does not,
   the data is wrong, not the chart.
6. Live prices: show when the price was last updated. Never show a
   stale price as if it were live.

Check: search for a stock that is not on the first screen, buy the
minimum amount, and confirm the portfolio total updates by the same
amount.

Reference: `references/cards-stocks.md`.

### Step 7 — Verification tiers

Verification controls daily limits. Build it as tiers, not as a single
on / off switch.

1. Define three tiers with clear daily limits, for example Tier 1:
   500 per day, Tier 2: 2,000 per day, Tier 3: 10,000 per day, all in
   the app currency. Pick limits that fit the project; keep the
   three-tier shape.
2. Tier 1: basic account, lowest limit.
3. Tier 2: higher limit. The app may collect a full card number and
   front and back photos of a card for review, but it must store only
   the last 4 digits and never store the security code.
4. Tier 3: highest limit. The app may collect a full government ID
   number for admin review, but it must store only the last 4 digits.
5. Badge: show a tick beside the user's name when any tier is verified.
   Use a scalloped rosette badge in a different colour per tier, for
   example green for Tier 1, indigo for Tier 2, gold for Tier 3.
   Colour the tick by the highest verified tier.
6. Enforcement: enforce the daily limit on every transfer and purchase,
   not only on the dashboard. A user over the limit must see the limit,
   the amount already used today, and the next tier that would raise it.
7. Admin review: tier upgrades that need review go to an admin queue.
   The user sees PENDING until an admin approves or declines.

Check: a Tier 1 user cannot send more than the Tier 1 daily limit,
even by splitting it into two transfers. The badge colour matches the
highest verified tier.

Reference: `references/verification-security.md`.

### Step 8 — Brand icons

1. Use real brand marks only from a trustworthy source: the brand's
   official brand page, the official SVG, or a reputable icon library
   that vendors the mark.
2. Vendor the logo locally as an SVG path. Do not hotlink a logo from
   another site.
3. If no trustworthy SVG exists for a bank or brand, keep the generic
   icon. Do not invent a logo, do not substitute a similar logo, and
   do not trace a low-resolution image.
4. Keep a list of which banks have a real mark and which use the
   generic icon. Update that list when a new mark is added, and test
   the new mark at phone width.
5. Brand icons and logos never change style to match the app theme.
   A brand mark keeps its own colours.

Check: every logo on the bank picker is either a sourced real mark or
the generic icon. There are no invented logos.

### Step 9 — Verify with tests and a live render

Do not call a step done until it is verified.

1. Type check: run the type checker. Zero errors in changed files.
2. Unit tests: run the test suite. All tests pass. Add a test for
   every new money rule: balance formula, daily limit, PIN block,
   frozen card block, and minimum stock order.
3. Render check: render the changed screens at phone width and look
   at them. Check the balance toggle, the receipt, the PIN modal,
   and the result screens.
4. Seeded data check: if the app uses seeded demo data, check that
   the dashboard total, the portfolio total, and the transaction list
   all agree. They must all come from the same seeded book.
5. Production check: after merging, check the production deployment,
   not only the preview deployment. Log in as a real user, load the
   dashboard, and complete one transfer. If the production deploy
   fails or is stale, say so, check the deploy log, and change the
   approach if the first fix fails. Do not repeat the same fix faster.
6. Record what you checked: the commit, the test result, the type
   check result, and the production URL you checked.

Check: tests pass, type check is clean, the render looks right at
phone width, and the production app shows the change.

Reference: `references/testing.md`.

## Checklists

### Before you start

- [ ] Money model is written down: balance formula, transaction types,
  currency, smallest unit, daily limits
- [ ] Simulated or real money is stated in the plan and in the UI
- [ ] Branch is created, pull request will be opened for review
- [ ] Price source, bank list, and stock list are named, not invented

### Before you merge

- [ ] Balance, portfolio, and transaction list agree
- [ ] PIN is required for transfers and stock purchases
- [ ] No full card number, government ID number, or security code is
  stored or logged
- [ ] Frozen cards cannot be used
- [ ] Daily limits are enforced on every money action
- [ ] Type check is clean in changed files, tests pass
- [ ] Changed screens were rendered and checked at phone width
- [ ] Production deployment was checked, not only preview

## Common mistakes

- Storing a full card number, government ID number, or security code.
  Store only the last 4 digits. Never store the security code.
- Showing a success screen for a failed payment, or showing a failed
  row with a minus sign that implies money moved.
- Letting the dashboard total, the portfolio total, and the transaction
  list disagree. Fix the data, not the chart.
- Allowing a transfer or a stock purchase without a PIN.
- Inventing a bank logo, or substituting a similar logo when the real
  one is not available. Use the generic icon instead.
- Checking only the preview deployment and calling the work live.
  Check production.
- Adding a dead button. Every quick action must go somewhere real.
- Hard-coding a currency symbol in many places. Format amounts from
  one helper.
- Treating a simulated balance as a real bank balance. Label it.

## What NOT to do

- Do not move real money unless the project explicitly says so and
  the payment provider, account, and authorisation are named.
- Do not collect a government ID number, card number, or security
  code without a stated reason, a storage rule, and an admin review
  process.
- Do not bypass the PIN flow, the daily limit, or the verification
  tier for convenience or for testing in production.
- Do not copy private code or business logic from another project
  into this one. Build the feature from the spec in this skill.
- Do not add selling, shorting, margin, lending, or credit as part
  of buy-only stocks. Those are separate features with separate specs.
- Do not claim a deployment is live until you have checked the
  production URL yourself.
