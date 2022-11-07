from cipher_app.rot import *
import pytest


def test_encrypt_method_rot_13():
    encrypt_text = ROT13.encrypt('Tękst do sprawedzenia')
    assert encrypt_text == 'Eóuće ńa ćbckfońhoźśk'


def test_decrypt_method_rot_13():
    encrypt_text = ROT13.decrypt('Eóuće ńa ćbckfońhoźśk')
    assert encrypt_text == 'Tękst do sprawedzenia'


def test_encrypt_method_rot_47():
    encrypt_text = ROT47.encrypt('Tękst do sprawedzenia')
    assert encrypt_text == '%ę<DE 5@ DAC2H65K6?:2'


def test_decrypt__method_rot_47():
    encrypt_text = ROT47.decrypt('%ę<DE 5@ DAC2H65K6?:2')
    assert encrypt_text == 'Tękst do sprawedzenia'
