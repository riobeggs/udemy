import operator


def intro() -> str:
    """
    Prints the logo.
    """

    logo = """
    _____________________
    |  _________________  |
    | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
    | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
    |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
    | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
    | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
    | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
    | |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
    | | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
    | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
    | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
    | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
    |_____________________|
    """

    return logo


def get_number(x: int) -> float:
    valid = False

    while not valid:
        try:
            if x == 1:
                number = float(input("What's the first number?: "))
                valid = True
            else:
                number = float(input("What's the next number?: "))
                valid = True
        except ValueError as error:
            print(error)

    return number


def get_operator() -> str:
    available_operators = ["+", "-", "*", "/"]
    chosen_operator = None

    for operator in available_operators:
        print(operator)

    while chosen_operator not in available_operators:
        chosen_operator = input("Pick an operation: ")

    return chosen_operator


def calculate_answer(
    first_number: int, chosen_operator: str, second_number: int
) -> float:
    ops_dict = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }

    answer = float(ops_dict[chosen_operator](first_number, second_number))

    return answer


def main() -> None:
    print(intro())

    first_number = get_number(1)
    chosen_operator = get_operator()
    second_number = get_number(2)
    answer = calculate_answer(first_number, chosen_operator, second_number)

    print(f"{first_number} {chosen_operator} {second_number} = {answer}\n")


if __name__ == "__main__":
    main()
