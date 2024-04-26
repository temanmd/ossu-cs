from datetime import date
import sys
import inflect


inflect_engine = inflect.engine()


def minutes_from_date(date_input):
    minutes = calc_minutes(date_input)
    return format_to_words(minutes)


def calc_minutes(date_input):
    try:
        parsed_date = date.fromisoformat(date_input)
    except ValueError:
        sys.exit("Invalid date")
    today = date.today()
    delta = today - parsed_date
    return int(delta.total_seconds() / 60)


def format_to_words(minutes):
    part_1 = inflect_engine.number_to_words(minutes, andword="")
    plural_minutes = inflect_engine.plural("minute", minutes)
    return f"{part_1} {plural_minutes}".capitalize()


def main():
    date_input = input("Date of Birth: ").strip()
    print(minutes_from_date(date_input))


if __name__ == "__main__":
    main()