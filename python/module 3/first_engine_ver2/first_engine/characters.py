from .objects import Object
import pygame


class Character(Object):

    def __init__(self, x=10, y=10, width=40, height=40, color=(255, 255, 255), speed=1):
        super().__init__(x, y, width, height, color)
        self.speed = speed

    def motion(self, speed=None):
        speed = speed if speed else self.speed

        self.rect.x += pygame.key.get_pressed()[100] * speed
        self.rect.x -= pygame.key.get_pressed()[97] * speed
        self.rect.y += pygame.key.get_pressed()[115] * speed
        self.rect.y -= pygame.key.get_pressed()[119] * speed

        return pygame.key.get_pressed()[100] * speed
