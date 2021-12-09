from numpy import add

from .movements import Movements
from .navigation_commands import Navigation_Commands
from .orientations import Orientations
from .rotations import Rotations


class Rover:

    def __init__(self, grid_size: int, location: list[int], orientation: str) -> None:
        self.__grid_size: int = grid_size
        self.__location: list[int] = location
        self.__orientation: str = orientation
        pass

    @property
    def grid_size(self):
        return self.__grid_size

    @grid_size.setter
    def grid_size(self, grid_size: int):
        self.__grid_size = grid_size

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: list[int]):
        self.__location = location

    @property
    def orientation(self):
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation: str):
        self.__orientation = orientation

    def rotate(self, rotation_direction: str):
        rotation: int = Rotations[rotation_direction].value
        new_direction_pointer: int = rotation + \
            Orientations[self.__orientation].value
        self.__orientation = Orientations(
            new_direction_pointer % len(Orientations)).name

    def isCurrentlyFacingGridBorder(self) -> bool:
        return self.isFacingEasternGridBorder() or self.isFacingNorthernGridBorder() or self.isFacingWesternGridBorder() or self.isFacingSouthernGridBorder()

    def isFacingNorthernGridBorder(self) -> bool:
        return self.__orientation == Orientations.N.name and self.__location[1] >= self.grid_size

    def isFacingSouthernGridBorder(self) -> bool:
        return self.__orientation == Orientations.S.name and self.__location[1] <= 0

    def isFacingEasternGridBorder(self) -> bool:
        return self.__orientation == Orientations.E.name and self.__location[0] >= self.grid_size

    def isFacingWesternGridBorder(self) -> bool:
        return self.__orientation == Orientations.W.name and self.__location[0] <= 0

    def move(self):
        if not self.isCurrentlyFacingGridBorder():
            self.__location = add(
                self.__location, Movements[self.__orientation].value)

    def navigate(self, navigation_command: str):
        if navigation_command == Navigation_Commands.MOVEMENT.value:
            self.move()
        elif navigation_command in Navigation_Commands.ROTATION.value:
            self.rotate(navigation_command)
        else:
            print(f'Invalid Command: {navigation_command}')
