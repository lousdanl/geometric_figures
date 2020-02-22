import pytest

from models import Circle


@pytest.mark.parametrize('radius', (-20, -1, 0))
def test_invalid_circle(radius):
    with pytest.raises(AttributeError):
        Circle(radius)


def test_get_name(get_circle):
    assert get_circle.get_name() == 'circle'


def test_get_angles(get_circle):
    assert get_circle.get_angles() == 0


def test_get_area(get_circle):
    assert round(get_circle.area, 3) == 153.938


def test_get_perimeter(get_circle):
    assert round(get_circle.perimeter, 3) == 43.982
