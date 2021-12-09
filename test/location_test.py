from src.navigation.location import Location
import numpy as np


def test_can_create_location():
    x: int = 2
    y: int = 3
    location: Location = Location(x, y)

    assert location.x == x
    assert location.y == y

def test_can_get_coordinate_from_location():
    x: int = 2
    y: int = 3
    location: Location = Location(x, y)

    assert location.coordinate() == [2, 3]


def test_can_update_location_with_coordinate():
    x: int = 2
    y: int = 3
    location: Location = Location(x, y)

    new_coordinate: np.ndarray = np.array([0, 0])
    location.update(new_coordinate)

    assert location.x == 0
    assert location.y == 0
    assert location.coordinate() == [0, 0]