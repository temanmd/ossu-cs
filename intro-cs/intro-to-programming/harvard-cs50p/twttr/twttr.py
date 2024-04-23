string = input("Input: ")
output = ""

for char in string:
    if char.lower() not in ["a", "e", "i", "o", "u"]:
        output += char

print("Output:", output)
