from abc import abstractmethod


class Figure:
    _name = None
    _angles = None
    _area = None
    _perimeter = None

    def __init__(self, name, angles):
        self._name = name
        self._angles = angles
        self._area = self.area
        self._perimeter = self.perimeter

    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
        pass

    def get_name(self):
        return self._name

    def get_angles(self):
        return self._angles

    def add_area(self, figure):
        if isinstance(figure, Figure):
            areas = figure.area + self.area
            return areas
        else:
            raise AttributeError('Wrong object')
