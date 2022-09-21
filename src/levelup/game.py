import sys, time, random
from typing import Callable
from levelup.controller import GameController, Direction, Persona
from levelup.map import Map


class GameUI:

    game: GameController

    def __init__(self):
        self.game = GameController()

    def prompt(self, message: str, validation_fn: Callable[[str], bool]) -> str:
        while True:
            response = input(f"\n{message}\n> ")
            if validation_fn(response):
                break
        return response

    def slow_type(self, t: str, speed: int = 50):
        typing_speed = speed  # wpm
        for l in t:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(random.random() * 10.0 / typing_speed)
        print
        ''

    def start(self):
        character = self.prompt("Enter your name", lambda x: len(x) > 0)
        welcome = f'Welcome to the game of Eternal Glory, {character}!\n'
        self.slow_type(welcome)
        choose = f'Now you must choose a persona to play the game with...choose wisely\n'
        self.slow_type(choose)
        self.slow_type('Here are your options\n')
        # self.game.create_personas()
        self.game.display_personas_to_choose()
        valid_personas = [x.value for x in Persona]
        persona_choice = self.prompt(f"Enter your persona choice: {valid_personas}\n", lambda x: x in valid_personas,)
        # self.game.assign_persona_to_character(Persona(persona_choice))

        map_size = int(self.prompt("Choose the size of your world (5-50 km):", lambda x: 4 < int(x) < 51))

        self.game.total_num_monsters = map_size // 2
        self.slow_type(f'Generating map\n')
        self.slow_type('. . . . . . . . . .\n', 10)
        self.game.map: Map = Map(map_size)
        self.slow_type(f'Creating monsters\n')
        self.slow_type('. . . . . . . . . .\n', 10)
        self.game.create_monsters(map_size)
        self.slow_type(f'Generating your character\n')
        self.slow_type('. . . . . . . . . .\n', 10)
        self.game.create_character(character, Persona(persona_choice))
        self.game.status.set_character_position(self.game.gen_random_location(map_size))

        print(f'Your fantasy world has been created with {self.game.total_num_monsters} monsters.')
        print(f'Find and defeat them all to win the game!')
        print(f'Your starting map coordinates are: {self.game.status.getPosition()}')

        valid_directions = [x.value for x in Direction]
        valid_directions.append('i')
        while True:
            # print(f'Your current coordinates are: {self.game.status.getPosition()}')
            responce = self.prompt(
                f"What direction would you like to go? {valid_directions}\n(or ctrl+c to quit)",
                lambda x: x in valid_directions,
            )
            if responce == 'i':
                self.game.print_game_status()
            else:
                self.game.move(Direction(responce))
