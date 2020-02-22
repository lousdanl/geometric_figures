import math

from models.figure import Figure


class Triangle(Figure):

    def __init__(self, side_a, side_b, angle):
        if side_a <= 0 or side_b <= 0 or angle % 180 == 0:
            raise AttributeError('Wrong param')
        self.side_a = side_a
        self.side_b = side_b
        self.angle = math.radians(angle)
        super().__init__('triangle', 3)

    @property
    def area(self):
        return self.side_a * self.side_b * math.sin(self.angle) / 2

    @property
    def side_c(self):
        side_c = math.sqrt(self.side_a ** 2 + self.side_b ** 2 -
                           2 * self.side_a * self.side_b * math.cos(self.angle))
        return side_c

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c
