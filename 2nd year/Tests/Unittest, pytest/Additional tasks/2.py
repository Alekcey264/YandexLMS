from yandex_testing_lesson import reverse
import pytest

def test_empty():
    assert reverse('') == ''

def test_one():
    assert reverse('a') == 'a'

def test_pal():
    assert reverse('abcba') == 'abcba'

def test_def():
    assert reverse('abcde') == 'edcba'

def test_wrong_type_uniter():
    with pytest.raises(TypeError):
        reverse(4) 

def test_wrong_type_uniter():
    with pytest.raises(TypeError):
        reverse(['a', 'b', 'c']) 