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
    def __init__(self, kiva: 'Kiva') -> None:
        self.__kiva = kiva

    def update(self, input: 'Commands') -> None:
        # print(f"Updating kiva: {input.code}")
        input.command.execute(self.__kiva)
