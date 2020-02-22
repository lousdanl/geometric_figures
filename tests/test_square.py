import pytest

from models import Square


@pytest.mark.parametrize('side', (-5, -1, 0))
def test_invalid_rectangle(side):
    with pytest.raises(AttributeError):
        Square(side)


def test_get_name(get_square):
    assert get_square.get_name() == 'square'


def test_get_angles(get_square):
    assert get_square.get_angles() == 4


def test_get_area(get_square):
    assert get_square.area == get_square.side_a * get_square.side_a


def test_get_perimeter(get_square):
    assert get_square.perimeter == get_square.side_b * 4
