from first_engine.game import Game
from first_engine import objects
import pygame


class FirstGame(Game):
    def run(self):
        hero = objects.Character(self.surface, speed=8)
        hero.load_sprites(name='stand_right', path='./sprites/viking/stand/right')
        hero.load_sprites(name='stand_left', path='./sprites/viking/stand/left')
        hero.load_sprites(name='run_left', path='./sprites/viking/run/left')
        hero.load_sprites(name='run_right', path='./sprites/viking/run/right')

        wall = objects.Barrier(self.surface, objects=[hero], width=200, height=50, x=300, y=450)

        game_over = False
        while self.RUNNER:
            if not game_over:
                self.cycle_init(FPS=60)

                # Объекты
                hero.blit()
                wall.blit()

                # проверяем - уперся ли персонаж в преграду
                self.window_borders([wall, hero])
                wall.resistance()

                # Движения персонажа
                hero.motion_left(sprites_active='run_left', sprite_inactive='stand_left', time_to_update=6)
                hero.motion_right(sprites_active='run_right', sprite_inactive='stand_right', time_to_update=6)
                # роняем персонажа
                hero.drop(speed_up=1, max_speed=20)

                # проверяем - уперся ли персонаж в преграду
                self.window_borders([hero])
                wall.resistance()

                # если да, то даем ему возможность прыгать
                hero.action_jump()

            for event in self.events():
                # print(event)  # отслеживание событий
                self.close(event)


FirstGame(width=800, height=600).run()
