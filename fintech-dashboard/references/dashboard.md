# Dashboard

Load this file when building or changing the home dashboard, the balance
card, the activity feed, or transaction detail and receipts.

## Balance card

- Show available balance, account label, and currency.
- Hide-balance toggle hides every amount on the screen: main balance,
  quick-action hints, activity amounts, and portfolio values. Test the
  toggle on every section, not only the balance.
- Amounts come from one formatting helper. Store amounts in the smallest
  unit and format at render time.
- If money is simulated, label it. Do not let a simulated balance look
  like a real bank balance without a label.

## Quick actions

- Send, Deposit, Activity, plus one more action the app actually
  supports. Every button must navigate to a real screen.
- No dead buttons. If an action is not built yet, do not show its button.

## Recent activity

- Latest 5 to 10 transactions, newest first.
- Each row: name, date, amount with in / out sign, status if not
  successful.
- Tapping a row opens transaction detail.
- Group by date when the list is long. Add search or filter by type
  when there are more than 20 transactions.

## Portfolio summary

- Total value, breakdown by holding, link to the full Stocks tab.
- Portfolio value must equal the sum of holdings. If it does not,
  fix the data, not the chart.
- Show when prices were last updated. Never show a stale price as live.

## Transaction detail and receipt

- Detail shows amount, date and time, status, sender or recipient,
  reference, and running balance after that transaction if tracked.
- Receipt after a payment shows amount, recipient, date, status, and
  reference. See `examples/transaction-receipt.md`.
- Status is SUCCESS, PENDING, or FAILED. A FAILED row shows no minus
  sign that implies money moved. A PENDING row does not change the
  available balance.
- Result screens are full-screen: green for success, red for failure.
  Each states what happened, the amount, and the next step.

## Common mistakes

- Hiding only the main balance and leaving amounts visible elsewhere.
- Dashboard total disagreeing with the transaction list.
- Showing a stale price or a simulated balance as if it were live.
- A dead quick-action button.
