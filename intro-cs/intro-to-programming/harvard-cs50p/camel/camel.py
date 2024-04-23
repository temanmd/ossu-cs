string = input("camelCase: ")
result = ""

for char in string:
    if char.isupper():
        result += f"_{char.lower()}"
    else:
        result += char

print(result)
