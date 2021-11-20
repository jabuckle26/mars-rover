from src.directions import Directions
from src.rover import Rover


def test_first_test():
    assert True


def test_can_create_rover():
    location: list[int] = [0, 0]
    orientation: str = 'WEST'
    rover = Rover(location, orientation)
    assert rover.location == location
    assert rover.orientation == Directions.WEST.name


def test_can_rotate_rover_ninty_degrees_right():
    location: list[int] = [0, 0]
    orientation: str = 'WEST'
    rover = Rover(location, orientation)
    assert rover.location == location
    assert rover.orientation == Directions.WEST.name
    rover.rotate('R')
    assert rover.location == location
    assert rover.orientation == Directions.NORTH.name


def test_can_roate_rover_ninty_degrees_left():
    location: list[int] = [0, 0]
    orientation: str = 'WEST'
    rover = Rover(location, orientation)
    assert rover.location == location
    assert rover.orientation == Directions.WEST.name
    rover.rotate('L')
    assert rover.location == location
    assert rover.orientation == Directions.SOUTH.name


def test_can_rotate_multiple_times():
    location: list[int] = [0, 0]
    orientation: str = 'WEST'
    rover = Rover(location, orientation)
    assert rover.location == location
    assert rover.orientation == Directions.WEST.name
    rover.rotate('L')
    assert rover.location == location
    assert rover.orientation == Directions.SOUTH.name
    rover.rotate('L')
    assert rover.location == location
    assert rover.orientation == Directions.EAST.name
    rover.rotate('L')
    assert rover.location == location
    assert rover.orientation == Directions.NORTH.name
    rover.rotate('R')
    assert rover.location == location
    assert rover.orientation == Directions.EAST.name
