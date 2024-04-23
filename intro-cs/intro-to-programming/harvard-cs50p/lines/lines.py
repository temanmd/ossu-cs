import sys


def get_file(args):
    if len(args) == 0:
        sys.exit("Too few command-line arguments")
    if len(args) > 1:
        sys.exit("Too many command-line arguments")

    filename = args[0]
    filename_parts = filename.split(".")

    if len(filename_parts) == 2 and filename_parts[1] == "py":
        try:
            return open(filename, "r")
        except FileNotFoundError:
            sys.exit("File does not exist")

    sys.exit("Not a Python file")


def lines(file):
    result = 0
    for line in file:
        if line.lstrip().startswith("#") or line.lstrip() == "":
            continue
        result += 1

    return result


def main():
    file = get_file(sys.argv[1:])
    print(lines(file))


if __name__ == "__main__":
    main()
