string = input("Input a few names: ").strip()

# lets split string with "," char
names = string.split(", ")


# print each name with newline
for name in names:
    print(name)
