import numpy as np
import pytest

from src.ex.invalid_command_exception import InvalidCommandException
from src.navigation.location import Location
from src.rover.movement_scalars import MovementScalars
from src.rover.orientations import Orientations
from src.rover.rover import Rover

gridSize: int = 5


def test_can_create_rover():
    location: Location = Location(0, 0)
    orientation: str = 'W'
    rover = Rover(gridSize, location, orientation)
    assert rover.location == location
    assert rover.orientation == MovementScalars.W.name


def test_can_rotate_rover_ninty_degrees_right():
    location: Location = Location(0, 0)
    orientation: str = 'W'
    rover = Rover(gridSize, location, orientation)
    assert rover.location == location
    assert rover.orientation == MovementScalars.W.name
    rover.rotate('R')
    assert rover.location == location
    assert rover.orientation == MovementScalars.N.name


def test_can_rotate_rover_ninty_degrees_left():
    location: Location = Location(0, 0)
    orientation: str = 'W'
    rover = Rover(gridSize, location, orientation)
    assert rover.location == location
    assert rover.orientation == MovementScalars.W.name
    rover.rotate('L')
    assert rover.location == location
    assert rover.orientation == MovementScalars.S.name


def test_can_rotate_multiple_times():
    location: Location = Location(0, 0)
    orientation: str = 'W'
    rover = Rover(gridSize, location, orientation)
    assert rover.location == location
    assert rover.orientation == MovementScalars.W.name
    rover.rotate('L')
    assert rover.location == location
    assert rover.orientation == MovementScalars.S.name
    rover.rotate('L')
    assert rover.location == location
    assert rover.orientation == MovementScalars.E.name
    rover.rotate('L')
    assert rover.location == location
    assert rover.orientation == MovementScalars.N.name
    rover.rotate('R')
    assert rover.location == location
    assert rover.orientation == MovementScalars.E.name


def test_can_move_rover_by_one_space():
    location: Location = Location(1, 1)
    orientation: str = 'N'
    rover = Rover(gridSize, location, orientation)

    rover.move()
    assert np.array_equal(rover.location.coordinate(), [1, 2])


def test_can_move_rover_multiple_spaces():
    location: Location = Location(1, 1)
    orientation: str = 'E'
    rover = Rover(gridSize, location, orientation)

    rover.move()
    rover.move()
    rover.move()
    assert np.array_equal(rover.location.coordinate(), [4, 1])


def test_rover_can_accept_rotate_command():
    location: Location = Location(1, 1)
    orientation: str = 'E'
    rover = Rover(gridSize, location, orientation)

    rover.navigate('L')
    assert rover.orientation == Orientations.N.name

    rover.navigate('R')
    assert rover.orientation == Orientations.E.name


def test_rover_does_nothing_with_invalid_command():
    location: Location = Location(1, 1)
    orientation: str = 'E'
    rover = Rover(gridSize, location, orientation)
    bad_command: str = 'invalid'

    with pytest.raises(InvalidCommandException, match=f'Invalid Command: {bad_command}'):
        rover.navigate(bad_command)



def test_rover_moves_with_move_command():
    location: Location = Location(1, 1)
    orientation: str = 'E'
    rover = Rover(gridSize, location, orientation)

    rover.navigate('M')
    assert np.array_equal(rover.location.coordinate(), [2, 1])
    assert rover.orientation == orientation


def test_first_sample_rover():
    location: Location = Location(1, 2)
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

    assert np.array_equal(rover.location.coordinate(), [1, 3])
    assert rover.orientation == Orientations.N.name


def test_second_sample_rover():
    location: Location = Location(3, 3)
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

    assert np.array_equal(rover.location.coordinate(), [5, 1])
    assert rover.orientation == Orientations.E.name
