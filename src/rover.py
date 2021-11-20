import numpy as np

from src.orientations import Orientations
from src.movements import Movements
from src.rotations import Rotations


class Rover():

    def __init__(self, location: list[int], orientation: str, gridSize: int) -> None:
        self.location: list[int] = location
        self.orientation: str = orientation
        self.gridSize: int = gridSize
        pass

    def rotate(self, rotation_direction: str):
        rotation: int = Rotations[rotation_direction].value
        new_direction_pointer: int = rotation + \
            Orientations[self.orientation].value
        self.orientation = Orientations(
            new_direction_pointer % len(Orientations)).name

    def isCurrentlyFacingGridBorder(self) -> bool:
        if self.orientation == Orientations.NORTH.name and self.location[1] >= self.gridSize - 1:
            return True
        if self.orientation == Orientations.EAST.name and self.location[0] >= self.gridSize - 1:
            return True
        if self.orientation == Orientations.SOUTH.name and self.location[1] <= 0:
            return True
        if self.orientation == Orientations.WEST.name and self.location[0] <= 0:
            return True
        else:
            return False

    def move(self):
        if not self.isCurrentlyFacingGridBorder():
            self.location = np.add(
                self.location, Movements[self.orientation].value)
