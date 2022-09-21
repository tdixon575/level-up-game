from enum import Enum
from dataclasses import dataclass
from levelup.character import Character
from levelup.map import Map
from levelup.map import Monster
import sys, time, random


DEFAULT_CHARACTER_NAME = "Character"
DEFAULT_PERSONA = "PAWN"
DEFAULT_INITIALIZED_POSITION = (1, 1)

class Direction(Enum):
    NORTH = "n"
    SOUTH = "s"
    EAST = "e"
    WEST = "w"

class Persona(Enum):
    Warrior = "w"
    Knight = "k"
    Fairie = "f"
    Princess = "p"
    Elf = "e"
    Dwarf = "d"
    Mage = "m"
    # fairie, knight, princess, elf, dwarf, mage, wizard, warrior

@dataclass
class GameStatus:
    running: bool = False
    current_position: tuple = DEFAULT_INITIALIZED_POSITION
    character: Character = Character(DEFAULT_CHARACTER_NAME, DEFAULT_PERSONA)
    num_moves: int = 0

    def set_character_position(self, xycoordinates: tuple) -> None:
        self.current_position = xycoordinates

    def getPosition(self):
        return self.current_position

    
class GameController:
    status: GameStatus
    map: Map
    total_num_monsters: int
    monster_list: list
    used_locations_list: list

    def __init__(self):
        self.status = GameStatus()
        self.monster_list = []
        self.used_locations_list = []

    def create_character(self, character_name: str, persona: Persona) -> None:
        x = str(persona).split('.')[1]
        if not character_name:
            character_name = DEFAULT_CHARACTER_NAME
        self.status.character = Character(character_name, x)

    def display_personas_to_choose(self):
        personas_list = [p.name for p in Persona]
        # for p in Persona:
        #     print(f'{p.name}')
        #     personas_list.append(p.name)
        print(f'personas_list is: {personas_list}')
        # keys: name, total_health, attack_power

    def create_personas(self):
        #need to finish this
        personas_list = []
        for p in Persona:
            print(f'{p.name}')
            personas_list.append(p.name)
        print(f'personas_list is: {personas_list}')
        # keys: name, total_health, attack_power

    def assign_persona_to_character(self):
        pass
        #parse Persona enum passed in
        #set character.i

    def create_monsters(self, map_size):
        # divide map size by 2 to get number of monsters needed
        num_monsters = map_size // 2
        num_easy_monsters = num_monsters // 2
        num_hard_monsters = num_monsters // 2
        num_medium_monsters = num_monsters - num_easy_monsters - num_hard_monsters

        print(num_easy_monsters, num_medium_monsters, num_hard_monsters)

        for i in range(1, num_easy_monsters+1):
            # get random int for type of monster
            x = random.randint(1, 3)
            if x == 1:
                m = Monster('troll', 2, 1, self.gen_random_location(map_size))
                self.monster_list.append(m)
            if x == 2:
                m = Monster('snake', 2, 2, self.gen_random_location(map_size))
                self.monster_list.append(m)
            if x == 3:
                m = Monster('goblin', 3, 1, self.gen_random_location(map_size))
                self.monster_list.append(m)

        for i in range(1, num_medium_monsters+1):
            # get random int for type of monster
            x = random.randint(1, 2)
            if x == 1:
                m = Monster('Witch', 5, 4, self.gen_random_location(map_size))
                self.monster_list.append(m)
            if x == 2:
                m = Monster('Vampire', 4, 3, self.gen_random_location(map_size))
                self.monster_list.append(m)

        for i in range(1, num_hard_monsters+1):
            # get random int for type of monster
            x = random.randint(1, 3)
            if x == 1:
                # m = Monster('Dragon', 10, 5, self.gen_random_location(map_size))
                m = Monster('Dragon', 1, 2, self.gen_random_location(map_size))
                self.monster_list.append(m)
            if x == 2:
                # m = Monster('Giant', 8, 4, self.gen_random_location(map_size))
                m = Monster('Giant', 1, 2, self.gen_random_location(map_size))
                self.monster_list.append(m)
            if x == 3:
                # m = Monster('Werewolf', 7, 3, self.gen_random_location(map_size))
                m = Monster('Werewolf', 1, 2, self.gen_random_location(map_size))
                self.monster_list.append(m)

        #add monster locations to used_locations_list
        for monster in self.monster_list:
            self.used_locations_list.append(monster.location)

    def move(self, direction) -> None:
        dir = str(direction).split('.')[1]
        cur_pos = self.status.getPosition()
        new_pos = self.map.calculatePosition(cur_pos, direction)
        if self.map.validatePosition(new_pos):
            self.status.set_character_position(new_pos)
            self.status.num_moves += 1
            for monster in self.monster_list:
                if monster.location == self.status.getPosition():
                    print(f'Oh dear, you encountered a {monster.name} with {monster.total_health} health and {monster.attack_power} power!')
                    print(f'You must fight to the death! Fight beginning...')
                    self.slow_type('..........', 10)
                    self.battle_monster(monster, self.status.character)
            print(f'Congrats {self.status.character.name} the {self.status.character.persona}, you travelled 1 KM {dir} and are now at {self.status.getPosition()}')
            print(f'You have traveled a total of {self.status.num_moves} kilometers')
        else:
            print(f'you cant move to {new_pos}')


    def gen_random_location(self, max_int: int) -> tuple:
        x = random.randint(1, max_int)
        y = random.randint(1, max_int)
        return (x, y)

    def battle_monster(self, monster_obj: Monster, character_obj: Character) -> bool:
        print(f'You are fighting a {monster_obj.name}! Good Luck!')
        battling = True
        while battling:
            # character attacks first
            monster_obj.total_health -= character_obj.attack_power
            # monster attacks second
            character_obj.total_health -= monster_obj.attack_power
            if character_obj.total_health <= 0:
                character_obj.alive = False
            if monster_obj.total_health <= 0:
                monster_obj.alive = False

            if not character_obj.alive and not monster_obj.alive:
                print(f'You killed the {monster.name}! But he also killed you....game over!')
                print(f'You died at {self.status.getPosition()} after traveling {self.status.num_moves} kilometers')
                sys.exit(0)
            if not monster_obj.alive:
                print(f'You killed the {monster_obj.name} with a mighty stroke!')
                #check how many monsters remain alive
                if not self.monsters_still_alive():
                    print(f'Congratulations YOU WON THE GAME!!!')
                    sys.exit(0)
                return True
            if not character_obj.alive:
                print(f'The {monster_obj.name} defeated you easily! game over!')
                print(f'You died at {self.status.getPosition()} after traveling {self.status.num_moves} kilometers')
                sys.exit(0)

    def monsters_still_alive(self) -> bool:
        num_dead_monsters = 0
        num_living_monsters = 0
        for monster in self.monster_list:
            if monster.alive:
                num_living_monsters += 1
            else:
                num_dead_monsters += 1

        return True if num_living_monsters > 0 else False

    def print_game_status(self):
        num_dead_monsters = 0
        num_living_monsters = 0
        for monster in self.monster_list:
            if monster.alive:
                num_living_monsters += 1
            else:
                num_dead_monsters += 1

        print(f'Name: {self.status.character.name}')
        print(f'Persona: {self.status.character.persona}')
        print(f'Health: {self.status.character.total_health}')
        print(f'Attack: {self.status.character.attack_power}')
        print(f'You have traveled {self.status.num_moves} kilometers')
        print(f'Your current coordinates are: {self.status.getPosition()}')
        print(f'Total monsters: {len(self.monster_list)}')
        print(f'Monster list: {self.monster_list}')
        print(f'You have killed {num_dead_monsters} monsters so far')
        print(f'There are {num_living_monsters} monsters remaining')


    def slow_type(self, t: str, speed: int = 50):
        typing_speed = speed  # wpm
        for l in t:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(random.random() * 10.0 / typing_speed)
        print
        ''

    def start_game():
        pass
