'''
This module defines the Kiva Robot Commands.

Kiva Robot's movement inside grid coordinates:


      0   1   2   3   x
    ┌───┬───┬───┬───┐
  0 │   │ ⇧ │   │   │
    ├───┼───┼───┼───┤
  1 │ ⇦ │ K │ ⇨ │   │
    ├───┼───┼───┼───┤
  2 │   │ ⇩ │   │   │
    ├───┼───┼───┼───┤
  3 │   │   │   │   │
    └───┴───┴───┴───┘
  y 


Kiva Robot will be moved one step forward from 
its current position at its current facing direction.

Kiva Robot's moving constraints:
- not moving out of grid limits;
- not moving into obstacles;
- risk collision: not moving into next Pod location when carrying Pod;
- not take when out of take zone;
- not take when carrying Pod;
- not drop when out of drop zone;
- not dorp when not carrying Pod.
'''
from enum import Enum
from abc import ABCMeta, abstractmethod
from math import (
    radians,
    sin,
    cos
)
from kiva_robot.facing_direction import FacingDirection

class KivaCommandStrategy(metaclass=ABCMeta):
    ''' The interface for all Kiva's commands.
    '''
    @abstractmethod
    def execute(self, controller: 'KivaController') -> None:
        raise NotImplementedError

class ForwardStrategy(KivaCommandStrategy):
    ''' Concrete Strategy. Implements Forward command.
    '''
    def execute(self, controller: 'KivaController') -> None:
        ''' Implements move one step forward.
        '''
        # print("Doing: Forward...")
        
        # Using Spherical Coordinate System        
        # Radius: r = 1
        # zenith: polar angle 90 degrees

        # Cartesian Coordinates of Spherical Coordinate System
        # x = int(r * sin_teta * cos_phi)
        # y = int(r * sin_teta * sin_phi)
        # z = int(r * cos_teta)

        # Coordinates xy and azimuth
        x, y = controller.kiva.position
        phi = controller.kiva.facing_direction.phi

        # Sine/Cosine
        sin_phi = sin(radians(phi))
        cos_phi = cos(radians(phi))

        # Transforming (x, y) to fit in movement grid coordinates.
        # Applying rotation 90 degrees and inverting y

        # Rotation 90 degrees
        # x' = x * Cos(90) - y * Sin(90) = x * 0 - y * 1 = -y
        # y' = x * Sin(90) + y * Cos(90) = x * 1 + y * 0 = x

        # x = -int(r * sin_teta * sin_phi)
        # y = -int(r * sin_teta * cos_phi)

        # Next position
        x += -int(sin_phi)
        y += -int(cos_phi)

        # Check Position
        # [TODO] constraint: not moving out of grid limits;
        # [TODO] constraint: not moving into obstacles;
        # [TODO] constraint: risk collision: not moving into next Pod location when carrying Pod;

        # if next_position is out_bound: raise Exception
        # if next_position is obstacles: raise Exception
        # if next_position is pod_zone and carrying_pod is true: raise Exception

        # Updating position
        controller.kiva.position = (x, y)

        # Incrementing motor_lifetime
        controller.kiva.motor_lifetime += int(1e3)

class TurnStrategy(KivaCommandStrategy):
    ''' Concrete Strategy. Implements Turn command.
    '''
    def __init__(self, angle: int) -> None:
        self.__angle = angle

    def execute(self, controller: 'KivaController') -> None:
        ''' Implements turn orthognally.
        '''
        # print("Doing: Turning...")
        
        if (self.__angle % 90 == 0):
            # azimuthal angle
            phi = controller.kiva.facing_direction.phi

            # Moving facing_direction
            phi += self.__angle

            # Updating facing_direction
            # Keeping value between 0 and 360
            phi %= 360
            controller.kiva.facing_direction = FacingDirection(phi)

            # Incrementing motor_lifetime
            controller.kiva.motor_lifetime += int(1e3)
        else:
            raise Exception("Kiva Robots can only turn orthogonally!")

class TakeStrategy(KivaCommandStrategy):
    ''' Concrete Strategy. Implements Take command.
    '''
    def execute(self, controller: 'KivaController') -> None:
        ''' Implements take pod.
        '''
        # print("Doing: Take...")
        
        # [TODO] constraint: not take when out of take zone;
        # [TODO] constraint: not take when carrying Pod;

        # if take_when_carrying_pod: raise Exception
        # if not pod_zone: raise Exception

        # Take
        controller.kiva.carrying_pod = True
        controller.kiva.successfully_dropped = False

        # Incrementing motor_lifetime
        controller.kiva.motor_lifetime += int(1e3)

class DropStrategy(KivaCommandStrategy):
    ''' Concrete Strategy. Implements Drop command.
    '''
    def execute(self, controller: 'KivaController') -> None:
        ''' Implements drop pod.
        '''
        # print("Doing: Drop...")
        
        # [TODO] constraint: not drop when out of drop zone;
        # [TODO] constraint: not dorp when not carrying Pod.

        # if drop_when_not_carryng_pod: raise Exception
        # if not drop_zone: raise Exception

        # Drop
        controller.kiva.successfully_dropped = True
        controller.kiva.carrying_pod = False

        # Incrementing motor_lifetime
        controller.kiva.motor_lifetime += int(1e3)

class Commands(Enum):
    ''' Collection of Kiva Robot's commands.
    '''
    FORWARD = ('F', ForwardStrategy())
    TURN_LEFT = ('L', TurnStrategy(90))
    TURN_RIGHT = ('R', TurnStrategy(-90))
    TAKE = ('T', TakeStrategy())
    DROP = ('D', DropStrategy())

    def __init__(self, code: str, command: 'KivaCommandStrategy') -> None:
        self.__code = code
        self.__command = command

    # Getters
    
    @property
    def code(self) -> str:
        return self.__code

    @property
    def command(self) -> 'KivaCommandStrategy':
        return self.__command
