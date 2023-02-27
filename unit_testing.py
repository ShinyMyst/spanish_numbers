import unittest
from spanish_numbers import SpanishNumbers


class TestNumbers(unittest.TestCase):
    def __init__(self, *args):
        super().__init__(*args)
        self.translator = SpanishNumbers()

    def test_teens(self):
        for num in range(10, 16):
            expected_dict = self.translator.number_to_text(str(num))
            function_result = self.translator.exceptions.get(str(num))
            self.assertEqual(expected_dict, function_result)

    def test_twenties(self):
        compare = self.translator.number_to_text(str('27')), 'veintisiete'
        self.assertEqual(*compare)

    def test_regular_tens(self):
        compare = self.translator.number_to_text(str('42')), 'cuarenta y dos'
        self.assertEqual(*compare)

    def test_one_hundred(self):
        compare = self.translator.number_to_text(str('100')), 'cien'
        self.assertEqual(*compare)

    def test_regular_hundreds(self):
        compare = self.translator.number_to_text(str('200')), 'doscientos '
        self.assertEqual(*compare)

    def test_five_hundred(self):
        compare = self.translator.number_to_text(str('500')), 'quinientos '
        self.assertEqual(*compare)

    def test_mixed_hundreds(self):
        translator = self.translator.number_to_text(str('138'))
        expected = 'ciento treinta y ocho'
        compare = translator, expected
        self.assertEqual(*compare)


if __name__ == '__main__':
    unittest.main(verbosity=2)
