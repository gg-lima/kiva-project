'''
This module defines the Terrain.
'''
from enum import Enum

class TerrainObject(Enum):
    ''' Collection of Terrain's objects.
    '''
    EMPTY = " "
    OBSTACLE = "|-*"
    POD = "P"
    DROP_ZONE = "D"

    def __init__(self, object: str) -> None:
        self.__object = object

    # Getters

    @property
    def object(self) -> str:
        return self.__object
    
    # Methods

    @classmethod
    def char_to_enum(cls, terrain_object: str) -> 'TerrainObject':
        ''' [TODO] doc
        '''
        char_to_enum_dict = {}
        for e in cls:
            for v in e.value:
                char_to_enum_dict[v] = e
        return char_to_enum_dict[terrain_object]

class TerrainMap():
    ''' Implements Terrain Map.
    '''
    def __init__(self):
        # [TODO] read map from a file
        
        # Default map
        self.__terrain_map = [
            ['|', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', 'P', '*', ' ', ' ', '*', ' ', ' ', ' ', '*', '*', ' ', ' ', ' ', 'D', '|', '-', '|'],
            ['|', ' ', ' ', '*', ' ', ' ', ' ', '*', '*', ' ', ' ', 'P', '*', ' ', ' ', ' ', ' ', '|', ' ', '|'],
            ['|', ' ', ' ', '*', '*', ' ', ' ', ' ', '*', ' ', ' ', '*', '*', ' ', ' ', ' ', ' ', '|', '-', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', '*', '*', ' ', ' ', '*', '*', ' ', ' ', '*', '*', ' ', ' ', ' ', 'D', '|', '-', '|'],
            ['|', ' ', ' ', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', 'P', ' ', ' ', ' ', ' ', ' ', '|', ' ', '|'],
            ['|', ' ', ' ', ' ', '*', ' ', ' ', '*', '*', ' ', ' ', '*', '*', ' ', ' ', ' ', ' ', '|', '-', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', '*', 'P', ' ', ' ', 'P', '*', ' ', ' ', '*', '*', ' ', ' ', ' ', 'D', '|', '-', '|'],
            ['|', ' ', ' ', '*', '*', ' ', ' ', '*', '*', ' ', ' ', 'P', '*', ' ', ' ', ' ', ' ', '|', ' ', '|'],
            ['|', ' ', ' ', 'P', '*', ' ', ' ', '*', ' ', ' ', ' ', '*', '*', ' ', ' ', ' ', ' ', '|', '-', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '|'],
        ]

        self.__x_max = len(self.__terrain_map[0]) - 1
        self.__y_max = len(self.__terrain_map) - 1

    # Getters

    @property
    def get_map(self) -> list:
        return self.__terrain_map
    
    @property
    def x_max(self) -> int:
        return self.__x_max

    @property
    def y_max(self) -> int:
        return self.__y_max

    # Methods

    def get_object_at(self, x: int, y: int) -> 'TerrainObject':
        ''' [TODO] doc
        '''
        return TerrainObject.char_to_enum(self.__terrain_map[y][x])
