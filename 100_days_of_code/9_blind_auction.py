import os


def intro() -> str:
    logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
    return logo + "\nWelcome to the secret auction program.\n"


def get_bid() -> list:
    bid_list = []
    valid_bid = False

    name = input("What is your name?: ")

    while valid_bid == False:
        try:
            bid = int(input("What is your bid?: $"))
            if bid >= 0:
                valid_bid = True
        except:
            continue

    bid_list.append(name)
    bid_list.append(bid)

    return bid_list


def bidders() -> True:
    other_bidders = True
    bidders = None
    options = ["yes", "no"]

    while bidders not in options:
        bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if bidders == "no":
        other_bidders = False

    return other_bidders


def calculate_bids(bids: dict) -> str:
    highest_bidder = max(bids, key=bids.get)
    amount_bid = bids[highest_bidder]

    return f"\nThe winner is {highest_bidder.capitalize()} with a bid of ${amount_bid}.\n"


def main() -> None:
    print(intro())

    other_bidders = True
    bids = {}

    while other_bidders:
        bid_list = get_bid()
        bids[bid_list[0]] = bid_list[1]
        other_bidders = bidders()

        if other_bidders:
            os.system("clear")

    print(calculate_bids(bids))


if __name__ == "__main__":
    main()
