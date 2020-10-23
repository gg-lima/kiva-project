'''
Testing user interface
'''
from kiva_robot.kiva import Kiva
from kiva_robot.kiva_controller import FacingDirection
from kiva_robot.kiva_controller import KivaController
from kiva_robot.kiva_command import Commands

if __name__ == '__main__':
    print()
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃                                                   ┃")
    print("┃ TEST: KIVA ROBOT                                  ┃")
    print("┃                                                   ┃")
    print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
    print("┃           ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━┓           ┃")
    print("┃           ┃       WAREHOUSE MAP       ┃           ┃")
    print("┃           ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━┫           ┃")
    print("┃           ┃ ┏━━━┳━━━┳━━━┳━━━┳━━━┳━━━┓ ┃           ┃")
    print("┃           ┃ ┃ K ┃   ┃   ┃   ┃   ┃   ┃ ┃           ┃")
    print("┃           ┃ ┣━━━╋━━━╋━━━╋━━━╋━━━╋━━━┫ ┃           ┃")
    print("┃           ┃ ┃   ┃   ┃ █ ┃ T ┃ █ ┃   ┃ ┃           ┃")
    print("┃           ┃ ┣━━━╋━━━╋━━━╋━━━╋━━━╋━━━┫ ┃           ┃")
    print("┃           ┃ ┃   ┃   ┃ █ ┃ █ ┃ █ ┃   ┃ ┃           ┃")
    print("┃           ┃ ┣━━━╋━━━╋━━━╋━━━╋━━━╋━━━┫ ┃           ┃")
    print("┃           ┃ ┃   ┃ D ┃   ┃   ┃   ┃   ┃ ┃           ┃")
    print("┃           ┃ ┗━━━┻━━━┻━━━┻━━━┻━━━┻━━━┛ ┃           ┃")
    print("┃           ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━┛           ┃")
    print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
    print("┃ Enter the Kiva Commands:                          ┃")
    print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
    print("┃ R F F F R F T L L F L F F L F F F D               ┃")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    print()
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃ Init Kiva Robot                                   ┃")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    initial_position = (0, 0)
    initial_direction_facing = FacingDirection.UP
    kiva = Kiva("kTEST", initial_position, initial_direction_facing)

    # Kiva State
    kiva.get_info()

    # Init KivaController
    kiva_controller = KivaController(kiva)

    # Taking Pod
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃ Taking POD                                        ┃")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    kiva_controller.update(Commands.TURN_RIGHT)
    kiva_controller.update(Commands.FORWARD)
    kiva_controller.update(Commands.FORWARD)
    kiva_controller.update(Commands.FORWARD)
    kiva_controller.update(Commands.TURN_RIGHT)
    kiva_controller.update(Commands.FORWARD)
    kiva_controller.update(Commands.TAKE)

    # Kiva State
    kiva.get_info()

    # Dropping Pod
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃ Dropping POD                                      ┃")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    kiva_controller.update(Commands.TURN_LEFT)
    kiva_controller.update(Commands.TURN_LEFT)
    kiva_controller.update(Commands.FORWARD)
    kiva_controller.update(Commands.TURN_LEFT)
    kiva_controller.update(Commands.FORWARD)
    kiva_controller.update(Commands.FORWARD)
    kiva_controller.update(Commands.TURN_LEFT)
    kiva_controller.update(Commands.FORWARD)
    kiva_controller.update(Commands.FORWARD)
    kiva_controller.update(Commands.FORWARD)
    kiva_controller.update(Commands.DROP)
    
    # Kiva State
    kiva.get_info()
    # Init Kiva
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃ End                                               ┃")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    print()
