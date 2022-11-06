from typing import Any


class Menu:
    @staticmethod
    def show() -> None:
        print("Menu:")
        print("1. Encrypt message")
        print("2. Decrypt message")
        print("3. Save encrypted messages to the chosen file")
        print("4. Read and decrypt message from file")
        print("5. Exit\n")

    @staticmethod
    def get_user_choice() -> Any:
        user_input = input('Please select number from menu to execute --> ')
        return user_input

    @staticmethod
    def show_rot_submenu() -> Any:
        """ Function will show the menu on the screen to get user cipher method choose """
        print("Cipher list:")
        print("1. ROT13")
        print("2. ROT47")
        cipher_type = input("Please choose the cipher method: ")
        return cipher_type
