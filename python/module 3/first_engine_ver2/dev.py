from first_engine.game import Game
from first_engine.characters import Character
from first_engine.borders import Border

import pygame
import os


class MyGame(Game):

    def run(self):  # рабочая область

        char = Character()  # создаем перса

        run = './viking/run/right/'
        run = [pygame.image.load(run + img) for img in os.listdir(run)]  # загружаете нужный спрайт

        time_to_sprite_update = 10
        sprite_id = 0

        while True:

            self.fps_control()
            self.display_update()
            self.surface.fill((0, 0, 0))

            sides = char.motion()
            print(sides)  # отслеживаете направление

            self.surface.blit(run[sprite_id], dest=(0, 0))  # АНИМАЦИЯ

            time_to_sprite_update -= 1
            if time_to_sprite_update == 0:
                time_to_sprite_update = 10
                sprite_id += 1
                if sprite_id == len(run):
                    sprite_id = 0

            for event in self.get_events():
                self.close(event)


MyGame().run()
