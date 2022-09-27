import sys

# Constants
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 3.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 5.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 6,
    },
}
COFFEE_LOGO = """
                       .
                        `:.
                          `:.
                  .:'     ,::
                 .:'      ;:'
                 ::      ;:'
                  :    .:'
                   `.  :.
          _________________________
         : _ _ _ _ _ _ _ _ _ _ _ _ :
     ,---:".".".".".".".".".".".".":
    : ,'"`::.:.:.:.:.:.:.:.:.:.:.::'
    `.`.  `:-===-===-===-===-===-:'
      `.`-._:                   :
        `-.__`.               ,' 
    ,--------`"`-------------'--------.
     `"--.__                   __.--"'
            `""-------------""'
"""


def resources_report(resources: dict) -> str:
    """
    Returns a string of the resources available in order to make a coffee.
    """
    available_resources = f"""
Water: {resources["water"]}ml,
Milk: {resources["milk"]}ml,
Coffee: {resources["coffee"]}g,
Money: ${resources["money"]}
    """

    return available_resources


def get_coffee_type(available_resources: dict) -> str:
    """
    Returns the coffee type specified by the user as a string.
    
    If the user inputs off, the program quits.
    If the user inputs report, resources_report is executed.
    """
    coffee_options = ["espresso", "latte", "cappuccino", "off"]
    chosen_coffee = None

    print("Welcome to the Coffee machine!")

    while chosen_coffee not in coffee_options:
        chosen_coffee = input(
            "\nWhat would you like? (espresso/latte/cappuccino): "
        ).lower()

        if chosen_coffee == "report":
            print(resources_report(available_resources))

    if chosen_coffee == "off":
        print("\nCoffee machine turning off...\n")
        sys.exit()

    return chosen_coffee


def processed_resources(chosen_coffee: str, available_resources: dict) -> bool:
    """
    Returns True if there are enough resources left to make the users coffee.
    """
    chosen_coffee_ingredients = MENU[chosen_coffee]["ingredients"]

    ingredients_set = ("water", "milk", "coffee")
    error = 0

    for ingredient in ingredients_set:
        if (
            chosen_coffee_ingredients[f"{ingredient}"]
            > available_resources[f"{ingredient}"]
        ):
            print(f"Sorry there is not enough {ingredient}.")
            error += 1
        else:
            available_resources[f"{ingredient}"] -= chosen_coffee_ingredients[
                f"{ingredient}"
            ]

    return error == 0


def processed_coins(chosen_coffee: str, available_resources: dict) -> bool:
    """
    Returns True if the user has deposited enough money for their coffee.
    """
    chosen_coffee_cost = MENU[chosen_coffee]["cost"]
    invalid_coins = True

    while invalid_coins:
        inserted_coins = input(
            f"{chosen_coffee} costs ${chosen_coffee_cost}.\nInsert coins: $"
        )
        try:
            inserted_coins = float(inserted_coins)
            invalid_coins = False
        except:
            pass

    if inserted_coins == chosen_coffee_cost:
        available_resources["money"] += inserted_coins
        print("\nThank you.")
        return True

    if inserted_coins > chosen_coffee_cost:
        available_resources["money"] += inserted_coins
        change = inserted_coins - chosen_coffee_cost
        print(f"Thank you.\nYou recieve ${change} in change.")
        return True

    print("\nSorry that's not enough money. Money refunded.")
    return False


def make_coffee(chosen_coffee: str, available_resources: dict) -> str:
    """
    Executes coin and resource processing.

    Returns the users coffee as a string if successful.
    """
    if processed_coins(chosen_coffee, available_resources):
        if processed_resources(chosen_coffee, available_resources):
            return f"\nHere is your {chosen_coffee}. Enjoy!\n☕\n\n"

    return "Please try again.\n\n"


def main() -> None:
    coffee_machine_operating = True
    available_resources = {"water": 300, "milk": 200, "coffee": 100, "money": 20}

    print(COFFEE_LOGO)

    while coffee_machine_operating:
        chosen_coffee = get_coffee_type(available_resources)
        print(make_coffee(chosen_coffee, available_resources))


if __name__ == "__main__":
    main()
