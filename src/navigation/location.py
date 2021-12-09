import numpy as np
from typing import List


class Location:

    def __init__(self, x: int, y: int):
        self.__x: int = x
        self.__y: int = y

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int) -> None:
        self.__x = x

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int) -> None:
        self.__y = y

    def coordinate(self) -> List[int]:
        return [self.__x, self.__y]

    def update(self, location_array: np.ndarray) -> None:
        self.__x = location_array[0]
        self.__y = location_array[1]

