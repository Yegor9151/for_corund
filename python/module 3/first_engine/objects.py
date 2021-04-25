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
        if sum((pygame.key.get_pressed()[100], pygame.key.get_pressed()[115],
                pygame.key.get_pressed()[97], pygame.key.get_pressed()[119])) > 1:
            speed = self.speed / 2
        else:
            speed = self.speed

        self.body.x += pygame.key.get_pressed()[100] * speed
        self.body.x -= pygame.key.get_pressed()[97] * speed
        self.body.y += pygame.key.get_pressed()[115] * speed
        self.body.y -= pygame.key.get_pressed()[119] * speed

    def change_speed(self, speed):
        self.speed = speed
