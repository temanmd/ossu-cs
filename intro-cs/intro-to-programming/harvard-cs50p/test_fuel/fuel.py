def main():
    fraction = input("Fraction: ").strip()
    precentage = convert(fraction)
    print(gauge(precentage))


def convert(fraction):
    a, b = fraction.split("/")
    a_num = int(a)
    b_num = int(b)
    if b_num == 0:
        raise ZeroDivisionError
    if a_num > b_num:
        raise ValueError
    return round(a_num / b_num * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    return f"{percentage}%"


if __name__ == "__main__":
    main()
