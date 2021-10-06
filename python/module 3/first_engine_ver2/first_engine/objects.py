import pygame


class Object:

    def __init__(self, width=40, height=40, color=(255, 255, 255), x=10, y=10):
        self.width = width
        self.height = height
        self.color = color
        self.x = x
        self.y = y

        self.surface = pygame.Surface(size=(self.width, self.height))
        self.surface.fill(color=self.color)
        self.rect = self.surface.get_rect(topleft=(self.x, self.y))

    def rebuild(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        self.surface = pygame.Surface(size=(self.width, self.height))
        self.surface.fill(color=self.color)
        self.rect = self.surface.get_rect(topleft=(self.x, self.y))

    def blit(self, surface):
        surface.blit(source=self.surface, dest=self.rect)
