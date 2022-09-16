logo = '''          
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
'''

alphabet = [
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
]


def caesar(start_text: str, shift_amount: int, cipher_direction: str) -> str:
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        try:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        except:
            end_text += char

    return end_text


def confirm_restart() -> bool:
    confirm = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if confirm == "yes":
        return True

    return False


def get_direction() -> str:
    restart = True

    while restart:
        valid = ["encode", "decode"]

        direction = input(
            "Type 'encode' to encrypt, type 'decode' to decrypt:\n"
        ).lower()
        print()

        if direction in valid:
            restart = False

        if direction == "restart":
            confirmed = confirm_restart()
            if not confirmed:
                restart = False

    return direction


def get_text() -> str:
    restart = True

    while restart:
        text = input("Type your message:\n").lower()
        print()
        if text == "restart":
            confirmed = confirm_restart()
            if not confirmed:
                restart = False
        restart = False

    return text


def valid_shift(text: str, shift: int) -> bool:
    try:
        shift = int(shift)
        for letter in text:
            if (alphabet.index(letter)) + shift > len(alphabet):
                return False
        return True
    except:
        return False


""" 
TODO: 
find a way to loop indexing through alphabet if shift + letterindex > 26
"""


def get_shift(text: str) -> int:
    restart = True

    while restart:
        shift = input("Type the shift number:\n")
        print()
        valid = valid_shift(text, shift)
        if valid:
            return int(shift)


def main() -> None:
    print(logo)

    direction = get_direction()
    text = get_text()
    shift = get_shift(text)

    end_text = caesar(text, shift, direction)
    print(f"Here's the {direction}d result: {end_text}\n")


if __name__ == "__main__":
    main()
