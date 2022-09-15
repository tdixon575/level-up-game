from enum import Enum
from dataclasses import dataclass
from levelup.character import Character

DEFAULT_CHARACTER_NAME = "Character"


class Direction(Enum):
    NORTH = "n"
    SOUTH = "s"
    EAST = "e"
    WEST = "w"


@dataclass
class GameStatus:
    running: bool = False
    character: Character = Character(DEFAULT_CHARACTER_NAME)

    def set_character_position(self, xycoordinates: tuple) -> None:
        print(f"Set character position state for testing")
        # TODO: IMPLEMENT THIS

    def character_xposition_should_be(self, expected):
        end_x = self.controller.status.current_position[0]
        if end_x != expected:
            raise AssertionError(
                    "%s != %s" % (end_x, expected)
                )

    def character_yposition_should_be(self, expected):
        end_y = self.controller.status.current_position[0]
        if end_y != expected: 
            raise AssertionError(
                    "%s != %s" % (end_y, expected)
                )

class GameController:
    status: GameStatus

    def __init__(self):
        self.status = GameStatus()

    def create_character(self, character_name: str) -> None:
        if not character_name: 
            character_name = DEFAULT_CHARACTER_NAME
        self.status.character = Character(character_name)

    def move(self, direction: Direction) -> None:
        print(f"Moved {direction.name}")
    
    def getStatus():
        Pass

    def startGame():
        pass
