import pytest

from Coordinate import Coordinate
from Quadrant import Quadrant
from Menu import Menu


def test_should_get_quadrant_coordinate():
    # Arrange / Setup
    a = 10
    b = 20
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == "First"


def test_should_get_second_quadrant_coordinate():
    a = -10
    b = 20
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    result = quadrant.get_quadrant_coordinate()

    assert result == "Second"


def test_should_get_third_quadrant_coordinate():
    a = -10
    b = -20
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    result = quadrant.get_quadrant_coordinate()

    assert result == "Third"


def test_should_get_fourth_quadrant_coordinate():
    a = 10
    b = -20
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    result = quadrant.get_quadrant_coordinate()

    assert result == "Fourth"


def test_should_return_nothing_from_zero():
    a = 0
    b = 0
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    result = quadrant.get_quadrant_coordinate()

    assert result == ""


def test_should_return_false_from_coordinate_validation():
    a = 0
    b = 0
    coordinates = Coordinate(a, b)
    result = Menu.cordinate_is_valid(Menu, coordinates)

    assert result == False


def test_should_return_True_from_coordinate_validation():
    a = 10
    b = 20
    coordinates = Coordinate(a, b)
    result = Menu.cordinate_is_valid(Menu, coordinates)

    assert result == True

def test_should_return_a_TypeError():
    with pytest.raises(TypeError):
        a = "a"
        b = "b"
        coordinates = Coordinate(a, b)
        quadrant = Quadrant(coordinates)
        quadrant.get_quadrant_coordinate()