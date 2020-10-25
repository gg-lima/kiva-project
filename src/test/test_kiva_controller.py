'''
'''
import unittest
import kiva_robot
from kiva_robot.kiva import Kiva
from kiva_robot.kiva_controller import FacingDirection
from kiva_robot.kiva_controller import KivaController
from kiva_robot.kiva_command import Commands

class TestKivaController(unittest.TestCase):
    '''
    '''
    kiva_id = "test_id"
    position = (1, 1)
    facing_direction = FacingDirection.UP
    carrying_pod = True
    successfully_dropped = True
    motor_lifetime = 5e3

    def test_move_forward_facing_up(self):
        '''
        '''
        # Init Kiva
        kiva = Kiva(
            self.kiva_id,
            self.position,
            FacingDirection.UP,
            self.carrying_pod,
            self.successfully_dropped,
            self.motor_lifetime
        )

        # Init KivaController
        terrain = "Terrain object"
        kiva_controller = KivaController(kiva, terrain)

        # Move
        kiva_controller.update(Commands.FORWARD)

        # Assertions
        self.assertEqual(kiva.id, self.kiva_id)
        self.assertEqual(kiva.position, (1, 0))
        self.assertEqual(kiva.facing_direction, FacingDirection.UP)
        self.assertEqual(kiva.carrying_pod, self.carrying_pod)
        self.assertEqual(kiva.successfully_dropped, self.successfully_dropped)
        self.assertEqual(kiva.motor_lifetime, self.motor_lifetime + int(1e3))

    def test_move_forward_facing_left(self):
        '''
        '''
        # Init Kiva
        kiva = Kiva(
            self.kiva_id,
            self.position,
            FacingDirection.LEFT,
            self.carrying_pod,
            self.successfully_dropped,
            self.motor_lifetime
        )

        # Init KivaController
        terrain = "Terrain object"
        kiva_controller = KivaController(kiva, terrain)

        # Move
        kiva_controller.update(Commands.FORWARD)

        # Assertions
        self.assertEqual(kiva.id, self.kiva_id)
        self.assertEqual(kiva.position, (0, 1))
        self.assertEqual(kiva.facing_direction, FacingDirection.LEFT)
        self.assertEqual(kiva.carrying_pod, self.carrying_pod)
        self.assertEqual(kiva.successfully_dropped, self.successfully_dropped)
        self.assertEqual(kiva.motor_lifetime, self.motor_lifetime + int(1e3))

    def test_move_forward_facing_down(self):
        '''
        '''
        # Init Kiva
        kiva = Kiva(
            self.kiva_id,
            self.position,
            FacingDirection.DOWN,
            self.carrying_pod,
            self.successfully_dropped,
            self.motor_lifetime
        )

        # Init KivaController
        terrain = "Terrain object"
        kiva_controller = KivaController(kiva, terrain)

        # Move
        kiva_controller.update(Commands.FORWARD)

        # Assertions
        self.assertEqual(kiva.id, self.kiva_id)
        self.assertEqual(kiva.position, (1, 2))
        self.assertEqual(kiva.facing_direction, FacingDirection.DOWN)
        self.assertEqual(kiva.carrying_pod, self.carrying_pod)
        self.assertEqual(kiva.successfully_dropped, self.successfully_dropped)
        self.assertEqual(kiva.motor_lifetime, self.motor_lifetime + int(1e3))

    def test_move_forward_facing_right(self):
        '''
        '''
        # Init Kiva
        kiva = Kiva(
            self.kiva_id,
            self.position,
            FacingDirection.RIGHT,
            self.carrying_pod,
            self.successfully_dropped,
            self.motor_lifetime
        )

        # Init KivaController
        terrain = "Terrain object"
        kiva_controller = KivaController(kiva, terrain)

        # Move
        kiva_controller.update(Commands.FORWARD)

        # Assertions
        self.assertEqual(kiva.id, self.kiva_id)
        self.assertEqual(kiva.position, (2, 1))
        self.assertEqual(kiva.facing_direction, FacingDirection.RIGHT)
        self.assertEqual(kiva.carrying_pod, self.carrying_pod)
        self.assertEqual(kiva.successfully_dropped, self.successfully_dropped)
        self.assertEqual(kiva.motor_lifetime, self.motor_lifetime + int(1e3))

    def test_turn_left_facing_up(self):
        '''
        '''
        # Init Kiva
        kiva = Kiva(
            self.kiva_id,
            self.position,
            FacingDirection.UP,
            self.carrying_pod,
            self.successfully_dropped,
            self.motor_lifetime
        )

        # Init KivaController
        terrain = "Terrain object"
        kiva_controller = KivaController(kiva, terrain)

        # Turn left
        kiva_controller.update(Commands.TURN_LEFT)

        # Assertions
        self.assertEqual(kiva.id, self.kiva_id)
        self.assertEqual(kiva.position, self.position)
        self.assertEqual(kiva.facing_direction, FacingDirection.LEFT)
        self.assertEqual(kiva.carrying_pod, self.carrying_pod)
        self.assertEqual(kiva.successfully_dropped, self.successfully_dropped)
        self.assertEqual(kiva.motor_lifetime, self.motor_lifetime + int(1e3))

    def test_turn_left_facing_left(self):
        '''
        '''
        # Init Kiva
        kiva = Kiva(
            self.kiva_id,
            self.position,
            FacingDirection.LEFT,
            self.carrying_pod,
            self.successfully_dropped,
            self.motor_lifetime
        )

        # Init KivaController
        terrain = "Terrain object"
        kiva_controller = KivaController(kiva, terrain)

        # Turn left
        kiva_controller.update(Commands.TURN_LEFT)

        # Assertions
        self.assertEqual(kiva.id, self.kiva_id)
        self.assertEqual(kiva.position, self.position)
        self.assertEqual(kiva.facing_direction, FacingDirection.DOWN)
        self.assertEqual(kiva.carrying_pod, self.carrying_pod)
        self.assertEqual(kiva.successfully_dropped, self.successfully_dropped)
        self.assertEqual(kiva.motor_lifetime, self.motor_lifetime + int(1e3))

    def test_turn_left_facing_down(self):
        '''
        '''
        # Init Kiva
        kiva = Kiva(
            self.kiva_id,
            self.position,
            FacingDirection.DOWN,
            self.carrying_pod,
            self.successfully_dropped,
            self.motor_lifetime
        )

        # Init KivaController
        terrain = "Terrain object"
        kiva_controller = KivaController(kiva, terrain)

        # Turn left
        kiva_controller.update(Commands.TURN_LEFT)

        # Assertions
        self.assertEqual(kiva.id, self.kiva_id)
        self.assertEqual(kiva.position, self.position)
        self.assertEqual(kiva.facing_direction, FacingDirection.RIGHT)
        self.assertEqual(kiva.carrying_pod, self.carrying_pod)
        self.assertEqual(kiva.successfully_dropped, self.successfully_dropped)
        self.assertEqual(kiva.motor_lifetime, self.motor_lifetime + int(1e3))

    def test_turn_left_facing_right(self):
        '''
        '''
        # Init Kiva
        kiva = Kiva(
            self.kiva_id,
            self.position,
            FacingDirection.RIGHT,
            self.carrying_pod,
            self.successfully_dropped,
            self.motor_lifetime
        )

        # Init KivaController
        terrain = "Terrain object"
        kiva_controller = KivaController(kiva, terrain)

        # Turn left
        kiva_controller.update(Commands.TURN_LEFT)

        # Assertions
        self.assertEqual(kiva.id, self.kiva_id)
        self.assertEqual(kiva.position, self.position)
        self.assertEqual(kiva.facing_direction, FacingDirection.UP)
        self.assertEqual(kiva.carrying_pod, self.carrying_pod)
        self.assertEqual(kiva.successfully_dropped, self.successfully_dropped)
        self.assertEqual(kiva.motor_lifetime, self.motor_lifetime + int(1e3))

    def test_turn_right_facing_up(self):
        '''
        '''
        # Init Kiva
        kiva = Kiva(
            self.kiva_id,
            self.position,
            FacingDirection.UP,
            self.carrying_pod,
            self.successfully_dropped,
            self.motor_lifetime
        )

        # Init KivaController
        terrain = "Terrain object"
        kiva_controller = KivaController(kiva, terrain)

        # Turn right
        kiva_controller.update(Commands.TURN_RIGHT)

        # Assertions
        self.assertEqual(kiva.id, self.kiva_id)
        self.assertEqual(kiva.position, self.position)
        self.assertEqual(kiva.facing_direction, FacingDirection.RIGHT)
        self.assertEqual(kiva.carrying_pod, self.carrying_pod)
        self.assertEqual(kiva.successfully_dropped, self.successfully_dropped)
        self.assertEqual(kiva.motor_lifetime, self.motor_lifetime + int(1e3))

    def test_turn_right_facing_left(self):
        '''
        '''
        # Init Kiva
        kiva = Kiva(
            self.kiva_id,
            self.position,
            FacingDirection.RIGHT,
            self.carrying_pod,
            self.successfully_dropped,
            self.motor_lifetime
        )

        # Init KivaController
        terrain = "Terrain object"
        kiva_controller = KivaController(kiva, terrain)

        # Turn right
        kiva_controller.update(Commands.TURN_RIGHT)

        # Assertions
        self.assertEqual(kiva.id, self.kiva_id)
        self.assertEqual(kiva.position, self.position)
        self.assertEqual(kiva.facing_direction, FacingDirection.DOWN)
        self.assertEqual(kiva.carrying_pod, self.carrying_pod)
        self.assertEqual(kiva.successfully_dropped, self.successfully_dropped)
        self.assertEqual(kiva.motor_lifetime, self.motor_lifetime + int(1e3))

    def test_turn_right_facing_down(self):
        '''
        '''
        # Init Kiva
        kiva = Kiva(
            self.kiva_id,
            self.position,
            FacingDirection.DOWN,
            self.carrying_pod,
            self.successfully_dropped,
            self.motor_lifetime
        )

        # Init KivaController
        terrain = "Terrain object"
        kiva_controller = KivaController(kiva, terrain)

        # Turn right
        kiva_controller.update(Commands.TURN_RIGHT)

        # Assertions
        self.assertEqual(kiva.id, self.kiva_id)
        self.assertEqual(kiva.position, self.position)
        self.assertEqual(kiva.facing_direction, FacingDirection.LEFT)
        self.assertEqual(kiva.carrying_pod, self.carrying_pod)
        self.assertEqual(kiva.successfully_dropped, self.successfully_dropped)
        self.assertEqual(kiva.motor_lifetime, self.motor_lifetime + int(1e3))

    def test_turn_right_facing_right(self):
        '''
        '''
        # Init Kiva
        kiva = Kiva(
            self.kiva_id,
            self.position,
            FacingDirection.LEFT,
            self.carrying_pod,
            self.successfully_dropped,
            self.motor_lifetime
        )

        # Init KivaController
        terrain = "Terrain object"
        kiva_controller = KivaController(kiva, terrain)

        # Turn right
        kiva_controller.update(Commands.TURN_RIGHT)

        # Assertions
        self.assertEqual(kiva.id, self.kiva_id)
        self.assertEqual(kiva.position, self.position)
        self.assertEqual(kiva.facing_direction, FacingDirection.UP)
        self.assertEqual(kiva.carrying_pod, self.carrying_pod)
        self.assertEqual(kiva.successfully_dropped, self.successfully_dropped)
        self.assertEqual(kiva.motor_lifetime, self.motor_lifetime + int(1e3))

if __name__ == '__main__':
    unittest.main()
