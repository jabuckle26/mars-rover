import numpy as np

from src.movements import Movements
from src.rover import Rover


gridSize: int = 5


def test_first_test():
    assert True


def test_can_create_rover():
    location: list[int] = [0, 0]
    orientation: str = 'WEST'
    rover = Rover(location, orientation, gridSize)
    assert rover.location == location
    assert rover.orientation == Movements.WEST.name


def test_can_rotate_rover_ninty_degrees_right():
    location: list[int] = [0, 0]
    orientation: str = 'WEST'
    rover = Rover(location, orientation, gridSize)
    assert rover.location == location
    assert rover.orientation == Movements.WEST.name
    rover.rotate('R')
    assert rover.location == location
    assert rover.orientation == Movements.NORTH.name


def test_can_roate_rover_ninty_degrees_left():
    location: list[int] = [0, 0]
    orientation: str = 'WEST'
    rover = Rover(location, orientation, gridSize)
    assert rover.location == location
    assert rover.orientation == Movements.WEST.name
    rover.rotate('L')
    assert rover.location == location
    assert rover.orientation == Movements.SOUTH.name


def test_can_rotate_multiple_times():
    location: list[int] = [0, 0]
    orientation: str = 'WEST'
    rover = Rover(location, orientation, gridSize)
    assert rover.location == location
    assert rover.orientation == Movements.WEST.name
    rover.rotate('L')
    assert rover.location == location
    assert rover.orientation == Movements.SOUTH.name
    rover.rotate('L')
    assert rover.location == location
    assert rover.orientation == Movements.EAST.name
    rover.rotate('L')
    assert rover.location == location
    assert rover.orientation == Movements.NORTH.name
    rover.rotate('R')
    assert rover.location == location
    assert rover.orientation == Movements.EAST.name


def test_can_move_rover_by_one_space():
    location: list[int] = [0, 0]
    orientation: str = 'NORTH'
    rover = Rover(location, orientation, gridSize)

    rover.move()
    assert np.array_equal(rover.location, [0, 1])


def test_can_move_rover_multiple_spaces():
    location: list[int] = [0, 0]
    orientation: str = 'EAST'
    rover = Rover(location, orientation, gridSize)

    rover.move()
    rover.move()
    rover.move()
    assert np.array_equal(rover.location, [3, 0])


def test_can_check_if_not_facing_border_while_at_border():
    location: list[int] = [0, 0]
    orientation: str = 'EAST'
    rover = Rover(location, orientation, gridSize)

    assert rover.isCurrentlyFacingGridBorder() == False


def test_top_border_identified():
    location: list[int] = [0, 4]
    orientation: str = 'NORTH'
    rover = Rover(location, orientation, gridSize)

    assert rover.isCurrentlyFacingGridBorder()


def test_left_border_identified():
    location: list[int] = [0, 3]
    orientation: str = 'WEST'
    rover = Rover(location, orientation, gridSize)

    assert rover.isCurrentlyFacingGridBorder()


def test_bottom_border_identified():
    location: list[int] = [2, 0]
    orientation: str = 'SOUTH'
    rover = Rover(location, orientation, gridSize)

    assert rover.isCurrentlyFacingGridBorder()


def test_right_border_identified():
    location: list[int] = [4, 2]
    orientation: str = 'EAST'
    rover = Rover(location, orientation, gridSize)

    assert rover.isCurrentlyFacingGridBorder()
