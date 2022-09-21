from dataclasses import dataclass

@dataclass
class Monster:
    name: str
    total_health: int
    attack_power: int
    location: tuple
    alive: bool = True
    #witch, goblin, dragon, troll, giant, werewolf

class Map:

    def __init__(self, size: int):
        self.size: int = size
        self.min_x: int = 1
        self.max_x: int = size
        self.min_y: int = 1
        self.max_y: int = size

    def validatePosition(self, current_position: tuple) -> bool:
        x_coord: int = int(current_position[0])
        y_coord: int = int(current_position[1])
        
        if (x_coord >= self.min_x and x_coord <= self.max_x):
            if (y_coord >= self.min_y and y_coord <= self.max_y):
                return True
            else:
                return False
        else:
            return False

    def calculatePosition(self, current_position: tuple, direction) -> tuple:
        x_coord: int = int(current_position[0])
        y_coord: int = int(current_position[1])

        dir = str(direction).split('.')[1]

        if dir == 'NORTH':
            if y_coord < self.max_y:
                y_coord += 1
        elif dir == 'SOUTH':
            if y_coord > self.min_y:
                y_coord -= 1
        elif dir == 'EAST':
            if x_coord < self.max_x:
                x_coord += 1
        elif dir == 'WEST':
            if x_coord > self.min_x:
                x_coord -= 1

        return((x_coord, y_coord))