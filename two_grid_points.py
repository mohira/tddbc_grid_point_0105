from dataclasses import dataclass

from grid_point import GridPoint


@dataclass
class TwoGridPoints:
    p1: GridPoint
    p2: GridPoint

    def count(self) -> int:
        return 2

    def contains(self, p: GridPoint) -> bool:
        return self.p1.has_same_coordinates_with(p) or \
               self.p2.has_same_coordinates_with(p)

    def is_connected(self) -> bool:
        return self.p1.is_neighbor_of(self.p2)
