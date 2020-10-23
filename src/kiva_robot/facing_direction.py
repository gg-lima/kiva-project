'''
This module defines the Kiva Robot facing direction.
'''
from enum import Enum

class FacingDirection(Enum):
    ''' Collection of Kiva Robot's facing direction.

    The facing direction is represented by azimuthal angle (0˚ <= phi < 360˚),
    defined as a horizontal angle measured counterclockwise from UP face.

    Kiva Robot is restricted to 4 directions based in movement grid coordinates:
        - UP (U), 0 degree;
        - LEFT (L), 90 degrees;
        - DOWN (D), 180 degrees;
        - RIGHT (R), 270 degrees.
    '''
    UP = 0
    LEFT = 90
    DOWN = 180
    RIGHT = 270

    def __init__(self, phi: int) -> None:
        self.__phi = phi

    # Getters

    @property
    def phi(self) -> None:
        return self.__phi
