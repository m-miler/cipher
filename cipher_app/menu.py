from typing import Any


class Menu:
    @staticmethod
    def show() -> None:
        print("Menu:")
        print("1. Encrypt message (ROT13, ROT47)")
        print("2. Decrypt message (ROT13, ROT47)")
        print("3. Save encrypted messages to the chosen file")
        print("4. Read and decrypt text from file")
        print("5. Exit")

    @staticmethod
    def get_user_choice() -> Any:
        user_input = input('Please select number from menu to execute --> ')
        return user_input

