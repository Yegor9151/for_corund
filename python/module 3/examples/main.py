from first_engine.game import Game
from first_engine.objects import Character, Barrier


class FirstGame(Game):
    def run(self):
        char = Character(self.surface, speed=4)
        wall = Barrier(self.surface, objects=[char],
                       width=200, height=200,
                       x=100, y=100, color=(255, 200, 200))

        game_over = False
        while self.RUNNER:
            if not game_over:
                self.cycle_init(objects=[char])

                char.motion_control()
                char.blit()

                wall.resistance()
                wall.blit()

            for event in self.events():
                # print(event)  # отслеживание событий
                self.close(event)


FirstGame(width=600, height=400).run()
