from cipher_app.buffer import Buffer
import pytest


def test_add_method_should_append_list():
    text_1 = 'Text1'
    text_2 = 'Text2'
    buffer = Buffer()
    buffer.add(text_1)
    buffer.add(text_2)
    assert buffer.buffer == [text_1, text_2]


def test_remove_method_should_remove_all_list_elements():
    text_1 = 'Text1'
    text_2 = 'Text2'
    buffer = Buffer()
    buffer.add(text_1)
    buffer.add(text_2)
    buffer.clear()
    assert buffer.buffer == []

