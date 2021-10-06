from .objects import Object
import pygame


class Character(Object):

    def __init__(self, width=40, height=40, color=(255, 255, 255), x=10, y=10, speed=1):
        super().__init__(width, height, color, x, y)

        self.speed = speed

    def motion(self, speed=None):
        speed = speed if speed else self.speed

        self.rect.x += pygame.key.get_pressed()[100] * speed
        self.rect.x -= pygame.key.get_pressed()[97] * speed
        self.rect.y += pygame.key.get_pressed()[115] * speed
        self.rect.y -= pygame.key.get_pressed()[119] * speed
