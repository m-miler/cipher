from cipher_app.menu import Menu
import pytest


def test_should_print_menu_in_terminal(capsys):
    Menu.show()
    capture = capsys.readouterr()
    assert capture.out.strip() == "Menu:\n" \
                                  "1. Encrypt message (ROT13, ROT47)\n" \
                                  "2. Decrypt message (ROT13, ROT47)\n" \
                                  "3. Save encrypted messages to the chosen file\n" \
                                  "4. Read and decrypt text from file\n" \
                                  "5. Exit"


def test_should_return_user_input(mocker):
    mocker.patch('builtins.input', return_value=1)
    assert Menu.get_user_choice() == 1
