from src.orientations import Orientations
from src.rotations import Rotations


class Rover():

    def __init__(self, location: list[int], orientation: str) -> None:
        self.location: list[int] = location
        self.orientation: str = orientation
        pass

    def rotate(self, rotation_direction: str):
        rotation: int = Rotations[rotation_direction].value
        new_direction_pointer: int = rotation + Orientations[self.orientation].value
        self.orientation = Orientations(new_direction_pointer % len(Orientations)).name
