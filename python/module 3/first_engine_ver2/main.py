from first_engine.game import Game
from first_engine.characters import Character
from first_engine.borders import Border
import pygame


class MyGame(Game):

    def run(self):  # рабочая область

        stand_right = pygame.image.load('./viking/stand/right/1.png')
        run_right = pygame.image.load('./viking/run/right/1.png')

        x, y, width, height = stand_right.get_rect()

        char = Character(x, y, width, height, speed=4)

        while True:

            self.fps_control()
            self.display_update()
            self.surface.fill((0, 0, 0))

            right = char.motion()

            # char.blit(self.surface)
            if right:
                self.surface.blit(run_right, char.rect)
                char.rebuild(rect=run_right.get_rect())
            else:
                self.surface.blit(stand_right, char.rect)
                char.rebuild(rect=stand_right.get_rect())

            for event in self.get_events():
                self.close(event)


MyGame().run()
