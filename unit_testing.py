import unittest
from spanish_numbers import SpanishNumbers


class TestNumbers(unittest.TestCase):
    def __init__(self, *args):
        super().__init__(*args)
        self.translator = SpanishNumbers()

    def test_teens(self):
        for num in range(10, 16):
            self.assertEqual(self.translator.number_to_text(str(num)), self.translator.exceptions.get(str(num)))


if __name__ == '__main__':
    unittest.main(verbosity=2)