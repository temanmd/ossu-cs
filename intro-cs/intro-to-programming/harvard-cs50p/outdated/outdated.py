months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ").strip()
        if len(date) > 10:
            month_day, year = date.split(",")
            month, day = month_day.split()
            month_number = int(months.index(month) + 1)
        else:
            month, day, year = date.split("/")
            month_number = int(month)
            if month_number > 12:
                continue

        day = int(day.split(',')[0])
        if day > 31:
            continue
        break
    except ValueError:
        continue
    except EOFError:
        print()
        break

print(f"{year}-{month_number:02}-{day:02}")
