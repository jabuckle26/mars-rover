import numpy as np
print(1)
from src.rover.movements import Movements
print(2)
from src.rover.orientations import Orientations
print(3)
from src.rover.rover import Rover


gridSize: int = 5


def test_first_test():
    assert True


def test_can_create_rover():
    location: list[int] = [0, 0]
    orientation: str = 'WEST'
    rover = Rover(gridSize, location, orientation)
    assert rover.location == location
    assert rover.orientation == Movements.WEST.name


def test_can_rotate_rover_ninty_degrees_right():
    location: list[int] = [0, 0]
    orientation: str = 'WEST'
    rover = Rover(gridSize, location, orientation)
    assert rover.location == location
    assert rover.orientation == Movements.WEST.name
    rover.rotate('R')
    assert rover.location == location
    assert rover.orientation == Movements.NORTH.name


def test_can_roate_rover_ninty_degrees_left():
    location: list[int] = [0, 0]
    orientation: str = 'WEST'
    rover = Rover(gridSize, location, orientation)
    assert rover.location == location
    assert rover.orientation == Movements.WEST.name
    rover.rotate('L')
    assert rover.location == location
    assert rover.orientation == Movements.SOUTH.name


def test_can_rotate_multiple_times():
    location: list[int] = [0, 0]
    orientation: str = 'WEST'
    rover = Rover(gridSize, location, orientation)
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
    location: list[int] = [1, 1]
    orientation: str = 'NORTH'
    rover = Rover(gridSize, location, orientation)

    rover.move()
    assert np.array_equal(rover.location, [1, 2])


def test_can_move_rover_multiple_spaces():
    location: list[int] = [1, 1]
    orientation: str = 'EAST'
    rover = Rover(gridSize, location, orientation)

    rover.move()
    rover.move()
    rover.move()
    assert np.array_equal(rover.location, [4, 1])


def test_can_check_if_not_facing_border_while_at_border():
    location: list[int] = [1, 1]
    orientation: str = 'EAST'
    rover = Rover(gridSize, location, orientation)

    assert rover.isCurrentlyFacingGridBorder() == False


def test_top_border_identified():
    location: list[int] = [1, 5]
    orientation: str = 'NORTH'
    rover = Rover(gridSize, location, orientation)

    assert rover.isCurrentlyFacingGridBorder()


def test_left_border_identified():
    location: list[int] = [1, 3]
    orientation: str = 'WEST'
    rover = Rover(gridSize, location, orientation)

    assert rover.isCurrentlyFacingGridBorder()


def test_bottom_border_identified():
    location: list[int] = [2, 1]
    orientation: str = 'SOUTH'
    rover = Rover(gridSize, location, orientation)

    assert rover.isCurrentlyFacingGridBorder()


def test_right_border_identified():
    location: list[int] = [5, 2]
    orientation: str = 'EAST'
    rover = Rover(gridSize, location, orientation)

    assert rover.isCurrentlyFacingGridBorder()


def test_first_sample_rover():
#     1 2 N

# LMLMLMLMM

    location: list[int] = [1, 2]
    orientation: str = 'NORTH'
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

    assert np.array_equal(rover.location, [2, 3])
    assert rover.orientation == Orientations.NORTH.name


def test_second_sample_rover():

# 3 3 E
# MM
# R
# MM
# R
# M
# RR
# M

    location: list[int] = [3, 3]
    orientation: str = 'EAST'
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
    assert rover.orientation == Orientations.EAST.name


#Issues remain with indexes of grid
#0 based index in the above code but 1 based index in the question