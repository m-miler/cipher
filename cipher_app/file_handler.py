from cipher_app.buffer import Buffer
import os


class FileHandler:
    @staticmethod
    def write_to_file(path: str, messages: Buffer) -> None:
        path = fr'{path}'
        with open(path, 'a') as file:
            for msg in messages.buffer:
                file.writelines(msg + '\n')

    @staticmethod
    def read_from_file(path: str) -> str:
        pass
