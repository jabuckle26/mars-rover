from enum import Enum


class MovementVectors(Enum):
    N = [0, 1]
    S = [0, -1]
    E = [1, 0]
    W = [-1, 0]
