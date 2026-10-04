#collect customer information
customer = input("Enter customer name: ")

# First product
product1 = input("Enter first product name: ")
price1 = float(input("Enter first product price (ETB): "))
quantity1 = int(input("Enter first product quantity: "))

# Second product
product2 = input("Enter second product name: ")
price2 = float(input("Enter second product price (ETB): "))
quantity2 = int(input("Enter second product quantity: "))

# Calculate totals
total1 = price1 * quantity1
total2 = price2 * quantity2
total = total1 + total2

# Display receipt
print("=" * 40)
print("             RECEIPT")
print("=" * 40)

print(f"Customer: {customer}")
print()
print(f"{'Product':<15}{'Price':>10}{'Qty':>7}")
print("-" * 40)

print(f"{product1:<15}{price1:>7.2f} ETB {quantity1:>3}")
print(f"{product2:<15}{price2:>7.2f} ETB {quantity2:>3}")

print("-" * 40)
print(f"Total: {total:.2f} ETB")
print()
print("Thank you for shopping!")
print("=" * 40)
