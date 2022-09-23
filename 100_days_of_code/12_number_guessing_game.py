# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


def intro() -> str:
    logo = """
  ____                       _   _            _   _                 _               
 / ___|_   _  ___  ___ ___  | |_| |__   ___  | \ | |_   _ _ __ ___ | |__   ___ _ __ 
| |  _| | | |/ _ \/ __/ __| | __| '_ \ / _ \ |  \| | | | | '_ ` _ \| '_ \ / _ \ '__|
| |_| | |_| |  __/\__ \__ \ | |_| | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
 \____|\__,_|\___||___/___/  \__|_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|  
    """

    return f"""{logo}
Welcome to the number guessing game!
I am thinking of a number between 1 and 100."""


def difficulty() -> int:
    difficulty_options = {"easy": 10, "hard": 5}
    chosen_difficulty = None

    while chosen_difficulty not in difficulty_options:
        chosen_difficulty = input(
            "Choose a difficulty. Type 'easy' or 'hard': "
        ).lower()

    chosen_difficulty = difficulty_options[chosen_difficulty]

    return chosen_difficulty


def main() -> None:
    print(intro())
    chosen_difficulty = difficulty()


if __name__ == "__main__":
    main()
