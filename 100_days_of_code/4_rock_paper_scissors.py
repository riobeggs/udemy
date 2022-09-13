rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Write your code below this line 👇
import random


def users_choice(options) -> str:
    while True:
        choice = input(
            "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
        )

        try:
            return options[int(choice)]
        except:
            continue


def computers_choice(options) -> str:
    choice = random.randrange(0, 3)
    return (options[int(choice)])


def game_result(user, computer) -> str:
    win = "You win."
    lose = "You lose."
    draw = "You drew."


    if user == rock:
        if computer == scissors:
            return win
        elif computer == paper:
            return lose
        return draw

    if user == paper:
        if computer == rock:
            return win
        elif computer == scissors:
            return lose
        return draw

    if user == scissors:
        if computer == paper:
            return win
        elif computer == rock:
            return lose
        return draw


def main() -> None:
    options = [rock, paper, scissors]

    user = users_choice(options)
    print(f"\nYou chose:\n{user}")

    computer = computers_choice(options)
    print(f"\nComputer chose:\n{computer}")

    result = game_result(user, computer)
    print(result)


if __name__ == "__main__":
    main()
