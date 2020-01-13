import unittest
from fraction import *

class TestFraction(unittest.TestCase):
    def test_gcd(self):
        print(gcd(9, 8))

    def test_init(self):
        fraction = Fraction(3, 5)
        self.assertEqual(fraction.num, 3)
        self.assertEqual(fraction.den, 5)

        frac = Fraction(3, -5)
        self.assertEqual(frac.getNum(), -3)

    def test_show(self):
        frac = Fraction(3, 5)
        print("show:")
        frac.show()
        print()

    def test_str(self):
        frac = Fraction(3, 5)
        print("str:", frac)
        print()

    def test_repr(self):
        frac = Fraction(3, 5)
        print("repr:", frac.__repr__())

    def test_add(self):
        frac = Fraction(3, 5)
        otherFrac = Fraction(3, 5)
        newFrac = frac + otherFrac
        self.assertEqual(str(newFrac), "6/5")

    def test_radd(self):
        frac = Fraction(3, 5)
        otherFrac = Fraction(3, 5)
        newFrac = otherFrac + frac
        self.assertEqual(str(newFrac), "6/5")

    def test_eq(self):
        frac = Fraction(3, 5)
        otherFrac = Fraction(3, 5)
        self.assertEqual(frac == otherFrac, True)

    def test_ne(self):
        frac = Fraction(3, 5)
        otherFrac = Fraction(2, 5)
        self.assertEqual(frac != otherFrac, True)

    def test_mul(self):
        frac = Fraction(3, 5)
        otherFrac = Fraction(3, 5)
        new = frac * otherFrac
        self.assertEqual(str(new), "9/25")

    def test_div(self):
        frac = Fraction(3, 5)
        otherFrac = Fraction(3, 5)
        new = frac / otherFrac
        self.assertEqual(str(new), "1/1")

    def test_sub(self):
        frac = Fraction(4, 5)
        otherFrac = Fraction(3, 5)
        new = frac - otherFrac
        self.assertEqual(str(new), "1/5")

    def test_gt(self):
        frac = Fraction(4, 5)
        otherFrac = Fraction(3, 5)
        new = frac > otherFrac
        self.assertEqual(new, True)

        new = otherFrac > frac
        self.assertEqual(new, False)

        frac = Fraction(4, 5)
        otherFrac = Fraction(4, 5)
        new = frac > otherFrac
        self.assertEqual(new, False)

    def test_ge(self):
        frac = Fraction(4, 5)
        otherFrac = Fraction(3, 5)
        new = frac >= otherFrac
        self.assertEqual(new, True)

        new = otherFrac >= frac
        self.assertEqual(new, False)

        frac = Fraction(4, 5)
        otherFrac = Fraction(4, 5)
        new = frac >= otherFrac
        self.assertEqual(new, True)


    def test_lt(self):
        frac = Fraction(4, 5)
        otherFrac = Fraction(3, 5)
        new = frac < otherFrac
        self.assertEqual(new, False)

        new = otherFrac < frac
        self.assertEqual(new, True)

    def test_le(self):
        frac = Fraction(4, 5)
        otherFrac = Fraction(3, 5)
        new = frac <= otherFrac
        self.assertEqual(new, False)

        new = otherFrac <= frac
        self.assertEqual(new, True)

        frac = Fraction(3, 5)
        otherFrac = Fraction(3, 5)
        b = frac <= otherFrac
        self.assertEqual(b, True)

    def test_getNum(self):
        frac = Fraction(3, 5)
        self.assertEqual(frac.getNum(), 3)

    def test_getDen(self):
        frac = Fraction(3, 5)
        self.assertEqual(frac.getDen(), 5)

if __name__ == '__main__':
    unittest.main()
