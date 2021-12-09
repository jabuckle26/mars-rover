from numpy import add

from .collision_detector import CollisionDetector
from .movement_scalars import MovementScalars
from .navigation_commands import NavigationCommands
from .orientations import Orientations
from .rotation_scalars import RotationScalars
from ..ex.invalid_command_exception import InvalidCommandException
from ..navigation.location import Location


class Rover:

    def __init__(self, grid_size: int, location: Location, orientation: str) -> None:
        self._grid_size: int = grid_size
        self._location: Location = location
        self._orientation: str = orientation
        self._collision_detector: CollisionDetector = CollisionDetector(grid_size)
        pass

    @property
    def location(self) -> Location:
        return self._location

    @location.setter
    def location(self, location: Location):
        self._location = location

    @property
    def orientation(self) -> str:
        return self._orientation

    @orientation.setter
    def orientation(self, orientation: str):
        self._orientation = orientation

    def rotate(self, rotation_direction: str):
        rotation: int = RotationScalars[rotation_direction].value
        new_direction_pointer: int = rotation + \
            Orientations[self._orientation].value
        self._orientation = Orientations(
            new_direction_pointer % len(Orientations)).name

    def move(self):
        if not self._collision_detector.will_collide_with_border(self._location, self._orientation):
            self._location.update(add(
                self._location.coordinate(), MovementScalars[self._orientation].value))

    def navigate(self, navigation_command: str):
        if navigation_command == NavigationCommands.MOVEMENT.value:
            self.move()
        elif navigation_command in NavigationCommands.ROTATION.value:
            self.rotate(navigation_command)
        else:
            print(f'Invalid Command: {navigation_command}')
            raise InvalidCommandException(f'Invalid Command: {navigation_command}')
