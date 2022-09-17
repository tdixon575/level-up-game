
class Map:

    def __init__(self):
        self.min_x: int = 1
        self.max_x: int = 10
        self.min_y: int = 1
        self.max_y: int = 10

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

        if direction == 'Direction.NORTH':
            if y_coord < self.max_y:
                y_coord += 1
        elif direction == 'Direction.SOUTH':
            if y_coord > self.min_y:
                y_coord -= 1
        elif direction == 'Direction.EAST':
            if x_coord < self.max_x:
                x_coord += 1
        elif direction == 'Direction.WEST':
            if x_coord > self.min_x:
                x_coord -= 1

        '''
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
        '''

        return((x_coord, y_coord))