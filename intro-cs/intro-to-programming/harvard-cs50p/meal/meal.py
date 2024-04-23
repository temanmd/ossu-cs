def main():
    human_time = input("What time is it? ").strip()
    float_time = convert(human_time)

    if 7 <= float_time <= 8:
        print("breakfast time")
    elif 12 <= float_time <= 13:
        print("lunch time")
    elif 18 <= float_time <= 19:
        print("dinner time")

def convert(time):
    format_parts = time.lower().split()
    hours_str, minutes_str = format_parts[0].split(":")
    hours_int, minutes_int = [int(hours_str), int(minutes_str)]
    hours_result = hours_int
    minutes_result = round(minutes_int / 60, 2)

    if len(format_parts) == 2:
        # its 12-hours format
        day_side = format_parts[1]
        match day_side:
            case "a.m.":
                if hours_int >= 12:
                    hours_result = 0
            case "p.m.":
                if hours_int != 12:
                    hours_result = hours_int + 12

    return(hours_result + minutes_result)

if __name__ == "__main__":
    main()
