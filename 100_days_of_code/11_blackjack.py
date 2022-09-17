import random
import sys


def intro() -> str:
    """
    Blackjack ascii art and game start.
    """

    confirmation = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if confirmation != "y":
        sys.exit()

    logo = """
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
        |  \/ K|                            _/ |                
        `------'                           |__/           
    """

    return logo


def draw_card() -> int:
    available_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    distributed_card = random.choice(available_cards)

    return distributed_card


def hit() -> bool:
    selection_is_valid = False

    while not selection_is_valid:
        selection = input("Type 'y' to get another card, type 'n' to pass: ")
        if selection == "y" or selection == "n":
            break

    if selection == "y":
        return True

    if selection == "n":
        return False


def calculate_cards(user, computer) -> list:
    total = []

    user = int(sum(user))
    computer = int(sum(computer))

    return total


def determine_winner(calculate_cards: list) -> str:
    user = calculate_cards[0]
    computer = calculate_cards[1]

    if user > 21 and computer <= 21:
        return "lose."

    if user <= 21 and computer > 21:
        return "win." 

    if user <= 21 and computer <= 21:
        if user == computer:
            return "drew."


def user() -> list:
    card_list = []
    play = True

    for i in range(0, 2):
        card = draw_card()
        card_list.append(card)

    print(f"Your cards: {card_list}")

    while play:
        take_card = hit()
        if not take_card:
            break

        card = draw_card()
        card_list.append(card)

    return card_list


def computer() -> list:
    card_list = []
    card = draw_card()
    card_list.append(card)

    return card_list


def main() -> None:
    print(intro())

    run = user()
    print(run)    


if __name__ == "__main__":
    main()
