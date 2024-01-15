import arcade


DOT_SIZE = 4


class Ant:
    def __init__(self, _map, _speed):
        self.map = _map
        self.tile = (255, 255, 255)
        self.on_black_tile = False
        self.dir = [0, DOT_SIZE]
        self.pos = [540, 360]
        self.step_counter = 0

        self.speed = 1.0 / _speed
        self.counter = 0.0

        self.offscreen = False

    def __repr__(self):
        return f'Ant <dir: {self.dir}>'

    def get_tile(self):
        return self.map.get_tile((self.pos[0], self.pos[1]))
        # return arcade.get_pixel(self.pos[0], self.pos[1])

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
            self.tile = self.get_tile()
            self.on_black_tile = self.tile == (0, 0, 0)
            self.rotate()
            self.pos[0] += self.dir[0]
            self.pos[1] += self.dir[1]

        if self.pos[0] < 0 or self.pos[0] > self.map.width or self.pos[1] < 0 or self.pos[1] > self.map.height:
            self.offscreen = True


class Map:
    def __init__(self):
        self.width, self.height = 1080, 720
        self.black_points: list[tuple[int, int]] = []

    def get_tile(self, pos):
        if pos in self.black_points:
            self.black_points.remove(pos)
            return 0, 0, 0
        self.black_points.append(pos)
        return 255, 255, 255


    def draw(self):
        for point in self.black_points:
            arcade.draw_point(point[0], point[1], (0, 0, 0), DOT_SIZE)



class LangtonAntSimulation:
    def __init__(self, _animation_speed):
        self.map = Map()
        self.ant = Ant(self.map, _animation_speed)

        self.active_process = True

    def update(self, dt):
        if not self.ant.offscreen:
            self.ant.update(dt)
        else:
            self.end_process()

    def draw(self):
        self.map.draw()

    def end_process(self):
        self.active_process = False
        # arcade.exit()
