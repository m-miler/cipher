from cipher_app.menu import Menu
import pytest


def test_should_print_menu_in_terminal(capsys):
    Menu.show()
    capture = capsys.readouterr()
    assert capture.out.strip() == "Menu:\n" \
                                  "1. Encrypt message\n" \
                                  "2. Decrypt message\n" \
                                  "3. Save encrypted messages to the chosen file\n" \
                                  "4. Read and decrypt message from file\n" \
                                  "5. Exit"


def test_should_return_user_input(mocker):
    mocker.patch('builtins.input', return_value=1)
    assert Menu.get_user_choice() == 1


def test_should_print_rot_menu_in_terminal(capsys, mocker):
    mocker.patch("builtins.input", return_value='1')
    cipher_type = Menu.show_rot_submenu()
    capture = capsys.readouterr()
    assert cipher_type == '1'
    assert capture.out.strip() == "Cipher list:\n" \
                                  "1. ROT13\n" \
                                  "2. ROT47"
