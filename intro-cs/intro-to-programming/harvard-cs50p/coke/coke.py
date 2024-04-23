amount_due = 50

while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    payment = int(input("Insert Coin: "))
    if payment == 5 or payment == 10 or payment == 25:
        amount_due -= payment

print(f"Change Owed: {abs(amount_due)}")
