from levelup.controller import GameController, GameStatus

start_x: int
start_y: int

class MoveLibrary:

    #def initialize_character_xposition_with(self, x_position):
    def initialize_character_position_with(self, startingX, startingY):
        self.controller = GameController()
        xy_coord = (startingX, startingY)
        self.controller.status.set_character_position(xy_coord)

    def move_in_direction(self, direction):
        #self.controller = GameController()
        #self.controller.set_character_position((self.start_x, self.start_y))
        self.controller.move(direction)

    def character_position_should_be(self, expected):
        end_x = self.controller.status.current_position[0]
        if end_x != expected:
            raise AssertionError(
                    "%s != %s" % (end_x, expected)
                )

    def character_yposition_should_be(self, expected):
        end_y = self.controller.status.current_position[1]
        if end_y != expected: 
            raise AssertionError(
                    "%s != %s" % (end_y, expected)
                )



