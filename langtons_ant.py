import arcade
import sim_settings as stg


DOT_SIZE = 4


class Ant:
    def __init__(self, _map, _speed, _x, _y, _index=0, _dir='U'):
        """Representation of Langton's Ant.
        :param _map: Representation of a board the ant moves on
        :param _speed: How many steps per second the ant does
        :param _x: X position of the ant on the screen
        :param _y: Y position of the ant on the screen
        :param _index: Color index of the ant for Map to decode - check Map.colors[] and Map.draw()
        :param _dir: Starting direction of the ant: 'D' down, 'L' left, 'R' right, anything else for up"""
        self.index = _index
        self.map = _map
        self.on_black_tile = False
        match _dir:
            case 'D':
                self.dir = [0, -1]
            case 'R':
                self.dir = [1, 0]
            case 'L':
                self.dir = [-1, 0]
            case _:
                self.dir = [0, 1]
        self.pos = [_x//DOT_SIZE, _y//DOT_SIZE]
        self.step_counter = 0  # TODO: display each ant's step counter
        self.speed = 1.0 / _speed
        self.counter = 0.0

    def __repr__(self):
        return f"index: {self.index}"


    def get_tile(self):
        return self.map.get_tile(self)

    def rotate(self):
        self.dir[self.on_black_tile] *= -1
        self.dir[0], self.dir[1] = self.dir[1], self.dir[0]


    def update(self, dt):
        # Counter that regulates ant's speed in simulation
        self.counter += dt
        while self.counter >= self.speed:
            self.counter -= self.speed
            self.step_counter += 1

            # Next Step Logic
            self.on_black_tile = self.get_tile()
            self.rotate()
            self.pos[0] += self.dir[0]
            self.pos[1] += self.dir[1]

            # What to do if ant leaves the screen?
            if self.pos[0] < 0:
                self.pos[0] = stg.SCR_WIDTH//DOT_SIZE
            elif self.pos[0] > stg.SCR_WIDTH//DOT_SIZE:
                self.pos[0] = 0
            elif self.pos[1] < 0:
                self.pos[1] = stg.SCR_HEIGHT//DOT_SIZE
            elif self.pos[1] > stg.SCR_HEIGHT//DOT_SIZE:
                self.pos[1] = 0


class Map:
    def __init__(self):
        # Ants' colors, ant.index points to its color
        self.colors = [
            (0, 0, 0),
            (255, 0, 0),
            (0, 255, 0),
            (0, 0, 255)
        ]
        self.width = stg.SCR_WIDTH//DOT_SIZE + 1
        self.height = stg.SCR_HEIGHT//DOT_SIZE + 1

        # Matrix, which size is determined by how many DOT_SIZE tiles fit in it.
        # White tiles are represented by -1, black/colored tiles by anything else
        self.matrix = [
            [-1 for y in range(self.height)]
            for x in range(self.width)
        ]


    def get_tile(self, ant):
        """Returns True if ant is on non-white tile, False otherwise."""
        if self.matrix[ant.pos[0]][ant.pos[1]] == -1:
            self.matrix[ant.pos[0]][ant.pos[1]] = ant.index
            return False
        else:
            self.matrix[ant.pos[0]][ant.pos[1]] = -1
            return True


    def draw(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.matrix[x][y] != -1:
                    arcade.draw_point(x*DOT_SIZE, y*DOT_SIZE, self.colors[self.matrix[x][y]], DOT_SIZE)



class LangtonAntSimulation:
    def __init__(self, _speed):
        self.map = Map()
        self.ants = []

        # TESTS - CREATING SOME ANTS
        self.ants.append(
            Ant(self.map, _speed * 4, stg.SCR_WIDTH // 2 - 200, stg.SCR_HEIGHT // 2 + 100, _index=1, _dir='D')
        )
        self.ants.append(
            Ant(self.map, _speed, stg.SCR_WIDTH // 2 + 200, stg.SCR_HEIGHT // 2 - 100, _index=2, _dir='L')
        )
        self.ants.append(
            Ant(self.map, _speed, stg.SCR_WIDTH // 2, stg.SCR_HEIGHT // 2)
        )

        print(self.ants[0])
        print(self.ants[1])

    def update(self, dt):
        for ant in self.ants:
            ant.update(dt)

    def draw(self):
        self.map.draw()
