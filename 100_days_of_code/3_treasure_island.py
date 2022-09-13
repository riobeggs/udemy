print(
    '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''
)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


# Write your code below this line 👇
def left(crossroad: str) -> bool:
    if crossroad == "left":
        lake = input(
            'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n'
        )

        if lake == "swim":
            print(
                "The island was further away than you thought. You drowned trying to swim there.\n"
            )
            return False
        if lake == "wait":
            door = input(
                "The boat arrives and takes you to the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n"
            )

            if door == "red":
                print("It's a room full of fire.\n")
                return False
            if door == "yellow":
                print("You found the treasure!\n")
                return True
            if door == "blue":
                print("You enter a room of beasts.\n")
                return False
            print("You chose a door that doesn't exist.\n")
            return False


def right(crossroad: str) -> bool:
    if crossroad == "right":
        weapon = input(
            "You get attacked by an angry trout. Choose your weapon: paper, scissors, rock.\n"
        )

        if weapon == "paper":
            print(
                "The trout happens to love paper. He guides you to an island in trade for your paper!"
            )
            door = input(
                "You arrive at the island and there is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n"
            )

            if door == "red":
                print("It's a room full of fire.\n")
                return False
            if door == "yellow":
                print("You found the treasure!\n")
                return True
            if door == "blue":
                print("You enter a room of beasts.\n")
                return False
            print("You chose a door that doesn't exist.\n")
            return False

        if weapon == "scissors":
            print("The trout ate you and your scissors.\n")
            return False
        if weapon == "rock":
            print("The trout ate you and your rock.\n")
            return False


def main() -> None:
    crossroad = input(
    'You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n'
)

    if crossroad == "left":
        won = left(crossroad)
        if won:
            print("You win.")
        else:
            print("You lose.")

    if crossroad == "right":
        won = right(crossroad)
        if won:
            print("You win.")
        else:
            print("You lose.")


if __name__ == "__main__":
    main()