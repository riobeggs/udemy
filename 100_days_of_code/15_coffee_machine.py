import sys

# Constants
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}


def resources_report(resources: dict, money: int = 0) -> str:
    available_resources = f"""
Water: {resources["water"]}ml,
Milk: {resources["milk"]}ml,
Coffee: {resources["coffee"]}g,
Money: ${money}
    """

    return available_resources


def resources_sufficient(chosen_coffee: str, available_resources: dict) -> bool:
    chosen_coffee_resources = MENU[chosen_coffee["ingredients"]]
    error = 0

    if chosen_coffee_resources["water"] > available_resources["water"]:
        print("Sorry there is not enough water.")
        error += 1

    if chosen_coffee_resources["milk"] > available_resources["milk"]:
        print("Sorry there is not enough milk.")
        error += 1

    if chosen_coffee_resources["coffee"] > available_resources["coffee"]:
        print("Sorry there is not enough coffee.")
        error += 1

    return error == 0


def make_coffee(chosen_coffee: str, available_resources: dict) -> str:
    if chosen_coffee == "espresso":
        if resources_sufficient(chosen_coffee, available_resources):
            pass

    if chosen_coffee == "latte":
        if resources_sufficient(chosen_coffee, available_resources):
            pass

    if chosen_coffee == "cappuccino":
        if resources_sufficient(chosen_coffee, available_resources):
            pass


def get_coffee_type(available_resources: dict) -> str:
    coffee_options = ["espresso", "latte", "cappuccino", "report", "off"]
    chosen_coffee = None

    while chosen_coffee not in coffee_options:
        chosen_coffee = input(
            "What would you like? (espresso/latte/cappuccino): "
        ).lower()

    if chosen_coffee == "report":
        print(resources_report(available_resources))

    if chosen_coffee == "off":
        print("Coffee machine turning off...")
        sys.exit()

    return chosen_coffee


def main() -> None:
    coffee_machine_operating = True
    available_resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }

    while coffee_machine_operating:
        chosen_coffee = get_coffee_type(available_resources)
        make_coffee(chosen_coffee, available_resources)


if __name__ == "__main__":
    main()
