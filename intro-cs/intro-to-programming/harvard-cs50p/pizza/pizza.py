import sys
import csv
from tabulate import tabulate


def render_csv(file):
    reader = csv.reader(file)
    rows_list = list(reader)
    print(tabulate(rows_list,
                   headers="firstrow",
                   tablefmt="grid"))


def main():
    args_length = len(sys.argv)
    if args_length == 1:
        sys.exit("Too few command-line arguments")
    if args_length > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    try:
        with open(sys.argv[1]) as file:
            render_csv(file)
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
