import math

from models import Figure


class Circle(Figure):

    def __init__(self, rad):
        if rad <= 0:
            raise AttributeError('Radius must be greater than zero')
        self.rad = rad
        super().__init__('circle', 0)

    @property
    def area(self):
        return math.pi * self.rad ** 2

    @property
    def perimeter(self):
        return math.pi * self.rad * 2
