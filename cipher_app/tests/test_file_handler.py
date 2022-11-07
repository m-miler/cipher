from cipher_app.file_handler import FileHandler
from cipher_app.buffer import Buffer
import pytest


def test_save_to_file_should_create_new_file_and_write_text(tmpdir):
    file = tmpdir.join('text.txt')
    buffer = Buffer()
    buffer.add('Test Tekst 1')
    FileHandler.write_to_file(file.strpath, buffer)
    assert file.read() == 'Test Tekst 1\n'

