# Example: Transaction Receipt

A worked example for a bank transfer. All names, banks, and numbers
are placeholders. No real user data.

## Scenario

- Sender: Alex Morgan, Tier 2 verified, daily limit 2,000
- Recipient: Jordan Lee
- Recipient bank: Example Bank, account ending 4321
- Amount: 150
- Fee: 0
- Total: 150
- Currency: the app currency, amounts in the smallest unit in storage
- Date: 2026-11-25, 14:05 local time
- Reference: TXN-20261125-0001

## Data model

```
Transaction
  id: txn_0001
  type: transfer_out
  status: SUCCESS
  amount: 150
  fee: 0
  currency: APP_CURRENCY
  sender: user_alex
  recipient_name: Jordan Lee
  recipient_bank: Example Bank
  recipient_account_last4: 4321
  reference: TXN-20261125-0001
  created_at: 2026-11-25T14:05:00
  balance_after: 850
```

Notes:

- Store only the last 4 digits of the recipient account.
- Never store a full account number, card number, government ID
  number, or security code in a transaction record.
- `balance_after` is the sender balance after this transaction.
  It must agree with the dashboard balance and the transaction list.

## Flow

1. Sender opens Send, chooses Bank Transfer.
2. Sender picks Example Bank from the bank picker, enters the
   recipient name and account, and enters 150.
3. App checks the amount against the available balance (1,000)
   and the Tier 2 daily limit (2,000, with 0 used today). Both pass.
4. App shows a confirm screen: recipient, bank, amount 150,
   fee 0, total 150.
5. Sender confirms. App asks for the PIN in a modal.
6. Sender enters the correct PIN. The transfer is sent.
7. App shows a full-screen green result, then the receipt below.

## Receipt

```
Payment successful

Amount: 150
Fee: 0
Total: 150

To: Jordan Lee
Bank: Example Bank
Account: ending 4321

Date: 2026-11-25, 14:05
Reference: TXN-20261125-0001
Status: SUCCESS

Balance after: 850
```

## Failure version

If the same transfer fails, show a full-screen red result instead:

```
Payment failed

Amount: 150
To: Jordan Lee, Example Bank, ending 4321
Reference: TXN-20261125-0001
Status: FAILED

No money was sent. Try again, or contact support.
```

The failed row in the transaction list shows the amount with no
minus sign implying money moved, and the balance after is unchanged.

## PIN failure version

If the sender enters a wrong PIN, the transfer is blocked before
sending:

```
Incorrect PIN. The transfer was not sent.
```

No transaction record is created for a PIN failure, and no money
moves.

## Checks for this example

- [ ] Receipt amount, recipient, bank, date, status, and reference
  match the transaction list entry
- [ ] Balance after (850) matches the dashboard balance
- [ ] Recipient account shows only the last 4 digits
- [ ] Failed version shows no minus sign implying money moved
- [ ] Wrong PIN blocks the transfer with no transaction created
