import pygame


class Object:

    def __init__(self, parent: pygame.Surface,
                 width=40, height=40, x=0, y=0,
                 color=(255, 255, 255),
                 speed=2):
        self.parent = parent
        self.color = color
        self.speed = speed

        self.skin = pygame.Surface(size=(width, height))
        self.skin.fill(color=self.color)
        self.body = self.skin.get_rect(topleft=(x, y))

    def blit(self):
        self.parent.blit(source=self.skin, dest=self.body)

    def recolor(self, color):
        self.skin.fill(color=color)

    def motion(self):
        left = pygame.key.get_pressed()[97]
        right = pygame.key.get_pressed()[100]
        up = pygame.key.get_pressed()[115]
        down = pygame.key.get_pressed()[119]

        self.body.x -= left * self.speed
        self.body.x += right * self.speed
        self.body.y += up * self.speed
        self.body.y -= down * self.speed

    def change_speed(self, speed):
        self.speed = speed
