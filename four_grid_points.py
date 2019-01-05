from dataclasses import dataclass

from grid_point import GridPoint
from two_grid_points import TwoGridPoints


@dataclass
class FourGridPoints:
    p1: GridPoint
    p2: GridPoint
    p3: GridPoint
    p4: GridPoint

    def contains(self, p: GridPoint) -> bool:
        return self.p1.has_same_coordinates_with(p) \
               or self.p2.has_same_coordinates_with(p) \
               or self.p3.has_same_coordinates_with(p) \
               or self.p4.has_same_coordinates_with(p)

    def count(self) -> int:
        return 4

    def is_connected(self) -> bool:
        s1 = TwoGridPoints(self.p1, self.p2)
        s2 = TwoGridPoints(self.p1, self.p3)
        s3 = TwoGridPoints(self.p1, self.p4)
        s4 = TwoGridPoints(self.p2, self.p3)
        s5 = TwoGridPoints(self.p2, self.p4)
        s6 = TwoGridPoints(self.p3, self.p4)

        return (s1.is_connected() and s2.is_connected() and s3.is_connected()) or \
               (s1.is_connected() and s2.is_connected() and s4.is_connected()) or \
               (s1.is_connected() and s2.is_connected() and s5.is_connected()) or \
               (s1.is_connected() and s2.is_connected() and s6.is_connected()) or \
               (s1.is_connected() and s3.is_connected() and s4.is_connected()) or \
               (s1.is_connected() and s3.is_connected() and s5.is_connected()) or \
               (s1.is_connected() and s3.is_connected() and s6.is_connected()) or \
               (s1.is_connected() and s4.is_connected() and s5.is_connected()) or \
               (s1.is_connected() and s4.is_connected() and s6.is_connected()) or \
               (s1.is_connected() and s5.is_connected() and s6.is_connected()) or \
 \
               (s2.is_connected() and s3.is_connected() and s4.is_connected()) or \
               (s2.is_connected() and s3.is_connected() and s5.is_connected()) or \
               (s2.is_connected() and s3.is_connected() and s6.is_connected()) or \
               (s2.is_connected() and s4.is_connected() and s5.is_connected()) or \
               (s2.is_connected() and s4.is_connected() and s6.is_connected()) or \
               (s2.is_connected() and s5.is_connected() and s6.is_connected()) or \
 \
               (s3.is_connected() and s4.is_connected() and s5.is_connected()) or \
               (s3.is_connected() and s4.is_connected() and s6.is_connected()) or \
               (s3.is_connected() and s5.is_connected() and s6.is_connected()) or \
 \
               (s4.is_connected() and s5.is_connected() and s6.is_connected())
