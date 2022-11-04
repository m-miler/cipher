import string
from abc import ABC, abstractmethod


class ROT(ABC):

    @staticmethod
    @abstractmethod
    def encrypt(text: str, shift: int) -> str:
        return NotImplemented

    @staticmethod
    @abstractmethod
    def decrypt(text: str, shift: int) -> str:
        return NotImplemented


class ROT13(ROT):

    @staticmethod
    def encrypt(text: str, shift: int = 13) -> str:
        alphabet = 'AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ'
        encrypt_text: str = ''
        for letter in text:
            if letter.upper() not in alphabet:
                encrypt_text += letter
            elif letter.isupper():
                encrypt_text += alphabet[(alphabet.index(letter) + shift) % len(alphabet)]
            else:
                encrypt_text += alphabet[(alphabet.lower().index(letter) + shift) % len(alphabet)].lower()
        return encrypt_text

    @staticmethod
    def decrypt(text: str, shift: int = 13) -> str:
        return ROT13.encrypt(text, -shift)


class ROT47(ROT):
    @staticmethod
    def encrypt(text: str, shift: int = 47) -> str:
        encrypt_text: str = ''
        for letter in text:
            if 33 <= ord(letter) <= 126:
                encrypt_text += chr(33 + (ord(letter) + 14) % 94)
            else:
                encrypt_text += letter
        return encrypt_text

    @staticmethod
    def decrypt(text: str, shift: int = 47) -> str:
        return ROT47.encrypt(text)

