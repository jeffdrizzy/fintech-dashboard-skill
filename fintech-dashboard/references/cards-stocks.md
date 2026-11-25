# Linked Cards and Stocks

Load this file when building or changing linked cards, card details,
freeze, or stocks.

## Linked cards

- Card list shows each card as a card face: brand, last 4 digits,
  expiry, and a Frozen badge if frozen.
- Never show a full card number in a list.
- Add card: collect details, validate them, store only the last 4
  digits plus brand, expiry, and a provider token or reference.
- Never store a full card number. Never store a security code.
- Card details: show full details only after a PIN check, and only
  to the card owner. Show the full number and security code on the
  back of the card view, and hide them again when the user leaves.
- Freeze, unfreeze, and delete act on the selected card only.
- A frozen card is greyed out, shows a Frozen badge, and cannot be
  used for a transfer or a payment.
- Legacy cards stored before the current rules show a clear re-add
  note instead of pretending their details exist.

## Stocks, buy-only

- Keep stocks buy-only. Selling, shorting, and margin are separate
  features with separate specs.
- Stock list: a fixed list the app can support, for example 100
  stocks. Each row shows symbol, name, price, and change.
- Prices come from one price source, refreshed on a schedule, and
  cached. Show when the price was last updated.
- Search filters the full list by symbol or name, including stocks
  not yet loaded on screen. Tapping a stock row scrolls to the
  buy panel.
- Buy panel: any stock, any amount, with a minimum order amount
  (for example 50 in the app currency). Show estimated shares,
  fee if any, and total before confirming.
- PIN is required before a stock purchase, the same way as a
  transfer. A purchase without a PIN must be blocked.
- Portfolio: holdings list, total value, and a donut by holding.
  Portfolio value must equal the sum of holdings.
- The PIN popup is used on the Stocks page too, not only on
  the transfer pages.

## Common mistakes

- Showing a full card number in a list or in a log.
- Storing a security code, even temporarily in a log or a test.
- Letting a frozen card be used for a payment.
- Letting portfolio total disagree with the sum of holdings.
- Showing a stale price as if it were live.
- Adding selling or margin inside a buy-only build.
