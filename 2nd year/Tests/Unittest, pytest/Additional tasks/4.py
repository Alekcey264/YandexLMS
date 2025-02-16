import pytest

from yandex_testing_lesson import is_under_queen_attack


def test_empty_first():
    with pytest.raises(ValueError):
        is_under_queen_attack('', 'e5')


def test_empty_second():
    with pytest.raises(ValueError):
        is_under_queen_attack('e5', '')


def test_empty_both():
    with pytest.raises(ValueError):
        is_under_queen_attack('', '')
    

def test_wrong_type_uniter_first():
    with pytest.raises(TypeError):
        is_under_queen_attack(42, 'e5')


def test_wrong_type_uniter_second():
    with pytest.raises(TypeError):
        is_under_queen_attack('e5', 52)


def test_wrong_type_uniter_both():
    with pytest.raises(TypeError):
        is_under_queen_attack(42, 62)


def test_wrong_type_iter_first():
    with pytest.raises(TypeError):
        is_under_queen_attack(['a', '2'], 'e5')


def test_wrong_type_iter_second():
    with pytest.raises(TypeError):
        is_under_queen_attack('e5', ['a', '2'])


def test_wrong_type_iter_both():
    with pytest.raises(TypeError):
        is_under_queen_attack(['a', '2'], ['b', '3'])


def test_def_true():
    assert is_under_queen_attack('g6', 'e6')


def test_def_false():
    assert not is_under_queen_attack('g6', 'f4')


def test_def_same_point():
    assert is_under_queen_attack('g6', 'g6')