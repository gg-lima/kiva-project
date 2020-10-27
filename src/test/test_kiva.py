'''
'''
from unittest import TestCase
from unittest.mock import Mock
from kiva_robot.kiva import Kiva

class TestKiva(TestCase):
    '''
    '''
    kiva_id = "test_id"
    position = (1, 1)
    facing_direction = Mock()
    carrying_pod = True
    successfully_dropped = True
    motor_lifetime = 5e3

    def test_kiva_creation(self):
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

        # Assertions
        self.assertEqual(kiva.id, self.kiva_id)
        self.assertEqual(kiva.position, self.position)
        self.assertEqual(kiva.facing_direction, self.facing_direction)
        self.assertEqual(kiva.carrying_pod, self.carrying_pod)
        self.assertEqual(kiva.successfully_dropped, self.successfully_dropped)
        self.assertEqual(kiva.motor_lifetime, self.motor_lifetime)

if __name__ == '__main__':
    unittest.main()
