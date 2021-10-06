from first_engine.game import Game
from first_engine.characters import Character
from first_engine.borders import Border


class MyGame(Game):

    def run(self):  # рабочая область

        char = Character(speed=4)
        wall = Border(width=150, height=150, color=(255, 200, 200), x=150, y=100)

        while True:

            self.fps_control()
            self.display_update()
            self.surface.fill((0, 0, 0))

            char.blit(self.surface)
            char.motion()

            wall.blit(self.surface)
            wall.resistance([char])

            for event in self.get_events():
                self.close(event)


MyGame().run()
