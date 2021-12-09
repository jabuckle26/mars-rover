from typing import List

from src.navigation.location import Location
from src.rover.orientations import Orientations


class CollisionDetector:

    def __init__(self, grid_size: int):
        self._grid_size = grid_size

    def will_collide_with_border(self, current_location: Location, orientation: str):
        def is_facing_northern_grid_border() -> bool:
            return orientation == Orientations.N.name and current_location.y >= self._grid_size

        def is_facing_southern_grid_border() -> bool:
            return orientation == Orientations.S.name and current_location.y <= 0

        def is_facing_eastern_grid_border() -> bool:
            return orientation == Orientations.E.name and current_location.x >= self._grid_size

        def is_facing_western_grid_border() -> bool:
            return orientation == Orientations.W.name and current_location.x <= 0

        return is_facing_northern_grid_border() or \
            is_facing_southern_grid_border() or \
            is_facing_eastern_grid_border() or \
            is_facing_western_grid_border()
