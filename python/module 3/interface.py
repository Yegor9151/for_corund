import pygame


class HealthBar:

    def __init__(self, parentSurface, character=None, size=(4, 20), xy=(0, 0)):
        self.parentSurface = parentSurface
        self.size = size
        self.xy = xy
        self.character = character

        self.max_healthSurface = pygame.Surface((self.character.health * self.size[0], self.size[1]))
        self.max_healthSurface.fill((200, 200, 200))

    def place(self):
        # максимальное здоровье
        self.parentSurface.blit(self.max_healthSurface, self.xy)

        # текущее здоровье
        if self.character.health > 0:
            healthSurface = pygame.Surface((self.character.health * self.size[0], self.size[1]))
            healthSurface.fill((255, 0, 0))
            self.parentSurface.blit(healthSurface, self.xy)

            return self.character.health
