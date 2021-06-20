from first_engine.game import Game
from first_engine import objects


class FirstGame(Game):
    def run(self):
        self.load_bg('./sarah-clark-environment.png')

        hero = objects.Character(self.surface, speed=8)
        hero.load_sprites(name='stand_right', path='./sprites/viking/stand/right/')
        hero.load_sprites(name='stand_left', path='./sprites/viking/stand/left/')
        hero.load_sprites(name='run_left', path='./sprites/viking/run/left/')
        hero.load_sprites(name='run_right', path='./sprites/viking/run/right/')

        wall = objects.Barrier(self.surface, objects=[hero], width=200, height=50, x=300, y=400)
        wall2 = objects.Barrier(self.surface, objects=[hero], width=200, height=300, x=600, y=300)

        game_over = False
        while self.RUNNER:
            if not game_over:
                self.cycle_init(FPS=60)
                wall.blit()
                wall2.blit()

                # Объекты
                hero.blit()
                hero.play_animation()

                hero.drop(speed_up=1, max_speed=20)
                left = hero.motion_left()
                right = hero.motion_right()
                bg_speed = -right if right else left

                self.bg_motion(char=hero, bg_speed=bg_speed // 2, objects=[wall, wall2], object_speed=bg_speed)

                wall.resistance()
                wall2.resistance()

                self.window_borders([hero])

                hero.action_jump()

            for event in self.events():
                # print(event)  # отслеживание событий
                self.close(event)


FirstGame(width=800, height=600).run()