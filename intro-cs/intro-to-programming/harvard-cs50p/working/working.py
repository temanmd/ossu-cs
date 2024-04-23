import re


def convert(hours):
    regex_object = re.compile(
        r"^(([1-9]|1[0-2])|([1-9]|1[0-2]):([0-5]\d)) (AM|PM) " +
        r"to (([1-9]|1[0-2])|([1-9]|1[0-2]):([0-5]\d)) (AM|PM)$")

    if not (matches := regex_object.search(hours)):
        raise ValueError

    if matches.group(2):
        from_hour = matches.group(2)
        from_minutes = "00"
        to_hour = matches.group(7)
        to_minutes = "00"
    else:
        from_hour = matches.group(3)
        from_minutes = matches.group(4)
        to_hour = matches.group(8)
        to_minutes = matches.group(9)
    from_type = matches.group(5)
    to_type = matches.group(10)

    from_hours_result = convert_hours(from_hour, from_type)
    to_hours_result = convert_hours(to_hour, to_type)

    return f"{from_hours_result}:{from_minutes} to {to_hours_result}:{to_minutes}"


def convert_hours(from_hour, from_type):
    if from_type == "AM":
        result = "0" if from_hour == "12" else from_hour
    else:
        if from_hour == "12":
            result = from_hour
        else:
            result = str(12 + int(from_hour))

    return result if len(result) == 2 else f"0{result}"


def main():
    hours_12 = input("Hours: ").strip()
    hours_24 = convert(hours_12)
    print(hours_24)


if __name__ == "__main__":
    main()
