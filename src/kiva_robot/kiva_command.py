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
from kiva_robot.terrain import TerrainObject

# Using Strategy Pattern
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
        # [TODO] test constraint: not moving out of grid limits;
        # [TODO] test constraint: not moving into obstacles;
        # [TODO] test constraint: risk collision: not moving into next Pod location when carrying Pod;

        # Rule Dispatcher
        dispatcher = RuleDispatcher([
            map_bound_rule(x, y, controller),
            obstacle_rule(x, y, controller),
            collision_rule(x, y, controller),
        ])
        dispatcher.handle_rule()

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
            raise SystemExit("Kiva Robots can only turn orthogonally!")

class TakeStrategy(KivaCommandStrategy):
    ''' Concrete Strategy. Implements Take command.
    '''
    def execute(self, controller: 'KivaController') -> None:
        ''' Implements take pod.
        '''
        # print("Doing: Take...")
        
        # [TODO] test constraint: not take when out of take zone;
        # [TODO] test constraint: not take when carrying Pod;

        # Rule Dispatcher
        dispatcher = RuleDispatcher([
            take_when_carrying_pod_rule(controller),
            take_zone_rule(controller),
        ])
        dispatcher.handle_rule()

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
        
        # [TODO] test constraint: not drop when out of drop zone;
        # [TODO] test constraint: not dorp when not carrying Pod.

        # Rule Dispatcher
        dispatcher = RuleDispatcher([
            drop_when_not_carryng_pod_rule(controller),
            drop_zone_rule(controller),
        ])
        dispatcher.handle_rule()

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

# Chain of Responsability for Moving Constraint
class RuleDispatcher():
    ''' [TODO] doc
    '''
    def __init__(self, rules: list) -> None:
        self.__rules = rules

    # Methods

    def handle_rule(self) -> None:
        for rule in self.__rules: rule

def map_bound_rule(next_x: int, next_y: int, controller: 'KivaController') -> None:
    ''' [TODO] doc
    '''
    if (
        next_x < 0 or next_x > controller.terrain.x_max or 
        next_y < 0 or next_y > controller.terrain.y_max
        ):
        raise SystemExit(f"Can't FORWARD: location ({next_x}, {next_y}) is out of map boundaries!")

def obstacle_rule(next_x: int, next_y: int, controller: 'KivaController')-> None:
    ''' [TODO] doc
    '''
    terrain_object = controller.terrain.get_object_at(next_x, next_y)
    if terrain_object == TerrainObject.OBSTACLE:
        raise SystemExit(f"Can't FORWARD: location ({next_x}, {next_y}) is an OBSTACLE!")

def collision_rule(next_x: int, next_y: int, controller: 'KivaController') -> None:
    ''' [TODO] doc
    '''
    terrain_object = controller.terrain.get_object_at(next_x, next_y)
    if (
        controller.kiva.carrying_pod and 
        terrain_object == TerrainObject.POD
        ):
        raise SystemExit(f"Can't FORWARD: location ({next_x}, {next_y}) is a POD and Kiva already carrying a POD, collision risk!")

def take_when_carrying_pod_rule(controller: 'KivaController') -> None:
    ''' [TODO] doc
    '''
    if controller.kiva.carrying_pod:
        raise SystemExit("Can't TAKE: already carrying a POD!")

def take_zone_rule(controller: 'KivaController') -> None:
    ''' [TODO] doc
    '''
    terrain_object = controller.terrain.get_object_at(controller.kiva.x, controller.kiva.y)
    if terrain_object != TerrainObject.POD:
        raise SystemExit(f"Can't TAKE: location {controller.kiva.position} is {terrain_object}, not a POD zone!")

def drop_when_not_carryng_pod_rule(controller: 'KivaController') -> None:
    ''' [TODO] doc
    '''
    if not controller.kiva.carrying_pod:
        raise SystemExit("Can't DROP: not carrying a POD!")

def drop_zone_rule(controller: 'KivaController') -> None:
    ''' [TODO] doc
    '''
    terrain_object = controller.terrain.get_object_at(controller.kiva.x, controller.kiva.y)
    if terrain_object != TerrainObject.DROP_ZONE:
        raise SystemExit(f"Can't DROP: location {controller.kiva.position} is {terrain_object}, not a DROP zone!")
