from dataclasses import dataclass

from grid_point import GridPoint
from two_grid_points import TwoGridPoints


@dataclass
class ThreeGridPoints:
    p1: GridPoint
    p2: GridPoint
    p3: GridPoint

    def count(self) -> int:
        return 3

    def contains(self, p: GridPoint) -> bool:
        return self.p1.has_same_coordinates_with(p) or \
               self.p2.has_same_coordinates_with(p) or \
               self.p3.has_same_coordinates_with(p)

    def is_connected(self) -> bool:
        s1 = TwoGridPoints(self.p1, self.p2)
        s2 = TwoGridPoints(self.p2, self.p3)
        s3 = TwoGridPoints(self.p3, self.p1)

        # 3点が構成する 3つの 2点格子点集合 のうち ある2つの2点格子点集合が連結である
        return (s1.is_connected() and s2.is_connected()) or \
               (s2.is_connected() and s3.is_connected()) or \
               (s3.is_connected() and s1.is_connected())
