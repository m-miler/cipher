from cipher_app.buffer import Buffer
from pathlib import Path


class FileHandler:
    @staticmethod
    def write_to_file(path: str, messages: Buffer) -> None:
        path = Path(path)
        with open(path, 'a') as file:
            for msg in messages.buffer:
                file.writelines(msg + '\n')
            file.close()

    @staticmethod
    def read_from_file(path: str) -> str:
        pass
