from models.figure import Figure


class Rectangle(Figure):

    def __init__(self, side_a, side_b):
        if side_a <= 0 or side_b <= 0:
            raise AttributeError('Side must be greater than zero')
        self.side_a = side_a
        self.side_b = side_b
        super().__init__('square' if side_a == side_b else 'rectangle', 4)

    @property
    def area(self):
        return self.side_a * self.side_b

    @property
    def perimeter(self):
        return (self.side_a + self.side_b) * 2
