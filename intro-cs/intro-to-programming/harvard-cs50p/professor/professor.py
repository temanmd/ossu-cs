import random


def main():
    level = get_level()
    correct_answers = 0

    for _ in range(10):
        mistakes = 0
        a = generate_integer(level)
        b = generate_integer(level)
        expected_result = a + b

        while True:
            try:
                user_result = int(
                    input(f"{a} + {b} = ").strip()
                )
                if expected_result != user_result:
                    raise ValueError
            except ValueError:
                mistakes += 1
                if mistakes == 3:
                    print(f"{a} + {b} = {expected_result}")
                    break
                print("EEE")
                continue
            correct_answers += 1
            break

    print(f"Score: {correct_answers}")


def get_level():
    while True:
        n = input("Level: ").strip()
        try:
            level = int(n)
            if not is_correct_level(level): continue
        except ValueError:
            continue
        break

    return level


def generate_integer(level):
    if not is_correct_level(level): raise ValueError

    if level == 1:
        from_num = 0
    else:
        from_num = 1
        for _ in range(level-1):
            from_num *= 10

    to_num_string = ""
    for _ in range(level):
        to_num_string += "9"
    to_num = int(to_num_string)

    return random.randint(from_num, to_num)


def is_correct_level(level):
    return 1 <= level <= 3


if __name__ == "__main__":
    main()
