def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(string):
    return ((2 <= len(string) <= 6) and
            string.isalnum() and
            string[0:2].isalpha() and
            check_numbers(string))


def check_numbers(string):
    remainder = string[2:]
    if len(remainder) == 0 or remainder.isalpha():
        return True
    else:
        for index in range(len(remainder)):
            char = remainder[index]
            if char.isdigit():
                return(remainder[index:].isdigit() and char != "0")
        return True


if __name__ == "__main__":
    main()
