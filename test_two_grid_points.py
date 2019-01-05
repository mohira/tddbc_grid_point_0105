import unittest

from grid_point import GridPoint
from two_grid_points import TwoGridPoints


class TestTwoGridPoints(unittest.TestCase):
    def test_格子点集合が指定した格子点を含むか判定できる(self):
        with self.subTest("含む"):
            p00 = GridPoint(0, 0)
            p11 = GridPoint(1, 1)

            self.assertTrue(TwoGridPoints(p00, p11).contains(p11))

        with self.subTest("含まない"):
            p00 = GridPoint(0, 0)
            p11 = GridPoint(1, 1)
            p22 = GridPoint(2, 2)

            self.assertFalse(TwoGridPoints(p00, p11).contains(p22))

    def test_格子点集合の連結してるか判定できる(self):
        with self.subTest("連結している場合"):
            p00 = GridPoint(0, 0)
            p10 = GridPoint(1, 0)

            self.assertTrue(TwoGridPoints(p00, p10).is_connected())

        with self.subTest("連結していない場合"):
            p00 = GridPoint(0, 0)
            p11 = GridPoint(1, 1)

            self.assertFalse(TwoGridPoints(p00, p11).is_connected())

    def test_格子点集合に含まれる格子点の数を取得できる(self):
        p00 = GridPoint(0, 0)
        p11 = GridPoint(1, 1)

        self.assertEqual(2, TwoGridPoints(p00, p11).count())


if __name__ == "__main__":
    unittest.main()
