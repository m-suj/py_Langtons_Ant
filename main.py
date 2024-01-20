import arcade
from langtons_ant import LangtonAntSimulation
from sim_settings import *


# TODO: langtons_ant.py[30:34] - display each ant's step counter on screen


class MyWindow(arcade.Window):
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

    def on_close(self):
        print('Closing...')
        self.close()
        print('Successfully closed')


def main():
    window = MyWindow(SCR_WIDTH, SCR_HEIGHT, SCR_TITLE)
    window.setup()
    arcade.run()


if __name__ == '__main__':
    main()