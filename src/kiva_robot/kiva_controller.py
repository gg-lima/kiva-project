'''
This module defines the Kiva Robot Controller.
'''
import math
from kiva_robot.kiva import Kiva
from kiva_robot.facing_direction import FacingDirection
from kiva_robot.kiva_command import Commands

class KivaController():
    ''' This interface implements Kiva Robot's controller
    '''
    def __init__(self, kiva: 'Kiva', terrain: 'str') -> None:
        self.__kiva = kiva
        self.__terrain = terrain

    # Getters

    @property
    def kiva(self) -> 'Kiva':
        return self.__kiva

    @property
    def terrain(self) -> 'str':
        return self.__terrain

    # Methods

    def update(self, input: 'Commands') -> None:
        ''' Execute Kiva Robot's command.
        '''
        # print(f"Updating kiva: {input.code}")
        input.command.execute(self)
