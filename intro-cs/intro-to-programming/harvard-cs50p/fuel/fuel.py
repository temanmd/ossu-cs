while True:
    try:
        a, b = input("Fraction: ").split("/")
        a_num = int(a)
        b_num = int(b)
        if a_num <= b_num:
            percentage = round(a_num / b_num * 100)
            break
    except (ValueError, ZeroDivisionError):
        pass

if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")
