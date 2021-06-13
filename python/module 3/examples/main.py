from first_engine.game import Game
from first_engine import objects


class FirstGame(Game):
    def run(self):
        hero = objects.Character(self.surface, speed=8)
        hero.load_sprites(name='stand_right', path='./sprites/viking/stand/right/')
        hero.load_sprites(name='stand_left', path='./sprites/viking/stand/left/')
        hero.load_sprites(name='run_left', path='./sprites/viking/run/left/')
        hero.load_sprites(name='run_right', path='./sprites/viking/run/right/')

        game_over = False
        while self.RUNNER:
            if not game_over:
                self.cycle_init(FPS=60)

                # Объекты
                hero.blit()
                hero.play_animation()
                hero.motion_left()
                hero.motion_right()

                self.window_borders([hero])

            for event in self.events():
                # print(event)  # отслеживание событий
                self.close(event)


FirstGame(width=800, height=600).run()
