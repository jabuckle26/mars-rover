import numpy as np

from src.rover.movements import Movements
from src.rover.orientations import Orientations
from src.rover.rover import Rover


gridSize: int = 5


def test_can_create_rover():
    location: list[int] = [0, 0]
    orientation: str = 'W'
    rover = Rover(gridSize, location, orientation)
    assert rover.location == location
    assert rover.orientation == Movements.W.name


def test_can_rotate_rover_ninty_degrees_right():
    location: list[int] = [0, 0]
    orientation: str = 'W'
    rover = Rover(gridSize, location, orientation)
    assert rover.location == location
    assert rover.orientation == Movements.W.name
    rover.rotate('R')
    assert rover.location == location
    assert rover.orientation == Movements.N.name


def test_can_roate_rover_ninty_degrees_left():
    location: list[int] = [0, 0]
    orientation: str = 'W'
    rover = Rover(gridSize, location, orientation)
    assert rover.location == location
    assert rover.orientation == Movements.W.name
    rover.rotate('L')
    assert rover.location == location
    assert rover.orientation == Movements.S.name


def test_can_rotate_multiple_times():
    location: list[int] = [0, 0]
    orientation: str = 'W'
    rover = Rover(gridSize, location, orientation)
    assert rover.location == location
    assert rover.orientation == Movements.W.name
    rover.rotate('L')
    assert rover.location == location
    assert rover.orientation == Movements.S.name
    rover.rotate('L')
    assert rover.location == location
    assert rover.orientation == Movements.E.name
    rover.rotate('L')
    assert rover.location == location
    assert rover.orientation == Movements.N.name
    rover.rotate('R')
    assert rover.location == location
    assert rover.orientation == Movements.E.name


def test_can_move_rover_by_one_space():
    location: list[int] = [1, 1]
    orientation: str = 'N'
    rover = Rover(gridSize, location, orientation)

    rover.move()
    assert np.array_equal(rover.location, [1, 2])


def test_can_move_rover_multiple_spaces():
    location: list[int] = [1, 1]
    orientation: str = 'E'
    rover = Rover(gridSize, location, orientation)

    rover.move()
    rover.move()
    rover.move()
    assert np.array_equal(rover.location, [4, 1])


def test_can_check_if_not_facing_border_while_at_border():
    location: list[int] = [1, 1]
    orientation: str = 'E'
    rover = Rover(gridSize, location, orientation)

    assert rover.isCurrentlyFacingGridBorder() == False


def test_top_border_identified():
    location: list[int] = [1, 5]
    orientation: str = 'N'
    rover = Rover(gridSize, location, orientation)

    assert rover.isCurrentlyFacingGridBorder()


def test_left_border_identified():
    location: list[int] = [0, 3]
    orientation: str = 'W'
    rover = Rover(gridSize, location, orientation)

    assert rover.isCurrentlyFacingGridBorder()


def test_bottom_border_identified():
    location: list[int] = [2, 0]
    orientation: str = 'S'
    rover = Rover(gridSize, location, orientation)

    assert rover.isCurrentlyFacingGridBorder()


def test_right_border_identified():
    location: list[int] = [5, 2]
    orientation: str = 'E'
    rover = Rover(gridSize, location, orientation)

    assert rover.isCurrentlyFacingGridBorder()


def test_rover_can_accept_rotate_command():
    location: list[int] = [1, 1]
    orientation: str = 'E'
    rover = Rover(gridSize, location, orientation)

    rover.navigate('L')
    assert rover.orientation == Orientations.N.name

    rover.navigate('R')
    assert rover.orientation == Orientations.E.name


def test_rover_does_nothing_with_invalid_command():
    location: list[int] = [1, 1]
    orientation: str = 'E'
    rover = Rover(gridSize, location, orientation)

    rover.navigate('invalid')
    assert rover.orientation == orientation
    assert rover.location == location


def test_rover_moves_with_move_command():
    location: list[int] = [1, 1]
    orientation: str = 'E'
    rover = Rover(gridSize, location, orientation)

    rover.navigate('M')
    assert np.array_equal(rover.location, [2, 1])
    assert rover.orientation == orientation


def test_first_sample_rover():
    location: list[int] = [1, 2]
    orientation: str = 'N'
    rover = Rover(gridSize, location, orientation)

    rover.rotate('L')
    rover.move()
    rover.rotate('L')
    rover.move()
    rover.rotate('L')
    rover.move()
    rover.rotate('L')
    rover.move()
    rover.move()

    assert np.array_equal(rover.location, [1, 3])
    assert rover.orientation == Orientations.N.name


def test_second_sample_rover():
    location: list[int] = [3, 3]
    orientation: str = 'E'
    rover = Rover(gridSize, location, orientation)

    rover.move()
    rover.move()
    rover.rotate('R')
    rover.move()
    rover.move()
    rover.rotate('R')
    rover.move()
    rover.rotate('R')
    rover.rotate('R')
    rover.move()

    assert np.array_equal(rover.location, [5, 1])
    assert rover.orientation == Orientations.E.name
