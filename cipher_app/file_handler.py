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
        with open(path, 'r', encoding="utf-8") as file:
            lines = file.readlines()
        test_to_decrypt = [line.strip() for line in lines]
        return test_to_decrypt


if __name__ == "__main__":
    print(FileHandler.read_from_file('test.txt'))
