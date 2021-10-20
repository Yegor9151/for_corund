from .objects import Object
import pygame


class Character(Object):

    def __init__(self, x=10, y=10, width=40, height=40, color=(255, 255, 255), speed=1):
        super().__init__(x, y, width, height, color)
        self.speed = speed

    def motion(self, speed=None):
        speed = speed if speed else self.speed

        right = pygame.key.get_pressed()[100]
        left = pygame.key.get_pressed()[97]
        up = pygame.key.get_pressed()[119]
        down = pygame.key.get_pressed()[115]

        self.rect.x += right * speed
        self.rect.x -= left * speed
        self.rect.y -= up * speed
        self.rect.y += down * speed

        return right, left, up, down
