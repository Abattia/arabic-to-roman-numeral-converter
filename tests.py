# std lib imports
import unittest

# local imports
import roman_numerals as app

class RomanNumeralsConverterTestCase(unittest.TestCase):

    def test_returns_I_when_arabic_is_1(self):
        arabic = 1

        result = app.convert_to_roman(arabic)

        self.assertEqual(result, "I")

    def test_returns_II_when_arabic_is_2(self):
        arabic = 2

        result = app.convert_to_roman(arabic)

        self.assertEqual(result, "II")

    def test_returns_III_when_arabic_is_3(self):
        arabic = 3

        result = app.convert_to_roman(arabic)

        self.assertEqual(result, "III")

    def test_returns_X_when_arabic_is_10(self):
        arabic = 10

        result = app.convert_to_roman(arabic)

        self.assertEqual(result, "X")

    def test_returns_X1_when_arabic_is_11(self):
        arabic = 11

        result = app.convert_to_roman(arabic)

        self.assertEqual(result, "XI")

    def test_returns_XX_when_arabic_is_20(self):
        arabic = 20

        result = app.convert_to_roman(arabic)

        self.assertEqual(result, "XX")

    def test_returns_C_when_arabic_is_100(self):
        arabic = 100

        result = app.convert_to_roman(arabic)

        self.assertEqual(result, "C")

    def test_returns_CXIII_when_arabic_is_113(self):
        arabic = 113

        result = app.convert_to_roman(arabic)

        self.assertEqual(result, "CXIII")

    def test_returns_M_when_arabic_is_1000(self):
        arabic = 1000

        result = app.convert_to_roman(arabic)

        self.assertEqual(result, "M")


if __name__ == "__main__":
    unittest.main(verbosity=2)
