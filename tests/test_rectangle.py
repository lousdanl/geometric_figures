import pytest

from models import Rectangle

SIDES = (-5, 5), (-1, 6), (0, 0), (0, 7), (1, 0), (2, -1), (10, -10)


@pytest.mark.parametrize(('side_a', 'side_b'), SIDES)
def test_invalid_rectangle(side_a, side_b):
    with pytest.raises(AttributeError):
        Rectangle(side_a, side_b)


def test_get_name(get_rectangle):
    name = get_rectangle.get_name()
    assert name == 'rectangle'


def test_get_angles(get_rectangle):
    assert get_rectangle.get_angles() == 4


def test_get_area(get_rectangle):
    assert get_rectangle.area == get_rectangle.side_a * get_rectangle.side_b


def test_get_perimeter(get_rectangle):
    assert get_rectangle.perimeter == (get_rectangle.side_a + get_rectangle.side_b) * 2


def test_add_areas():
    figure1 = Rectangle(10, 12)
    figure2 = Rectangle(8, 5)
    assert figure1.add_area(figure2) == figure1.area + figure2.area
