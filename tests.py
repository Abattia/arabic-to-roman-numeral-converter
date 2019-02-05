# std lib imports
import unittest

# local imports
import arabic_to_roman as app

class ToRomanTestCase(unittest.TestCase):

    def test_converts_1_to_I(self):
        anArabic = 1

        result = app.to_roman(anArabic)

        self.assertEqual(result, "I")

    def test_converts_2_to_II(self):
        anArabic = 2

        result = app.to_roman(anArabic)

        self.assertEqual(result, "II")

    def test_converts_3_to_III(self):
        anArabic = 3

        result = app.to_roman(anArabic)

        self.assertEqual(result, "III")

    def test_converts_10_to_X(self):
        anArabic = 10

        result = app.to_roman(anArabic)

        self.assertEqual(result, "X")

    def test_converts_30_to_XXX(self):
        anArabic = 30

        result = app.to_roman(anArabic)

        self.assertEqual(result, "XXX")

    def test_converts_100_to_C(self):
        anArabic = 100

        result = app.to_roman(anArabic)

        self.assertEqual(result, "C")

    def test_converts_200_to_CC(self):
        anArabic = 200

        result = app.to_roman(anArabic)

        self.assertEqual(result, "CC")

    def test_converts_1000_to_M(self):
        anArabic = 1000

        result = app.to_roman(anArabic)

        self.assertEqual(result, "M")

    def test_converts_3232_to_MMMCCXXXII(self):
        anArabic = 3232

        result = app.to_roman(anArabic)

        self.assertEqual(result, "MMMCCXXXII")

    def test_converts_5_to_V(self):
        anArabic = 5

        result = app.to_roman(anArabic)

        self.assertEqual(result, "V")

    def test_converts_50_to_L(self):
        anArabic = 50

        result = app.to_roman(anArabic)

        self.assertEqual(result, "L")

    def test_converts_500_to_D(self):
        anArabic = 500

        result = app.to_roman(anArabic)

        self.assertEqual(result, "D")

    def test_converts_2768_to_MMDCCLXVIII(self):
        anArabic = 2768

        result = app.to_roman(anArabic)

        self.assertEqual(result, "MMDCCLXVIII")

    def test_converts_4_to_IV(self):
        anArabic = 4

        result = app.to_roman(anArabic)

        self.assertEqual(result, "IV")

    def test_converts_40_to_XL(self):
        anArabic = 40

        result = app.to_roman(anArabic)

        self.assertEqual(result, "XL")

    def test_converts_400_to_CD(self):
        anArabic = 400

        result = app.to_roman(anArabic)

        self.assertEqual(result, "CD")

    def test_converts_9_to_IX(self):
        anArabic = 9

        result = app.to_roman(anArabic)

        self.assertEqual(result, "IX")

    def test_converts_90_to_XC(self):
        anArabic = 90

        result = app.to_roman(anArabic)

        self.assertEqual(result, "XC")

    def test_converts_900_to_CM(self):
        anArabic = 900

        result = app.to_roman(anArabic)

        self.assertEqual(result, "CM")

    def test_converts_3491_to_MMMCDXCI(self):
        anArabic = 3491

        result = app.to_roman(anArabic)

        self.assertEqual(result, "MMMCDXCI")
if __name__ == "__main__":
    unittest.main(verbosity=2)
