from cipher_app.buffer import Buffer
from pathlib import Path


class FileHandler:
    @staticmethod
    def write_to_file(path: str, messages: Buffer) -> None:
        path = Path(path)
        with open(path, 'a', encoding="utf-8") as file:
            for msg in messages.buffer:
                file.writelines(msg + '\n')
            file.close()
            print('All messages have been saved!')

    @staticmethod
    def read_from_file(path: str) -> list:
        path = Path(path)
        try:
            with open(path, 'r', encoding="utf-8") as file:
                text_to_decrypt = [line.strip() for line in file.readlines()]
            return text_to_decrypt
        except FileNotFoundError as err:
            print(err)

