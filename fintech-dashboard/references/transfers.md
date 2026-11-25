# Transfers

Load this file when building or changing send money, bank transfer,
internal transfer, or external transfer flows.

## Flow order

1. Transfer hub: list the transfer types the app supports.
2. Recipient: name, account, and bank for bank transfer.
3. Amount: amount, balance check, fee line even if the fee is zero.
4. PIN: PIN modal before sending, every time.
5. Confirm: recipient, bank, amount, fee, and total on one screen.
6. Result: full-screen green success or red failure screen.

Do not skip or reorder these steps.

## Bank picker

- Use real brand marks only when you have a sourced SVG for that bank.
- Vendor the logo locally as an SVG path. Do not hotlink a logo.
- If no trustworthy SVG exists, use the same generic bank icon.
- Never invent a logo. Never substitute a similar logo.
- Keep a list of banks with a real mark and banks with the generic icon.
- Brand marks keep their own colours. Do not restyle them to match
  the app theme.

## Amount and limits

- Block the transfer if the amount is over the available balance.
- Block the transfer if the amount is over the user's daily limit.
- Show the limit, the amount already used today, and the next tier
  that would raise the limit.
- Enforce the limit on every money action, not only on the dashboard.
  Splitting a transfer into two smaller transfers must not bypass it.

## PIN

- Ask for the PIN in a modal before sending, every time.
- The PIN is never shown on screen, never logged, and never stored
  in plain text.
- A wrong PIN blocks the transfer and says so.
- A transfer without a PIN must be blocked. There is no exception
  for testing in production.

## Confirm and result

- Confirm screen shows recipient, bank, amount, fee, and total.
- The user confirms from that screen. No silent send.
- Result screen states what happened, the amount, and the next step.
- A transfer is not done until the result screen has been shown.
- The receipt must match the transaction list entry.

## Common mistakes

- Skipping the PIN step, or allowing a transfer after a wrong PIN.
- Letting a user bypass a daily limit by splitting a transfer.
- Inventing a bank logo.
- Showing a success screen for a failed transfer.
