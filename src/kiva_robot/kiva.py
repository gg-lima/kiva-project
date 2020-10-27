'''
This module defines the Kiva Robot.
'''
from kiva_robot.facing_direction import FacingDirection

class Kiva():
    ''' This interface allows to create Kiva Robot.

    Kiva Robot's position is represented by x and y coordinates and 
    its facing direction is represented by azimuthal angle (0˚ <= phi < 360˚),
    defined as a horizontal angle measured counterclockwise from its UP face.

    Kiva Robot is restricted to 4 directions based in movement grid coordinates:
        - UP (U), 0 degree;
        - LEFT (L), 90 degrees;
        - DOWN (D), 180 degrees;
        - RIGHT (R), 270 degrees.

    Initialize with the Kiva Robot:
        - Facing UP;
        - not carrying any Pod;
        - not having successfully dropped a Pod.

    The motor on each Kiva Robot is rated for 20,000 hours. After this point it
    needs to have its motor replaced or be retired.

    Arguments:
        id: The Kiva Robot's ID.
        position: The tuple of Kiva Robot's Position (x, y).
        facing_direction: The Kiva Robot's facing direction.
        carrying_pod: Boolean, whether the Kiva Robot is carrying any Pod.
        successfully_dropped: Boolean, whether the Kiva Robot has successfully dropped a Pod.
        motor_lifetime: the motor lifetime in milliseconds.
    '''
    def __init__(self,
                 kiva_id: str,
                 position: tuple,
                 facing_direction: 'FacingDirection' = FacingDirection.UP,
                 carrying_pod: bool = False,
                 successfully_dropped: bool = False,
                 motor_lifetime: int = 0) -> None:
        self.__id = kiva_id
        self.__position = position
        self.__facing_direction = facing_direction
        self.__carrying_pod = carrying_pod
        self.__successfully_dropped = successfully_dropped
        self.__motor_lifetime = motor_lifetime

    # Getters

    @property
    def id(self) -> str:
        return self.__id

    @property
    def position(self) -> tuple:
        return self.__position

    @property
    def facing_direction(self) -> 'FacingDirection':
        return self.__facing_direction

    @property
    def carrying_pod(self) -> bool:
        return self.__carrying_pod

    @property
    def successfully_dropped(self) -> bool:
        return self.__successfully_dropped

    @property
    def motor_lifetime(self) -> int:
        return self.__motor_lifetime

    @property
    def x(self):
        return self.__position[0]
    
    @property
    def y(self):
        return self.__position[1]

    # Setters

    @position.setter
    def position(self, position: tuple) -> tuple:
        self.__position = position

    @facing_direction.setter
    def facing_direction(self, facing_direction: 'FacingDirection') -> int:
        self.__facing_direction = facing_direction

    @carrying_pod.setter
    def carrying_pod(self, state: bool) -> bool:
        self.__carrying_pod = state

    @successfully_dropped.setter
    def successfully_dropped(self, state: bool) -> bool:
        self.__successfully_dropped = state

    @motor_lifetime.setter
    def motor_lifetime(self, ms: int) -> int:
        self.__motor_lifetime = ms

    # Methods

    def get_info(self) -> None:
        ''' [TODO] doc
        '''
        print( '  "kiva": {')
        print(f'     "id": {self.__id}')
        print(f'     "position": {self.__position}')
        print(f'     "facing_direction": {self.__facing_direction}')
        print(f'     "carrying_pod": {self.__carrying_pod}')
        print(f'     "successfully_dropped": {self.__successfully_dropped}')
        print(f'     "motor_lifetime": {self.__motor_lifetime:,}')
        print( '  }')
