import random
import sys


# Constants
PERFECT_SCORE = 21  # perfect blackjack score
ACE = 11  # ace represented as 11 until score is over 21


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


def game_variables() -> dict:
    hands = {"users_hand": [], "computers_hand": []}
    return hands


def deal_starting_hands(users_hand: list, computers_hand: list) -> str:
    # deal starting hands
    for _ in range(2):
        add_card_to_hand(users_hand)
        add_card_to_hand(computers_hand)

    status = game_status(users_hand, computers_hand, hide_dealers_hand=True)

    return status


def user_plays(users_hand: list, computers_hand: list) -> bool:
    game_over = False

    while not game_over and sum(users_hand) < PERFECT_SCORE:
        players_title = "Your"
        # ask if user wants to draw card:
        new_card = hit()
        if new_card:
            add_card_to_hand(users_hand)
            if not sum(users_hand) >= PERFECT_SCORE:
                print(game_status(users_hand, computers_hand, hide_dealers_hand=True))
                continue
        users_score = sum(users_hand)
        if users_score > PERFECT_SCORE:
            if downgrade_aces(users_hand, players_title):
                print(game_status(users_hand, computers_hand, hide_dealers_hand=True))
                continue
            # if there are no aces in hand and hand is still over PERFECT_SCORE end game.
            game_over = True
        break

    return game_over


def computer_plays(users_hand: list, computers_hand: list) -> None:
    while computer_should_draw(computers_hand, sum(users_hand)):
        players_title = "Computer's"
        add_card_to_hand(computers_hand)
        computers_score = sum(computers_hand)
        if computers_score > PERFECT_SCORE:
            downgrade_aces(computers_hand, players_title)


def draw_card() -> int:
    """Draw a card from valid card selection and return its value as an integer."""
    available_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    distributed_card = random.choice(available_cards)
    return distributed_card


def add_card_to_hand(hand: list) -> None:
    """
    Draws a card and adds it to a players hand.

    returns none bacause lista are mutable
    shorturl.at/aSV07
    """
    card = draw_card()
    hand.append(card)


def hit() -> bool:
    """Take input from the user if they would like to hit or stand.

    Return a boolean indicating this."""
    VALID_SELECTIONS = ["y", "n"]
    selection_is_valid = False

    while not selection_is_valid:
        selection = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        selection_is_valid = selection in VALID_SELECTIONS

    if selection == "y":
        return True

    if selection == "n":
        return False


def computer_should_draw(computers_hand: list, users_score: int) -> bool:
    """
    determines if computer should draw another card.
    returns True if computers hand is less than the BREAKPOINT.
    """
    return sum(computers_hand) < users_score


def downgrade_aces(hand: list, player: str) -> bool:
    """
    Downgrades 11 to 1s if there are any but only hand is over 21.
    """
    if ACE in hand:
        ace_index = hand.index(ACE)
        hand[ace_index] = 1
        print(f"\n{player} ace/ 11 got downgraded to 1.")
        return True

    return False


def game_status(users_hand: list, computers_hand: list, hide_dealers_hand: bool = False) -> str:
    """Lets the user know what the game state is.

    Returns a string indicating the game state."""

    if not hide_dealers_hand:
        return f"""
Your cards: {users_hand} Your total = {sum(users_hand)} 
Computer's cards: {computers_hand} Computer's total = {sum(computers_hand)}
        """

    return f"""
Your cards: {users_hand} Your total = {sum(users_hand)}
Computer's cards: [{computers_hand[0]}, ?] Computer's total = {computers_hand[0]}
        """


def calculate_score(users_hand: list, computers_hand: list) -> list:
    """Calculate the score for each user and return a list.
    user_Score is 0 index, computer_score is 1 index"""
    total = []

    user_score = sum(users_hand)
    computer_score = sum(computers_hand)

    total.append(user_score)
    total.append(computer_score)

    return total


def determine_winner(calculate_card_values: list) -> str:
    """Based on scores, determine who won the round. Returns result as a string."""
    user = calculate_card_values[0]
    computer = calculate_card_values[1]
    result = None

    if user > PERFECT_SCORE:
        result = "lose."

    elif user <= PERFECT_SCORE and computer > PERFECT_SCORE:
        result = "win."

    elif user <= PERFECT_SCORE and computer <= PERFECT_SCORE:
        if user == computer:
            result = "drew."

        elif user > computer:
            result = "win."

        elif user < computer:
            result = "lose."

    elif user > PERFECT_SCORE and computer > PERFECT_SCORE:
        result = "drew."

    return result


def main() -> None:
    print(intro())

    hands = game_variables()
    users_hand = hands["users_hand"]
    computers_hand = hands["computers_hand"]

    print(deal_starting_hands(users_hand, computers_hand))
    game_over = user_plays(users_hand, computers_hand)
    if not game_over:
        computer_plays(users_hand, computers_hand)

    score = calculate_score(users_hand, computers_hand)
    result = determine_winner(score)

    print(game_status(users_hand, computers_hand))
    print(f"You {result}")


if __name__ == "__main__":
    main()
