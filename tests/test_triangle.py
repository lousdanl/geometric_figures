import pytest

from models import Triangle

PARAMS = [(-5, 1, 30), (0, 6, 40), (7, -2, 50), (8, 0, 90), (10, 1, 180), (11, 6, -360), (0, 0, 0)]


@pytest.mark.parametrize(('side_a', 'side_b', 'angle'), PARAMS)
def test_invalid_triangle(side_a, side_b, angle):
    with pytest.raises(AttributeError):
        Triangle(side_a, side_b, angle)


def test_get_name(get_triangle):
    assert get_triangle.get_name() == 'triangle'


def test_get_angles(get_triangle):
    assert get_triangle.get_angles() == 3


def test_get_side_c(get_triangle):
    assert round(get_triangle.side_c, 3) == 4.858


def test_get_area(get_triangle):
    assert round(get_triangle.area, 3) == 6.023


def test_get_perimeter(get_triangle):
    assert round(get_triangle.perimeter, 3) == 14.858
