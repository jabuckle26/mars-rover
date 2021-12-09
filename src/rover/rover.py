from numpy import add

from .collision_detector import CollisionDetector
from .movement_scalars import MovementScalars
from .navigation_commands import NavigationCommands
from .orientations import Orientations
from .rotation_scalars import RotationScalars
from ..navigation.location import Location


class Rover:

    def __init__(self, grid_size: int, location: Location, orientation: str) -> None:
        self.__grid_size: int = grid_size
        self.__location: Location = location
        self.__orientation: str = orientation
        self.__collision_detector: CollisionDetector = CollisionDetector(grid_size)
        pass

    @property
    def location(self) -> Location:
        return self.__location

    @location.setter
    def location(self, location: Location):
        self.__location = location

    @property
    def orientation(self) -> str:
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation: str):
        self.__orientation = orientation

    def rotate(self, rotation_direction: str):
        rotation: int = RotationScalars[rotation_direction].value
        new_direction_pointer: int = rotation + \
            Orientations[self.__orientation].value
        self.__orientation = Orientations(
            new_direction_pointer % len(Orientations)).name

    def move(self):
        if not self.__collision_detector.will_collide_with_border(self.__location, self.__orientation):
            self.__location.update(add(
                self.__location.coordinate(), MovementScalars[self.__orientation].value))

    def navigate(self, navigation_command: str):
        if navigation_command == NavigationCommands.MOVEMENT.value:
            self.move()
        elif navigation_command in NavigationCommands.ROTATION.value:
            self.rotate(navigation_command)
        else:
            print(f'Invalid Command: {navigation_command}')
