import validators


def validate(email):
    return "Valid" if validators.email(email) else "Invalid"


def main():
    email = input("What's your email address? ").strip()
    print(validate(email))


if __name__ == "__main__":
    main()
