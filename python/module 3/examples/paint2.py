from first_engine.game import Game
from first_engine.objects import Object


class FirstGame(Game):

    def run(self):

        draw = False
        w, h = 5, 5
        brash = Object(parent=self.parentSurface, width=w, height=w)

        while self.RUNNER:
            self.fps_counter(60000)
            self.display_update()

            for event in self.events():
                print(event)  # отслеживание событий

                if event.type == 1025:
                    draw = True
                    if event.button == 1:
                        brash.color = (255, 255, 255)
                        brash.body.center = event.pos
                        brash.blit()
                    elif event.button == 3:
                        brash.color = self.parent_color
                        brash.body.center = event.pos
                        brash.blit()
                elif event.type == 1026:
                    draw = False

                if draw and event.type == 1024:
                    brash.body.center = event.pos
                    brash.blit()

                if event.type == 1027:
                    w += event.y
                    h += event.y
                    if w < 1 or h < 1:
                        w, h = 1, 1
                    brash = Object(parent=self.parentSurface, width=w, height=h)

                if event.type == 768 and event.key == 99:
                    self.window_fill()

                self.close(event)


FirstGame().run()
