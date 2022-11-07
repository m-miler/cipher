from cipher_app.manager import Manager
import pytest


@pytest.fixture
def set_up():
    manager = Manager()
    return manager


def test_execute_should_show_incorrect_input(capsys, set_up):
    manager = set_up
    user_input = 'kaks'
    manager.execute(user_input)
    capture = capsys.readouterr()
    assert capture.out.strip() == 'Incorrect option'


