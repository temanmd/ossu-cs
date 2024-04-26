from datetime import date
import sys
import inflect


def calc_minutes(date_input):
    try:
        parsed_date = date.fromisoformat(date_input)
    except ValueError:
        sys.exit("Invalid date")
    today = date.today()
    delta = today - parsed_date
    return int(delta.total_seconds() / 60)


def format_to_words(minutes):
    inflect_engine = inflect.engine()
    part_1 = inflect_engine.number_to_words(minutes, andword="")
    plural_minutes = inflect_engine.plural("minute", minutes)
    return f"{part_1} {plural_minutes}".capitalize()


def main():
    date_input = input("Date of Birth: ").strip()
    minutes = calc_minutes(date_input)
    print(format_to_words(minutes))


if __name__ == "__main__":
    main()
