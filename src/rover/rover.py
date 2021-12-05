import numpy as np

from .orientations import Orientations
from .movements import Movements
from .rotations import Rotations


class Rover():

    def __init__(self, gridSize: int, location: list[int], orientation: str) -> None:
        self.gridSize: int = gridSize
        self.location: list[int] = location
        self.orientation: str = orientation
        pass

    def rotate(self, rotation_direction: str):
        rotation: int = Rotations[rotation_direction].value
        new_direction_pointer: int = rotation + \
            Orientations[self.orientation].value
        self.orientation = Orientations(
            new_direction_pointer % len(Orientations)).name

    def isCurrentlyFacingGridBorder(self) -> bool:
        return self.isFacingEasternGridBorder() or self.isFacingNorthernGridBorder() or self.isFacingWesternGridBorder() or self.isFacingSouthernGridBorder()

    def isFacingNorthernGridBorder(self) -> bool:
        return self.orientation == Orientations.NORTH.name and self.location[1] >= self.gridSize

    def isFacingSouthernGridBorder(self) -> bool:
        return self.orientation == Orientations.SOUTH.name and self.location[1] <= 1

    def isFacingEasternGridBorder(self) -> bool:
        return self.orientation == Orientations.EAST.name and self.location[0] >= self.gridSize

    def isFacingWesternGridBorder(self) -> bool:
        return self.orientation == Orientations.WEST.name and self.location[0] <= 1

    def move(self):
        if not self.isCurrentlyFacingGridBorder():
            self.location = np.add(
                self.location, Movements[self.orientation].value)
