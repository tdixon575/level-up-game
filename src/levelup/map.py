# map class

class Map:

    def __init__(self):
        self.min_x = 1
        self.max_x = 10
        self.min_y = 1
        self.max_y = 10

    def validatePosition(self, current_position: tuple) -> bool:
        x_coord = current_position[0]
        y_coord = current_position[1]
        
        if (x_coord >= self.min_x and x_coord <= self.max_x):
            if (y_coord >= self.min_y and y_coord <= self.max_y):
                return True
            else:
                return False
        else:
            return False

    def calculatePosition(self, current_position: tuple, direction: str) -> tuple:
        x_coord = current_position[0]
        y_coord = current_position[1]

        if direction.lower() in ('north','n'):
            if y_coord < self.max_y:
                y_coord += 1
        elif direction.lower() in ('south','s'):
            if y_coord > self.min_y:
                y_coord -= 1
        elif direction.lower() in ('east','e'):
            if x_coord < self.max_x:
                x_coord += 1
        elif direction.lower() in ('west','w'):
            if x_coord > self.min_x:
                x_coord -= 1
                
        return((x_coord, y_coord))