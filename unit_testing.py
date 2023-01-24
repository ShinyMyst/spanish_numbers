import unittest
from spanish_numbers import SpanishNumbers


class TestNumbers(unittest.TestCase):
    def __init__(self, *args):
        super().__init__(*args)
        self.translator = SpanishNumbers()

    def test_teens(self):
        for num in range(10, 16):
            self.assertEqual(self.translator.number_to_text(str(num)), self.translator.exceptions.get(str(num)))

    def test_twenties(self):
        self.assertEqual(self.translator.number_to_text(str('27')), 'veintisiete')

    def test_regular_tens(self):
        self.assertEqual(self.translator.number_to_text(str('42')), 'cuarenta y dos')
    
    def test_one_hundred(self):
        self.assertEqual(self.translator.number_to_text(str('100')), 'cien')
    
    def test_regular_hundreds(self):
        self.assertEqual(self.translator.number_to_text(str('200')), 'doscientos')

    def test_five_hundred(self):
        self.assertEqual(self.translator.number_to_text(str('500')), 'quinientos')

    def test_mixed_hundreds(self):
        self.assertEqual(self.translator.number_to_text(str('138')), 'ciento treinta y ocho')


if __name__ == '__main__':
    unittest.main(verbosity=2)