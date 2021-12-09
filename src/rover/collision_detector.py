from typing import List

from src.rover.orientations import Orientations


class CollisionDetector:

    def __init__(self, grid_size: int):
        self.__grid_size = grid_size

    def will_collide_with_border(self, current_location: List[int], orientation: str):
        def is_facing_northern_grid_border() -> bool:
            return orientation == Orientations.N.name and current_location[1] >= self.__grid_size

        def is_facing_southern_grid_border() -> bool:
            return orientation == Orientations.S.name and current_location[1] <= 0

        def is_facing_eastern_grid_border() -> bool:
            return orientation == Orientations.E.name and current_location[0] >= self.__grid_size

        def is_facing_western_grid_border() -> bool:
            return orientation == Orientations.W.name and current_location[0] <= 0

        return is_facing_northern_grid_border() or is_facing_southern_grid_border() or is_facing_eastern_grid_border() or is_facing_western_grid_border()


