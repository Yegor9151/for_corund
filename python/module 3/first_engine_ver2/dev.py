from first_engine.game import Game
from first_engine.characters import Character
from first_engine.borders import Border
import pygame


class MyGame(Game):

    def run(self):  # рабочая область

        gravitation = 15
        bg_x = 0
        speed = 8

        self.load_bg('./sarah-clark-environment.png')

        char = Character(speed=speed)  # создаем перса
        char.load_sprite(name='run_right', path='./viking/run/right/', update=6)
        char.load_sprite(name='run_left', path='./viking/run/left/', update=6)
        char.load_sprite(name='stand_right', path='./viking/stand/right/', update=6)
        char.load_sprite(name='stand_left', path='./viking/stand/left/', update=6)

        ground = Border(x=0, y=self.h - 40, width=self.w, height=40)
        platform1 = Border(x=200, y=200, width=200, height=40)

        while self.cycle:

            # Перемешения
            right = char.motion_right()
            left = char.motion_left()

            # Прыжок и падение
            char.rect.y += gravitation  # падение

            # сопротивление с поверхностями
            rsides = ground.resistance([char]) + \
                     platform1.resistance([char])

            gravitation = char.jump(rsides, gravitation, start_jump_speed=20)  # прыжок

            if gravitation < 15:
                gravitation += 1

            if char.rect.right > 400 and bg_x > -50:
                char.rect.right = 400
                platform1.rect.right -= right * speed
                bg_x -= right
            elif char.rect.left < 200 and bg_x < 0:
                char.rect.left = 200
                platform1.rect.left += left * speed
                bg_x += left

            # отрисовка
            self.fps_control()
            # self.surface.fill((0, 0, 0))
            self.surface.blit(self.bg, dest=(bg_x, -140))  # отрисовка экрана

            char.play_animation()

            char.blit(self.surface)
            # ground.blit(self.surface)
            platform1.blit(self.surface)

            self.display_update()

            # обработка событий
            for event in self.get_events():
                # print(event)
                self.close(event)


MyGame().run()
