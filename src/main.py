'''
Testing user interface
'''
from kiva_robot.kiva import Kiva
from kiva_robot.kiva_controller import FacingDirection
from kiva_robot.kiva_controller import KivaController
from kiva_robot.kiva_command import Commands
from kiva_robot.terrain import TerrainMap

if __name__ == '__main__':
    print()
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃                                                   ┃")
    print("┃ TEST: KIVA ROBOT                                  ┃")
    print("┃                                                   ┃")
    print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
    print("┃       ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓        ┃")
    print("┃       ┃           WAREHOUSE MAP          ┃        ┃")
    print("┃       ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫        ┃")
    print("┃       ┃                                  ┃        ┃")
    print("┃       ┃       |------------------|       ┃        ┃")
    print("┃       ┃       |                  |       ┃        ┃")
    print("┃       ┃       |  P*  *   **   D|-|       ┃        ┃")
    print("┃       ┃       |  *   **  P*    | |       ┃        ┃")
    print("┃       ┃       |  **   *  **    |-|       ┃        ┃")
    print("┃       ┃       |                  |       ┃        ┃")
    print("┃       ┃       |  **  **  **   D|-|       ┃        ┃")
    print("┃       ┃       |  **  K   P     | |       ┃        ┃")
    print("┃       ┃       |   *  **  **    |-|       ┃        ┃")
    print("┃       ┃       |                  |       ┃        ┃")
    print("┃       ┃       |  *P  P*  **   D|-|       ┃        ┃")
    print("┃       ┃       |  **  **  P*    | |       ┃        ┃")
    print("┃       ┃       |  P*  *   **    |-|       ┃        ┃")
    print("┃       ┃       |                  |       ┃        ┃")
    print("┃       ┃       |------------------|       ┃        ┃")
    print("┃       ┃                                  ┃        ┃")
    print("┃       ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛        ┃")
    print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
    print("┃ Enter the Kiva Commands:                          ┃")
    print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
    print("┃ R F F F F T F F L F R F F L F F F F R F D         ┃")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    print()
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃ Init Kiva Robot                                   ┃")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    initial_position = (7, 7)
    initial_direction_facing = FacingDirection.UP
    kiva = Kiva("K01W01", initial_position, initial_direction_facing)

    # Kiva State
    kiva.get_info()

    # Init KivaController
    terrain = TerrainMap()
    kiva_controller = KivaController(kiva, terrain)

    # Taking Pod
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃ Taking POD                                        ┃")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    kiva_controller.update(Commands.TURN_RIGHT)
    kiva_controller.update(Commands.FORWARD)
    kiva_controller.update(Commands.FORWARD)
    kiva_controller.update(Commands.FORWARD)
    kiva_controller.update(Commands.FORWARD)
    kiva_controller.update(Commands.TAKE)

    # Kiva State
    kiva.get_info()

    # Dropping Pod
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃ Dropping POD                                      ┃")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    kiva_controller.update(Commands.FORWARD)
    kiva_controller.update(Commands.FORWARD)
    kiva_controller.update(Commands.TURN_LEFT)
    kiva_controller.update(Commands.FORWARD)
    kiva_controller.update(Commands.TURN_RIGHT)
    kiva_controller.update(Commands.FORWARD)
    kiva_controller.update(Commands.FORWARD)
    kiva_controller.update(Commands.TURN_LEFT)
    kiva_controller.update(Commands.FORWARD)
    kiva_controller.update(Commands.FORWARD)
    kiva_controller.update(Commands.FORWARD)
    kiva_controller.update(Commands.FORWARD)
    kiva_controller.update(Commands.TURN_RIGHT)
    kiva_controller.update(Commands.FORWARD)
    kiva_controller.update(Commands.DROP)
    
    # Kiva State
    kiva.get_info()
    # Init Kiva
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃ End                                               ┃")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    print()
