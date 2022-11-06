from cipher_app.manager import Manager
import pytest


def test_execute_should_show_incorrect_input(capsys, mocker):
    user_input = 'kaks'
    Manager().execute(user_input)
    capture = capsys.readouterr()
    assert capture.out.strip() == 'Incorrect option'

