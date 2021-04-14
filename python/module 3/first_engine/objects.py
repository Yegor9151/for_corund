import pygame


class Object:

    def __init__(self, parent: pygame.Surface,
                 width=40, height=40, x=0, y=0,
                 color=(255, 255, 255)):
        self.parent = parent
        self.color = color

        self.skin = pygame.Surface(size=(width, height))
        self.body = self.skin.get_rect(topleft=(x, y))

    def blit(self):
        self.skin.fill(color=self.color)
        self.parent.blit(source=self.skin, dest=self.body)
