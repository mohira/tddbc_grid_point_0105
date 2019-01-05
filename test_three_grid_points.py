import unittest

from grid_point import GridPoint
from three_grid_points import ThreeGridPoints


class TestThreeGridPoints(unittest.TestCase):
    def test_格子点集合が指定した格子点を含むか判定できる(self):
        with self.subTest("含む"):
            p00 = GridPoint(0, 0)
            p11 = GridPoint(1, 1)
            p22 = GridPoint(2, 2)

            self.assertTrue(ThreeGridPoints(p00, p11, p22).contains(p22))

        with self.subTest("含まない"):
            p00 = GridPoint(0, 0)
            p11 = GridPoint(1, 1)
            p22 = GridPoint(2, 2)
            p33 = GridPoint(3, 3)

            self.assertFalse(ThreeGridPoints(p00, p11, p22).contains(p33))

    def test_格子点集合の連結している場合(self):
        p00 = GridPoint(0, 0)
        p01 = GridPoint(0, 1)
        p02 = GridPoint(0, 2)
        p10 = GridPoint(1, 0)
        p11 = GridPoint(1, 1)
        p20 = GridPoint(2, 0)
        p22 = GridPoint(2, 2)

        with self.subTest("連結である_左右に並ぶ"):
            self.assertTrue(ThreeGridPoints(p00, p10, p20).is_connected())

        with self.subTest("連結である_上下に並ぶ"):
            self.assertTrue(ThreeGridPoints(p00, p01, p02).is_connected())

        with self.subTest("連結である_L字に並ぶ"):
            self.assertTrue(ThreeGridPoints(p00, p01, p11).is_connected())

        with self.subTest("連結でない_どの格子点も隣り合っていない"):
            self.assertFalse(ThreeGridPoints(p00, p11, p22).is_connected())

        with self.subTest("連結でない_3つの格子点のうち、2点だけ隣り合う"):
            self.assertFalse(ThreeGridPoints(p00, p10, p22).is_connected())

    def test_格子点集合に含まれる格子点の数を取得できる(self):
        p00 = GridPoint(0, 0)
        p11 = GridPoint(1, 1)
        p22 = GridPoint(2, 2)

        self.assertEqual(3, ThreeGridPoints(p00, p11, p22).count())


if __name__ == "__main__":
    unittest.main()
