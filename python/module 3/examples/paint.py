import pygame
from first_engine.game import Game


class FirstGame(Game):

    def run(self) -> None:

        draw = False
        x, y = None, None
        color = self.parent_color

        while self.RUNNER:

            self.display_update()
            self.fps_counter(FPS=1920)

            for event in self.events():
                print(event)  # отслеживание событий

                if event.type == 1025:
                    if event.button == 1:
                        color = (255, 255, 255)
                    elif event.button == 3:
                        color = self.parent_color
                    x, y = event.pos
                    draw = True
                elif event.type == 1026:
                    x, y = None, None
                    draw = False

                if draw and event.type == 1024:
                    x, y = event.pos

                if event.type == 768 and event.key == 99:
                    self.window_fill()

                self.close(event)

            if (x is not None) and (y is not None):
                pygame.draw.rect(surface=self.parentSurface, color=color, rect=(x, y, 5, 5))


FirstGame(color=(100, 200, 100)).run()
