import random
import sys


# complete
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


# continue
def draw_card() -> int:
    available_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    distributed_card = random.choice(available_cards)

    return distributed_card


# complete
def hit_or_stand() -> bool:
    selection_is_not_valid = True

    while selection_is_not_valid:
        selection = input("Type 'y' to get another card, type 'n' to pass: ")
        if selection == "y" or selection == "n":
            selection_is_not_valid = False

    if selection == "y":
        return True

    if selection == "n":
        return False


# complete
def game_status(user: list, computer: list, final: bool) -> str:
    if final:
        return f"""
Your final hand: {user}
Computer's final hand: {computer}
        """

    if len(computer) == 1:
        return f"""
Your cards: {user}
Computer's first card: {computer[0]}
        """

    return f"""
Your cards: {user}
Computer's cards: {computer}
    """


# complete
def calculate_card_values(user: list, computer: list) -> list:
    total = []

    user = int(sum(user))
    computer = int(sum(computer))

    total.append(user)
    total.append(computer)

    return total


# complete
def determine_winner(calculate_card_values: list) -> str:
    user = calculate_card_values[0]
    computer = calculate_card_values[1]

    if user > 21 and computer <= 21:
        return "lose."

    if user <= 21 and computer > 21:
        return "win."

    if user <= 21 and computer <= 21:
        if user == computer:
            return "drew."

        if user > computer:
            return "win."

        if user < computer:
            return "lose."

    if user > 21 and computer > 21:
        return "drew."


# TODO optimize/ refactor
def main() -> None:
    computers_cards = []
    users_cards = []
    play = True
    final = False

    print(intro())

    while play:
        # if the game has just started:
        if len(users_cards) == 0:
            for i in range(2):
                user = draw_card()
                users_cards.append(user)

            computer = draw_card()
            computers_cards.append(computer)

            print(game_status(users_cards, computers_cards, final))

        # ask if user wants to draw card:
        play = hit_or_stand()

        # if the user doesnt want to draw another card:
        if not play:
            while int(sum(computers_cards)) <= 16:
                computer = draw_card()
                computers_cards.append(computer)
            final = True
            break

        # if user decides to draw another card:
        user = draw_card()
        users_cards.append(user)

        # if computers cards add to below 16, it draws another card
        if not int(sum(computers_cards)) > 15:
            computer = draw_card()
            computers_cards.append(computer)

        # if the users or computers cards add to above 21, if they have an 11, change the value to 1 instead.
        if int(sum(users_cards)) > 21:
            if 11 in users_cards:
                ace_index = users_cards.index(11)
                users_cards[ace_index] = 1
                if int(sum(computers_cards)) > 21:
                    if 11 in computers_cards:
                        ace_index = computers_cards.index(11)
                        computers_cards[ace_index] = 1

                        print(game_status(users_cards, computers_cards, final))
                        continue

                print(game_status(users_cards, computers_cards, final))
                continue

            final = True
            break

        print(game_status(users_cards, computers_cards, final))

    calculate_score = calculate_card_values(users_cards, computers_cards)
    result = determine_winner(calculate_score)

    print(game_status(users_cards, computers_cards, final))
    print(f"You {result}")


if __name__ == "__main__":
    main()
