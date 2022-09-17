from enum import Enum
from dataclasses import dataclass
from levelup.character import Character
from levelup.map import Map

DEFAULT_CHARACTER_NAME = "Character"
ARBITRARY_INITIALIZED_POSITION = (1, 1)

class Direction(Enum):
    NORTH = "n"
    SOUTH = "s"
    EAST = "e"
    WEST = "w"


@dataclass
class GameStatus:
    running: bool = False
    current_position: tuple = ARBITRARY_INITIALIZED_POSITION
    map: Map = Map()
    character: Character = Character(DEFAULT_CHARACTER_NAME)
    num_moves: int = 0

    def set_character_position(self, xycoordinates: tuple) -> None:
        print(f"Set character position state for testing")
        self.current_position = xycoordinates

    def getPosition(self):
        return self.current_position

    
class GameController:
    status: GameStatus
    map: Map

    def __init__(self):
        self.status = GameStatus()
        self.map = Map()

    def create_character(self, character_name: str) -> None:
        if not character_name: 
            character_name = DEFAULT_CHARACTER_NAME
        self.status.character = Character(character_name)

    def move(self, direction) -> None:
        cur_pos = self.status.getPosition()
        new_pos = self.map.calculatePosition(cur_pos, direction)
        if self.map.validatePosition(new_pos):
            self.status.set_character_position(new_pos)
            self.status.num_moves += 1
            print(f'Congrats {self.status.character.name}, you moved {direction} and are now at {self.status.getPosition()}')
            print(f'You have moved {self.status.num_moves} squares')
        else:
            print(f'you cant move to {new_pos}')
    
    def getStatus():
        pass

    def startGame():
        pass
