from cipher_app.file_handler import FileHandler
from cipher_app.buffer import Buffer
import pytest


def test_save_to_file_should_create_new_file_and_write_text(tmpdir, capsys):
    file = tmpdir.join('text.txt')
    buffer = Buffer()
    buffer.add('Test Tekst 1')
    FileHandler.write_to_file(file.strpath, buffer)
    capture = capsys.readouterr()
    assert file.read() == 'Test Tekst 1\n'
    assert capture.out.strip() == 'All messages have been saved!'


def test_read_from_file_should_return_list_with_all_lines_from_file(tmpdir):
    file = tmpdir.join('test.txt')
    with open(file.strpath, 'w', encoding="utf-8") as f:
        for i in range(4):
            f.writelines('Eóuće ńa ćbckfońhoźśk\n')
    text_to_decrypt = FileHandler.read_from_file(file.strpath)
    assert text_to_decrypt == ['Eóuće ńa ćbckfońhoźśk',
                               'Eóuće ńa ćbckfońhoźśk',
                               'Eóuće ńa ćbckfońhoźśk',
                               'Eóuće ńa ćbckfońhoźśk']