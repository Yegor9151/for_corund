import pygame


class Object:

    def __init__(self, x=10, y=10, width=40, height=40, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

        self.surface = pygame.Surface(size=(self.width, self.height))
        self.surface.fill(color=self.color)
        self.rect = self.surface.get_rect(topleft=(x, y))

    def rebuild(self, width=None, height=None, color=None, rect=None):
        self.width = width if width else self.width  # <
        self.height = height if height else self.height  # <
        self.color = color if color else self.color  # <

        if rect:
            self.width, self.height = rect[2:]

        self.surface = pygame.Surface(size=(self.width, self.height))
        self.surface.fill(color=self.color)
        self.rect = self.surface.get_rect(topleft=(self.rect[:2]))

    def blit(self, surface):
        surface.blit(source=self.surface, dest=self.rect)
