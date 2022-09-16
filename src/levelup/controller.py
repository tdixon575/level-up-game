from enum import Enum
from dataclasses import dataclass
from levelup.character import Character
from levelup.map import Map

DEFAULT_CHARACTER_NAME = "Character"
ARBITRARY_INVALID_INITIALIZED_POSITION = (1,1)

class Direction(Enum):
    NORTH = "n"
    SOUTH = "s"
    EAST = "e"
    WEST = "w"


@dataclass
class GameStatus:
    running: bool = False
    character: Character = Character(DEFAULT_CHARACTER_NAME)
    current_position: tuple = ARBITRARY_INVALID_INITIALIZED_POSITION
    map: Map = Map()

    def set_character_position(self, xycoordinates: tuple) -> None:
        print(f"Set character position state for testing")
        self.current_position = xycoordinates

    def getPosition(self):
        return self.current_position

    
class GameController:
    status: GameStatus

    def __init__(self):
        self.status = GameStatus()

    def create_character(self, character_name: str) -> None:
        if not character_name: 
            character_name = DEFAULT_CHARACTER_NAME
        self.status.character = Character(character_name)

    def move(self, direction) -> None:
        cur_pos = self.status.getPosition()
        new_pos = self.status.map.calculatePosition(cur_pos, direction)
        if self.status.map.validatePosition(new_pos):
            self.status.set_character_position(new_pos)
            print(f'Congrats {self.status.character.name}, you moved {direction} and are now at {self.status.getPosition()}')
        else:
            print(f'you cant move to {new_pos}')
    
    def getStatus():
        pass

    def startGame():
        pass
