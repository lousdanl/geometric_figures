import pytest

from models import Rectangle, Square, Triangle, Circle


@pytest.fixture()
def get_rectangle():
    return Rectangle(4, 6)


@pytest.fixture()
def get_square():
    return Square(5)


@pytest.fixture()
def get_triangle():
    return Triangle(3, 7, 35)


@pytest.fixture()
def get_circle():
    return Circle(7)
