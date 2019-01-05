import unittest

from four_grid_points import FourGridPoints
from grid_point import GridPoint


class TestFourGridPoints(unittest.TestCase):
    def test_格子点集合が指定した格子点を含むか判定できる(self):
        p00 = GridPoint(0, 0)
        p11 = GridPoint(1, 1)
        p22 = GridPoint(2, 2)
        p33 = GridPoint(3, 3)
        p44 = GridPoint(4, 4)

        with self.subTest("含む"):
            self.assertTrue(FourGridPoints(p00, p11, p22, p33).contains(p33))

        with self.subTest("含まない"):
            self.assertFalse(FourGridPoints(p00, p11, p22, p33).contains(p44))

    def test_格子点集合に含まれる格子点の数を取得できる(self):
        p00 = GridPoint(0, 0)
        p11 = GridPoint(1, 1)
        p22 = GridPoint(2, 2)
        p33 = GridPoint(3, 3)

        self.assertEqual(4, FourGridPoints(p00, p11, p22, p33).count())

    def test_格子点集合の連結かどうかを判定できる(self):
        p01 = GridPoint(0, 1)
        p02 = GridPoint(0, 2)
        p03 = GridPoint(0, 3)
        p30 = GridPoint(3, 0)
        p20 = GridPoint(2, 0)
        p21 = GridPoint(2, 1)
        p00 = GridPoint(0, 0)
        p10 = GridPoint(1, 0)
        p11 = GridPoint(1, 1)
        p22 = GridPoint(2, 2)
        p33 = GridPoint(3, 3)

        with self.subTest("連結である_横に一直線"):
            self.assertTrue(FourGridPoints(p00, p01, p02, p03).is_connected())

        with self.subTest("連結である_縦に一直線"):
            self.assertTrue(FourGridPoints(p00, p10, p20, p30).is_connected())

        with self.subTest("連結である_L字"):
            self.assertTrue(FourGridPoints(p00, p10, p20, p21).is_connected())

        with self.subTest("連結である_T字"):
            self.assertTrue(FourGridPoints(p00, p10, p11, p20).is_connected())

        with self.subTest("連結でない_その1"):
            self.assertFalse(FourGridPoints(p00, p10, p11, p30).is_connected())

        with self.subTest("連結でない_その2"):
            self.assertFalse(FourGridPoints(p00, p11, p22, p33).is_connected())


if __name__ == "__main__":
    unittest.main()
