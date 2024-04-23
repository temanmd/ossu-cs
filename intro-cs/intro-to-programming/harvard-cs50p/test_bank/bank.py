def main():
    greeting = input("Greeting: ")
    result = value(greeting)
    print(f"${result}")


def value(greeting):
    string = greeting.strip().lower()
    if string.startswith("h"):
        return 0 if string.startswith("hello") else 20
    return 100


if __name__ == "__main__":
    main()
