import unittest
from dataclasses import dataclass


@dataclass
class GridPoint:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        if (not isinstance(x, int)) or (not isinstance(y, int)):
            raise TypeError("Coordinate must be integer")

        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x},{self.y})"

    def has_same_coordinates_with(self, other) -> bool:
        return self.x == other.x and self.y == other.y


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


if __name__ == "__main__":
    unittest.main()
