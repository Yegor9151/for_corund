from first_engine.game import Game
from first_engine.characters import Character
from first_engine.borders import Border


class MyGame(Game):

    def run(self):  # рабочая область

        char = Character(speed=4)  # создаем перса
        char.load_sprite(name='run_right', path='./viking/run/right/', update=6)
        char.load_sprite(name='run_left', path='./viking/run/left/', update=6)
        char.load_sprite(name='stand_right', path='./viking/stand/right/', update=6)

        while True:

            self.fps_control()
            self.display_update()
            self.surface.fill((0, 0, 0))

            char.motion_right()
            char.play_animation()
            char.blit(self.surface)

            for event in self.get_events():
                self.close(event)


MyGame().run()
