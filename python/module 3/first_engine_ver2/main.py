"""Quick start"""

from first_engine.game import Game
from first_engine.characters import Character
from first_engine.borders import Border
from first_engine.objects import Object
import pygame


class MyGame(Game):

    def run(self):  # рабочая область

        bg_x = 0
        speed = 8

        self.load_bg('./sarah-clark-environment.png')

        char = Character(speed=speed)  # создаем перса

        char.load_sprite(name='run_right', path='./viking/run/right/', update=6)
        char.load_sprite(name='run_left', path='./viking/run/left/', update=6)
        char.load_sprite(name='stand_right', path='./viking/stand/right/', update=6)
        char.load_sprite(name='stand_left', path='./viking/stand/left/', update=6)
        char.load_sprite(name='jump_left', path='./viking/jump/left/', update=6)
        char.load_sprite(name='jump_right', path='./viking/jump/right/', update=6)
        # char.load_sprite(name='attack1_right', path='./viking/attack2/right/', update=6)
        # char.load_sprite(name='attack1_left', path='./viking/attack2/left/', update=6)

        char.set_gravitation(15)

        ground = Border(x=0, y=self.h - 40, width=self.w, height=40)
        platform1 = Border(x=200, y=200, width=200, height=40)

        enemy = Object(color=(255, 0, 0), y=200)

        while self.cycle:

            # Перемешения
            char.drop()
            right = char.motion_right()
            left = char.motion_left()

            # сопротивление с поверхностями
            floor = ground.resistance([char]) + \
                     platform1.resistance([char])

            # Прыжки
            char.jump(floor, start_jump_speed=20)  # прыжок

            if char.rect.right > 400 and bg_x > -50:
                char.rect.right = 400
                platform1.rect.right -= right * speed
                bg_x -= right
            elif char.rect.left < 200 and bg_x < 0:
                char.rect.left = 200
                platform1.rect.left += left * speed
                bg_x += left

            # print(enemy.rect.colliderect(char.rect))

            # отрисовка
            self.fps_control()
            # self.surface.fill((0, 0, 0))
            self.surface.blit(self.bg, dest=(bg_x, -140))  # отрисовка экрана

            char_attack = char.attack()
            if char_attack=='right':
                attack_box = Object(color=(255, 0, 0), x=char.rect.right, y=char.rect.y)
                attack_box.blit(self.surface)

            if char_attack == 'left':
                attack_box = Object(color=(255, 0, 0), x=char.rect.left - 40, y=char.rect.y)
                attack_box.blit(self.surface)

            char.play_animation()

            char.blit(self.surface)
            # ground.blit(self.surface)
            platform1.blit(self.surface)
            enemy.blit(self.surface)

            self.display_update()

            # обработка событий
            for event in self.get_events():
                # print(event)
                self.close(event)


MyGame().run()
