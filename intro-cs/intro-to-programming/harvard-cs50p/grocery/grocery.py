cart = {}

while True:
    try:
        product = input().strip()
    except EOFError:
        break
    if product in cart:
        cart[product] += 1
    else:
        cart[product] = 1

print()
for item in sorted(cart):
    print(f"{cart[item]} {item.upper()}")
