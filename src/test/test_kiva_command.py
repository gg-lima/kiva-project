'''
'''
import unittest
from kiva_robot.facing_direction import FacingDirection
from kiva_robot.kiva import Kiva
from kiva_robot.kiva_command import TurnStrategy

class TestKivaCommand(unittest.TestCase):
    '''
    '''
    kiva_id = "test_id"
    position = (1, 1)
    facing_direction = FacingDirection.RIGHT
    carrying_pod = True
    successfully_dropped = True
    motor_lifetime = 5e3

    def test_turn_not_orthogonal(self):
        '''
        '''
        # Init Kiva
        kiva = Kiva(
            self.kiva_id,
            self.position,
            self.facing_direction,
            self.carrying_pod,
            self.successfully_dropped,
            self.motor_lifetime
        )

        # Turn not orthogonal
        not_orthogonal_angle = 45

        # Init TurnStrategy
        turning = TurnStrategy(not_orthogonal_angle)

        # Assertions
        self.assertRaises(Exception,
                          turning.execute,
                          {'kiva': kiva})

if __name__ == '__main__':
    unittest.main()
