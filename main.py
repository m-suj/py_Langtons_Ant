import arcade
import matplotlib
from langtons_ant import LangtonAntSimulation
from sim_settings import *


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)
        self.sim: LangtonAntSimulation = None

    def setup(self):
        self.sim = LangtonAntSimulation(SIM_SPEED)

    def on_update(self, delta_time):
        self.sim.update(delta_time)

    def on_draw(self):
        self.clear()
        self.sim.draw()


def main():
    game = MyGame(SCR_WIDTH, SCR_HEIGHT, SCR_TITLE)
    game.setup()
    arcade.run()


if __name__ == '__main__':
    main()