import random

while True:
    n = input("Level: ").strip()
    try:
        level = int(n)
    except ValueError:
        continue
    if level > 0: break

right_number = random.randint(1, level)

while True:
    guess_input = input("Guess: ").strip()
    try:
        guess_number = int(guess_input)
    except ValueError:
        continue
    if guess_number < 1: continue

    if guess_number == right_number:
        print("Just right!")
        break
    elif guess_number > right_number:
        print("Too large!")
        continue
    else:
        print("Too small!")
        continue
