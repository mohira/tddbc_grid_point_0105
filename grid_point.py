from __future__ import annotations

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

    def has_same_coordinates_with(self, other: GridPoint) -> bool:
        return self.x == other.x and self.y == other.y

    def is_neighbor_of(self, other: GridPoint) -> bool:
        return ((self.x == other.x + 1) and (self.y == other.y)) \
               or ((self.x == other.x - 1) and (self.y == other.y)) \
               or ((self.x == other.x) and (self.y == other.y + 1)) \
               or ((self.x == other.x) and (self.y == other.y - 1))
