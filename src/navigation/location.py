import numpy as np
from typing import List


class Location:

    def __init__(self, x: int, y: int):
        self._x: int = x
        self._y: int = y

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, x: int) -> None:
        self._x = x

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, y: int) -> None:
        self._y = y

    def coordinate(self) -> List[int]:
        return [self._x, self._y]

    def update(self, location_array: np.ndarray) -> None:
        self._x = location_array[0]
        self._y = location_array[1]

