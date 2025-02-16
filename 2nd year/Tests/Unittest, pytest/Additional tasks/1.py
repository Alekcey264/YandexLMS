import unittest
from yandex_testing_lesson import reverse


class TestReverse(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverse(''), '')
    
    def test_one(self):
        self.assertEqual(reverse('a'), 'a')

    def test_pal(self):
        self.assertEqual(reverse('abcba'), 'abcba')

    def test_def(self):
        self.assertEqual(reverse('abcde'), 'edcba')

    def test_wrong_type_uniter(self):
        with self.assertRaises(TypeError):
            reverse(42)

    def test_wrong_type_iter(self):
        with self.assertRaises(TypeError):
            reverse(['a', 'b', 'c'])


if __name__ == '__main__':
    unittest.main()