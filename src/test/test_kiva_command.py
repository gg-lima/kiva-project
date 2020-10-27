'''
'''
from unittest import TestCase
from unittest.mock import Mock
from kiva_robot.kiva_command import TurnStrategy

class TestKivaCommand(TestCase):
    '''
    '''
    def test_turn_not_orthogonal(self):
        '''
        '''
        # Init KivaController
        controller = Mock()

        # Turn not orthogonal
        not_orthogonal_angle = 45

        # Init TurnStrategy
        turning = TurnStrategy(not_orthogonal_angle)

        # Assertions
        self.assertRaises(SystemExit,
                          turning.execute,
                          {"controller": controller})

if __name__ == '__main__':
    unittest.main()
