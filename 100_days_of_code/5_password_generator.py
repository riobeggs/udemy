# Password Generator Project
import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("\nWelcome to the PyPassword Generator!")
number_of_letters = int(input("How many letters would you like in your password?\n"))
number_of_numbers = int(input("How many numbers would you like?\n"))
number_of_symbols = int(input("How many symbols would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


def letter_gen(letters: str, number_of_letters: int) -> str:
    chosen_letters = []

    for i in range(number_of_letters):
        letter = random.choice(letters)
        chosen_letters.append(letter)

    return chosen_letters


def number_gen(numbers: str, number_of_numbers: int) -> str:
    chosen_numbers = []

    for i in range(number_of_numbers):
        number = random.choice(numbers)
        chosen_numbers.append(number)

    return chosen_numbers


def symbol_gen(symbols: str, number_of_symbols: int) -> str:
    chosen_symbols = []

    for i in range(number_of_symbols):
        symbol = random.choice(symbols)
        chosen_symbols.append(symbol)

    return chosen_symbols


def password_gen(chosen_letters: str, chosen_numbers: str, chosen_symbols: str) -> str:
    character_list = []

    for letter in chosen_letters:
        character_list.append(letter)

    for number in chosen_numbers:
        character_list.append(number)

    for symbol in chosen_symbols:
        character_list.append(symbol)

    password = "".join(random.sample(character_list, len(character_list)))

    return password


def main() -> None:
    chosen_letters = letter_gen(letters, number_of_letters)
    chosen_numbers = number_gen(numbers, number_of_numbers)
    chosen_symbols = number_gen(symbols, number_of_symbols)
    password = password_gen(chosen_letters, chosen_numbers, chosen_symbols)

    print(f"Here is your password: {password}\n")


if __name__ == "__main__":
    main()
