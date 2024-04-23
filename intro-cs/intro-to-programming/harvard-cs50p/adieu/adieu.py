names = []

while True:
    try:
        name = input("Name: ").strip()
        names.append(name)
    except EOFError:
        break

def generate_names_phrase(list):
    match len(list):
        case 1:
            return list[0]
        case 2:
            return " and ".join(list)
        case _:
            first_part = ", ".join(list[:-1])
            return f"{first_part}, and {list[-1]}"

names_phrase = generate_names_phrase(names)
print(f"\nAdieu, adieu, to {names_phrase}")
