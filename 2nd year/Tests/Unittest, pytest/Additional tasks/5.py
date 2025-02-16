import pytest
from yandex_testing_lesson import Rectangle


def test_empty():
    with pytest.raises(TypeError):
        Rectangle(None, None)


def test_wrong_type_iter_first():
    with pytest.raises(TypeError):
        Rectangle('ab', 5)


def test_wrong_type_iter_second():
    with pytest.raises(TypeError):
        Rectangle(5, 'ab')


def test_wrong_type_iter_both():
    with pytest.raises(TypeError):
        Rectangle('ab', 'as')


def test_wrong_value_first():
    with pytest.raises(ValueError):
        Rectangle(-1, 2)


def test_wrong_value_second():
    with pytest.raises(ValueError):
        Rectangle(2, -1)


def test_wrong_value_both():
    with pytest.raises(ValueError):
        Rectangle(-1, -5)


def test_cor_area_zero_first():
    r = Rectangle(0, 5)
    assert r.get_area() == 0


def test_cor_area_zero_second():
    r = Rectangle(5, 0)
    assert r.get_area() == 0


def test_cor_area_good():
    r = Rectangle(4, 5)
    assert r.get_area() == 20


def test_cor_perim_zero_first():
    r = Rectangle(0, 5)
    assert r.get_perimeter() == 10


def test_cor_perim_zero_second():
    r = Rectangle(5, 0)
    assert r.get_perimeter() == 10


def test_cor_perim_good():
    r = Rectangle(4, 5)
    assert r.get_perimeter() == 18