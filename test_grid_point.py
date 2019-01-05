import unittest

from grid_point import GridPoint


class TestGridPoint(unittest.TestCase):
    def test_格子点の文字列表記(self):
        self.assertEqual("(4,7)", str(GridPoint(4, 7)))

    def test_座標の値は整数であること(self):
        with self.subTest("x=1.5 -> Error"):
            self.assertRaises(TypeError, lambda: GridPoint(1.5, 7))

        with self.subTest("y=1.5 -> Error"):
            self.assertRaises(TypeError, lambda: GridPoint(7, 1.5))

    def test_格子点が同じ座標を持つかどうか判定できる(self):
        with self.subTest("(4,7) と (4,7) は 同じ座標"):
            self.assertTrue(GridPoint(4, 7).has_same_coordinates_with(GridPoint(4, 7)))

        with self.subTest("(4,7) と (3,8) は 違う座標"):
            self.assertFalse(GridPoint(4, 7).has_same_coordinates_with(GridPoint(3, 8)))

    def test_格子点が隣り合っているかどうか判定できる(self):
        origin_point = GridPoint(0, 0)

        with self.subTest("(1, 0) は (0, 0) と 隣り合う"):
            self.assertTrue(GridPoint(1, 0).is_neighbor_of(origin_point))

        with self.subTest("(-1, 0) は (0, 0) と 隣り合う"):
            self.assertTrue(GridPoint(-1, 0).is_neighbor_of(origin_point))

        with self.subTest("(0, 1) は (0, 0) と 隣り合う"):
            self.assertTrue(GridPoint(0, 1).is_neighbor_of(origin_point))

        with self.subTest("(0, -1) は (0, 0) と 隣り合う"):
            self.assertTrue(GridPoint(0, -1).is_neighbor_of(origin_point))


if __name__ == "__main__":
    unittest.main()
