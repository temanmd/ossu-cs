import sys, csv


def generate_after_csv(before_file, after_filename):
    headers = ["first", "last", "house"]
    csv_reader = csv.reader(before_file)

    with open(after_filename, "w") as after_file:
        csv_writer = csv.writer(after_file)
        csv_writer.writerow(headers)

        for row in list(csv_reader)[1:]:
            csv_writer.writerow(parse_before_row(row))


def parse_before_row(row):
    first_name, last_name = list(reversed(row[0].split(", ")))
    house = row[1]
    return [first_name, last_name, house]


def main():
    args_length = len(sys.argv)
    if args_length < 3:
        sys.exit("Too few command-line arguments")
    if args_length > 3:
        sys.exit("Too many command-line arguments")

    before_csv = sys.argv[1]
    after_csv = sys.argv[2]

    try:
        with open(before_csv) as before_file:
            generate_after_csv(before_file, after_csv)
    except FileNotFoundError:
        sys.exit(f"Could not read {before_csv}")


if __name__ == "__main__":
    main()
