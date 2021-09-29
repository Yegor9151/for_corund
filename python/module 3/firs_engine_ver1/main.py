from first_engine.game import Game
from first_engine.objects import *


class MyGame(Game):

    def run(self):  # рабочая область

        char = Character()

        while True:

            self.fps_control()
            self.display_update()
            self.surface.fill((0, 0, 0))

            char.blit(self.surface)
            char.motion()

            for event in self.get_events():
                self.close(event)


MyGame().run()
