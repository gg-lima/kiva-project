'''
This module defines the Kiva Robot Controller.
'''
import math
from kiva_robot.kiva import Kiva
from kiva_robot.facing_direction import FacingDirection
from kiva_robot.kiva_command import Commands
from kiva_robot.terrain import TerrainMap

class KivaController():
    ''' This interface implements Kiva Robot's controller.
    '''
    def __init__(self, kiva: 'Kiva', terrain: 'TerrainMap') -> None:
        self.__kiva = kiva
        self.__terrain = terrain

    # Getters

    @property
    def kiva(self) -> 'Kiva':
        return self.__kiva

    @property
    def terrain(self) -> 'TerrainMap':
        return self.__terrain

    # Methods

    def update(self, input: 'Commands') -> None:
        ''' Execute Kiva Robot's command.
        '''
        # Using Strategy Pattern
        input.command.execute(self)
