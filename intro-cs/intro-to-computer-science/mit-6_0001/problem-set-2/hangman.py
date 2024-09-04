# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, "r")
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """

    for char in set(secret_word):
        if char not in letters_guessed:
            return False

    return True


def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    """
    result = []

    for char in secret_word:
        if char in letters_guessed:
            result.append(char)
        else:
            result.append("_ ")

    return "".join(result)


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    """
    result = []

    for char in string.ascii_lowercase:
        if char not in letters_guessed:
            result.append(char)

    return "".join(result)


def draw_line():
    print("-----------")


def get_warnings_left_text(warnings):
    return f"You have {warnings} warnings left."


def handle_wrong_answer(warnings, guesses):
    new_warnings = warnings
    new_guesses = guesses
    if warnings > 0:
        new_warnings -= 1
        warnings_left_text = get_warnings_left_text(new_warnings)
    else:
        new_guesses -= 1
        warnings_left_text = "You have no warnings left so you lose one guess"
    return [new_warnings, new_guesses, warnings_left_text]


def match_with_gaps(my_word, other_word):
    """
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    """
    my_index = 0
    other_index = 0
    missed_chars = []

    while my_index < len(my_word):
        my_letter = my_word[my_index]
        try:
            other_letter = other_word[other_index]
        except IndexError:
            return False

        if my_letter == other_letter:
            if my_letter in missed_chars:
                return False
            my_index += 1
        else:
            if my_letter == "_":
                missed_chars.append(other_letter)
                my_index += 2
            else:
                return False

        other_index += 1

    return True if other_index == len(other_word) else False


def show_possible_matches(my_word):
    """
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    """
    result = []

    for word in wordlist:
        if match_with_gaps(my_word, word):
            result.append(word)

    if result == []:
        print("No matches found")
        return

    print(" ".join(result))


def hangman(secret_word, with_hints=False):
    """
    secret_word: string, the secret word to guess
    with_hints: boolean, to game w/ hints (default False)

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If with_hints param is True and the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    """
    guesses = 6
    warnings = 3
    letters_guessed = set()
    vowels = ["a", "e", "i", "o", "u"]

    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print(get_warnings_left_text(warnings))

    while True:
        draw_line()
        print(f"You have {guesses} guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))

        guess_letter = input("Please guess a letter: ").strip().lower()

        if with_hints and guess_letter == "*":
            print("Possible word matches are:")
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            continue

        wrong_answer = len(guess_letter) > 1 or not guess_letter.isalpha()
        already_guessed = guess_letter in letters_guessed

        if wrong_answer or already_guessed:
            warnings, guesses, warnings_left_text = handle_wrong_answer(
                warnings, guesses
            )
            if wrong_answer:
                print("Oops! That is not a valid letter. ", end="")
            else:
                print("Oops! You've already guessed that letter. ", end="")
            if guesses == 0:
                print()
                break
            print(
                f"{warnings_left_text}: {get_guessed_word(secret_word, letters_guessed)}"
            )
        else:
            letters_guessed.add(guess_letter)
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            if guess_letter in secret_word:
                print(f"Good guess: {guessed_word}")
            else:
                print("Oops! That letter is not in my word.")
                if guess_letter in vowels:
                    guesses -= 2
                else:
                    guesses -= 1
                if guesses < 1:
                    break
                print(f"Please guess a letter: {guessed_word}")
            if is_word_guessed(secret_word, letters_guessed):
                break

    draw_line()
    if guesses == 0:
        print(f"Sorry, you ran out of guesses. The word was {secret_word}.")
    else:
        score = guesses * len(set(secret_word))
        print("Congratulations, you won!")
        print(f"Your total score for this game is: {score}")


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # print(secret_word)
    # hangman(secret_word)

    secret_word = choose_word(wordlist)
    hangman(secret_word, True)

    # show_possible_matches("t_ _ t")
    # show_possible_matches("abbbb_ ")
    # show_possible_matches("a_ pl_ ")

    # print(match_with_gaps("t_ _ t", "to"))
    # print(match_with_gaps("te_ t", "tact"))
    # print(match_with_gaps("a_ _ le", "banana"))
    # print(match_with_gaps("a_ _ le", "apple"))
    # print(match_with_gaps("a_ ple", "apple"))

    # print(is_word_guessed("apple", ["l", "x", "p", "a"]))
    # print(get_guessed_word("apple", ["e", "i", "k", "p", "r", "s"]))
    # print(get_available_letters(["e", "i", "k", "p", "r", "s"]))
