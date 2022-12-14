class Menu:
    @staticmethod
    def show() -> None:
        print("Menu:")
        print("1. Encrypt message")
        print("2. Decrypt message")
        print("3. Save encrypted messages to the chosen file")
        print("4. Read and decrypt message from file")
        print("5. Exit")

    @staticmethod
    def get_user_choice() -> str:
        user_input = input('\nPlease select number from menu to execute --> ')
        return user_input

    @staticmethod
    def show_rot_submenu() -> str:
        """ Function will show the menu on the screen to get user cipher method choose """
        print("\nCipher list:")
        print("1. ROT13")
        print("2. ROT47")
        cipher_type = input("Please choose the cipher method: ")
        return cipher_type
