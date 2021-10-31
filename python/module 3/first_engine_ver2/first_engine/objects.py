import pygame
import os


class Object:
    spritesDict = {}  # словарик для спрайтов
    sprite_id = 0
    action = None # текущее действие
    actions = {}

    def __init__(self, x=10, y=10, width=40, height=40, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

        self.surface = pygame.Surface(size=(self.width, self.height))
        self.surface.fill(color=self.color)
        self.rect = self.surface.get_rect(topleft=(x, y))

    def load_sprite(self, name: str, path: str, update: int = 6):
        """метод для загрузки спрайтов"""
        spriteList = [pygame.image.load(path + name) for name in os.listdir(path)]
        self.spritesDict[name] = {'spriteList': spriteList, 'updateConst': update, 'update': update}

        return spriteList

    def sprite_update(self, name: str):

        self.spritesDict[name]['update'] -= 1  # использовать из spritesDict 'update'

        if self.spritesDict[name]['update'] == 0:
            self.sprite_id += 1
            self.spritesDict[name]['update'] = self.spritesDict[name]['updateConst']

            if self.sprite_id == len(self.spritesDict[name]['spriteList']):
                self.sprite_id = 0

        return self.sprite_id

    def animation_rebuild(self, name: str):

        self.surface = self.spritesDict[name]['spriteList'][self.sprite_id]
        self.rebuild(rect=self.surface.get_rect())

        return self.surface

    def play_animation(self):
        self.sprite_update(self.action)
        self.animation_rebuild(self.action)

    def rebuild(self, width=None, height=None, color=None, rect=None):
        self.width = width if width else self.width  # <
        self.height = height if height else self.height  # <
        self.color = color if color else self.color  # <

        if rect:
            self.width, self.height = rect[2:]

        if not self.spritesDict:
            self.surface = pygame.Surface(size=(self.width, self.height))
            self.surface.fill(color=self.color)

        self.rect = self.surface.get_rect(topleft=(self.rect[:2]))

    def blit(self, surface):
        surface.blit(source=self.surface, dest=self.rect)
