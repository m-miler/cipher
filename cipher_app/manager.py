from cipher_app.buffer import Buffer
from cipher_app.file_handler import FileHandler
from cipher_app.menu import Menu
from cipher_app.rot import ROT13, ROT47


class Manager:
    def __init__(self) -> None:
        self.__run: bool = True
        self.buffer = Buffer()
        self.__options = {
            "1": self.__encrypt_message,
            "2": self.__decrypt_message,
            "3": self.__save_to_the_file,
            "4": self.__decrypt_from_file,
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
        """ Execute options selected by user"""
        if user_input in self.__options:
            self.__options.get(user_input)()
        else:
            print("Incorrect option")

    def __get_cipher_type(self) -> str:
        """ Method for get user input for the cipher type and validate
            if user put correct option"""
        cipher_type: str = Menu.show_rot_submenu()
        if cipher_type in self.__rot_options:
            return cipher_type
        else:
            print('Incorrect option')

    def __encrypt_message(self) -> None:
        """ Method for encrypt user input message and save it to the buffer list than
            print out the success message with encrypted text """
        cipher_type: str = self.__get_cipher_type()
        if cipher_type:
            text_to_encrypt: str = input('Please write message to encrypt: ')
            encrypt_messages: str = self.__rot_options.get(cipher_type).encrypt(text_to_encrypt)
            self.buffer.add(encrypt_messages)
            print(f'Message has been encrypted! -- {encrypt_messages}')
        else:
            self.__encrypt_message()

    def __decrypt_message(self) -> None:
        """ Method for decrypt user input message and print out the success message with decrypted text """
        cipher_type: str = self.__get_cipher_type()
        if cipher_type:
            text_to_decrypt: str = input('Please write message to decrypt: ')
            decrypt_messages: str = self.__rot_options.get(cipher_type).decrypt(text_to_decrypt)
            print(f'Message has been decrypted! -- {decrypt_messages}')
        else:
            self.__decrypt_message()

    def __save_to_the_file(self) -> None:
        """ Method to save all encrypted messages from buffer to the provided file.
        If file already exist method will append result at the end. """
        user_path: str = input('Please provide absolute path to the file: ')
        FileHandler.write_to_file(user_path, self.buffer)

    def __decrypt_from_file(self) -> None:
        """ Method to read text from chosen file and decrypt it with selected cipher """
        user_path: str = input('Please provide absolute path to the file: ')
        texts_to_decrypt: list = FileHandler.read_from_file(user_path)
        if texts_to_decrypt:
            while True:
                cipher_type: str = self.__get_cipher_type()
                if cipher_type:
                    break
            decrypted_text: list = [self.__rot_options.get(cipher_type).decrypt(text) for text in texts_to_decrypt]
            return print(decrypted_text)
        else:
            self.__decrypt_from_file()


if __name__ == "__main__":
    Manager().start_app()
