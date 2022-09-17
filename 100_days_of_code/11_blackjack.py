import random


def intro() -> str:
    """
    Blackjack ascii art.
    """

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


def user() -> None:
    pass


def computer() -> None:
    pass


def main() -> None:
    print(intro())

    card = draw_card()


if __name__ == "__main__":
    main()
