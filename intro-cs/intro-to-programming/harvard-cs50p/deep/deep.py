prompt_text = ("What is the Answer to the Great Question"
               "of Life, the Universe, and Everything? ")
answer = input(prompt_text).lower().strip()

match answer:
    case "yes" | "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
