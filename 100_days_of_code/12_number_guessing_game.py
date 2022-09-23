import random


def intro() -> str:
    """
    Prints game logo and provides game information.
    """

    logo = """
  ____                       _   _            _   _                 _               
 / ___|_   _  ___  ___ ___  | |_| |__   ___  | \ | |_   _ _ __ ___ | |__   ___ _ __ 
| |  _| | | |/ _ \/ __/ __| | __| '_ \ / _ \ |  \| | | | | '_ ` _ \| '_ \ / _ \ '__|
| |_| | |_| |  __/\__ \__ \ | |_| | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
 \____|\__,_|\___||___/___/  \__|_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|  
    """

    return f"""{logo}
Welcome to the number guessing game!
I am thinking of a number between 1 and 100.
"""


def difficulty() -> int:
    """
    Asks the user to choose the difficulty.

    returns an integer relative to the amount of guesses they get for the chosen difficulty.
    """

    difficulty_options = {"easy": 10, "hard": 5}
    chosen_difficulty = None

    while chosen_difficulty not in difficulty_options:
        chosen_difficulty = input(
            "Choose a difficulty. Type 'easy' or 'hard': "
        ).lower()

    chosen_difficulty = difficulty_options[chosen_difficulty]

    return chosen_difficulty


def chosen_number() -> int:
    """
    A random number between 1 and 100 is selected.

    returns number as an integer.
    """

    number = random.randrange(1, 101)

    return number


def guess(guesses_left: int, answer: int) -> int:
    """
    Takes the users guess as an input.
    Lets the user know how many guesses they have left and hints relative to the answer.

    returns the users guess as an integer.
    """

    for guess_number in range(guesses_left):
        valid_guess = False
        print(
            f"\nYou have {guesses_left - guess_number} attempts remaining to guess the number."
        )

        while not valid_guess:
            guess = input("Make a guess: ")
            if int(guess):
                guess = int(guess)
                valid_guess = True

        if guess < answer:
            print("Too low.")

        if guess > answer:
            print("Too high.")

        if guess == answer:
            return guess

    return guess


def results(users_guess: bool, answer: int) -> str:
    """
    returns a string that lets user know if they guessed the correct number or not.
    """

    computers_number = f"The answer was {answer}."

    if users_guess == answer:
        return "You got it! " + computers_number

    return "You've run out of guesses, you lose. " + computers_number


def main() -> None:
    print(intro())

    guesses_left = difficulty()
    answer = chosen_number()
    users_guess = guess(guesses_left, answer)

    print(results(users_guess, answer))


if __name__ == "__main__":
    main()
