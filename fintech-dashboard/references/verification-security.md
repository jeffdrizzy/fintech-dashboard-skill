# Verification Tiers and Security

Load this file when building or changing identity verification,
verification tiers, daily limits, admin review, or sensitive data
handling.

## Three tiers

Define three tiers with clear daily limits, for example:

- Tier 1: 500 per day
- Tier 2: 2,000 per day
- Tier 3: 10,000 per day

All limits are in the app currency. Pick limits that fit the project.
Keep the three-tier shape.

## What each tier may collect

- Tier 1: basic account, lowest limit.
- Tier 2: higher limit. The app may collect a full card number and
  front and back photos of a card for review.
- Tier 3: highest limit. The app may collect a full government ID
  number for admin review.

Collect only what the tier needs. Do not collect a government ID
number for Tier 1.

## Storage rules — these are absolute

- Store only the last 4 digits of a card number or account number.
- Store only the last 4 digits of a government ID number.
- Never store a full card number.
- Never store a full government ID number.
- Never store a security code (CVV / CVC), not in the database,
  not in a log, not in a test fixture, not even temporarily.
- Never log a PIN, a full card number, a full government ID number,
  or a security code.
- Full details are shown only after a PIN check, only to the owner,
  and hidden again when the user leaves the screen.

## Badge

- Show a tick beside the user's name when any tier is verified.
- Use a scalloped rosette badge in a different colour per tier,
  for example green for Tier 1, indigo for Tier 2, gold for Tier 3.
- Colour the tick by the highest verified tier.
- A user with no verified tier shows no tick.

## Enforcement

- Enforce the daily limit on every transfer and purchase, not only
  on the dashboard.
- A user over the limit sees the limit, the amount already used
  today, and the next tier that would raise it.
- Splitting a payment into smaller payments must not bypass the limit.

## Admin review

- Tier upgrades that need review go to an admin queue.
- The user sees PENDING until an admin approves or declines.
- Admins see the submitted evidence, not a stored full number.
  The review decision is recorded with who approved it and when.

## Common mistakes

- Storing a full number "just for now" or "just in a test".
- Storing a security code anywhere.
- Enforcing limits only on one screen.
- Showing a verified tick for a pending tier.
- Collecting a government ID number without a stated reason,
  a storage rule, and an admin review process.
