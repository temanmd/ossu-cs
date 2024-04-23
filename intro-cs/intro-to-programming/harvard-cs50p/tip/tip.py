def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(string):
    without_prefix = string.removeprefix("$")
    return(float(without_prefix))


def percent_to_float(string):
    without_suffix = string.removesuffix("%")
    return(float(without_suffix) / 100)

main()
