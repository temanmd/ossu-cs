def main():
    string = input("Input: ").strip()
    shorten_string = shorten(string)
    print(f"Output: {shorten_string}")


def shorten(string):
    vowels = ["A", "E", "I", "O", "U"]
    result = ""
    for char in string:
        if char.upper() not in vowels:
            result += char
    return result


if __name__ == "__main__":
    main()
