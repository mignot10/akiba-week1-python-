# collect exchange rate and USD amount
exchange_rate = float(input("Enter exchange rate (1 USD in ETB): "))
usd_amount = float(input("Enter amount in USD: "))

# Calculate conversion
etb_amount = usd_amount * exchange_rate

# Display receipt
print("=" * 35)
print("       CURRENCY EXCHANGE")
print("=" * 35)

print(f"USD Amount:       {usd_amount:,.2f} USD")
print(f"Exchange Rate:    1 USD = {exchange_rate:,.2f} ETB")

print("-" * 35)
print(f"ETB Amount:       {etb_amount:,.2f} ETB")
print("=" * 35)
