from cipher_app.buffer import Buffer
from cipher_app.menu import Menu
from cipher_app.rot import ROT13, ROT47


class Manager:
    def __init__(self) -> None:
        self.__run: bool = True
        self.buffer = Buffer()
        self.__options = {
            "1": self.__encrypt_message,
            "2": self.__decrypt_message,
            "5": self.__exit_app
        }
        self.__rot_options = {
            "1": ROT13,
            "2": ROT47,
        }

    def start_app(self) -> None:
        Menu.show()
        while self.__run:
            user_input = Menu.get_user_choice()
            self.execute(user_input)

    def __exit_app(self) -> None:
        self.__run = False

    def execute(self, user_input) -> None:
        if user_input in self.__options:
            self.__options.get(user_input)()
        else:
            print("Incorrect option")

    def __encrypt_message(self) -> None:
        """ Method for encrypt user input message and save it to the buffer list than
            print out the success message with encrypted messages """
        cipher_type: str = Menu.show_rot_submenu()
        if cipher_type in self.__rot_options:
            text_to_encrypt: str = input('Please write message to encrypt: ')
            encrypt_messages: str = self.__rot_options.get(cipher_type).encrypt(text_to_encrypt)
            self.buffer.add(encrypt_messages)
            print(f'Message has been encrypted! -- {encrypt_messages}')
        elif cipher_type == str(len(self.__rot_options) + 1):
            return
        else:
            print('Incorrect option')
            self.__encrypt_message()

    def __decrypt_message(self) -> None:
        """ Method for decrypt user input message and print out the success message with encrypted messages """
        cipher_type: str = Menu.show_rot_submenu()
        if cipher_type in self.__rot_options:
            text_to_decrypt: str = input('Please write message to decrypt: ')
            decrypt_messages: str = self.__rot_options.get(cipher_type).decrypt(text_to_decrypt)
            print(f'Message has been decrypted! -- {decrypt_messages}')
        elif cipher_type == str(len(self.__rot_options) + 1):
            return
        else:
            print('Incorrect option')
            self.__decrypt_message()


if __name__ == "__main__":
    Manager().start_app()
