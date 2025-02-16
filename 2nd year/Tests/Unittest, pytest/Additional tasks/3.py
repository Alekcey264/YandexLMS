import pytest
from yandex_testing_lesson import count_chars


def test_empty():
    assert count_chars('') == dict()

def test_one():
    assert count_chars('a') == {'a': 1}

def test_def():
    assert count_chars('asdla') == {'a': 2, 's': 1, 'd': 1, 'l': 1}

def test_wrong_type_uniter():
    with pytest.raises(TypeError):
        count_chars(43)

def test_wrong_type_iter():
    with pytest.raises(TypeError):
        count_chars(['a', 'n', 'c'])

def test_with_spec_symb():
    assert count_chars('aaaaaa,') == {'a': 6, ',': 1}