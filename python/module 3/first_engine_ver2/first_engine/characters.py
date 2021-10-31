from .objects import Object
import pygame


class Character(Object):

    def __init__(self, x=10, y=10, width=40, height=40, color=(255, 255, 255), speed=1):
        super().__init__(x, y, width, height, color)
        self.speed = speed

        self.action = 'stand_right'

    def motion(self):

        right = pygame.key.get_pressed()[100]
        left = pygame.key.get_pressed()[97]
        up = pygame.key.get_pressed()[119]
        down = pygame.key.get_pressed()[115]
        jump = pygame.key.get_pressed()[32]

        stand = (left + right + up + down + jump) == 0

        if stand and 'left' in self.action:
            self.action = 'stand_left'
        elif stand and 'right' in self.action:
            self.action = 'stand_right'

        self.actions = {'left': left, 'right': right, 'up': up, 'down': down,
                        'jump': jump, 'default': stand}

        return self.actions

    def motion_right(self):
        right = self.motion()['right']
        if right:
            self.rect.x += right * self.speed
            self.action = 'run_right'

        return right
