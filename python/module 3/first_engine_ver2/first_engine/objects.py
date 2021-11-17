import pygame
import os


class Object:
    """Общий класс для создания любых объектов и классов"""
    spritesDict = {}  # словарик для спрайтов
    sprite_id = 0
    action = None  # текущее действие
    actions = {}

    def __init__(self, x=10, y=10, width=40, height=40, color=(255, 255, 255)):
        """
        Конструктор класса
        :param x: местоположение на экране
        :param y: местоположение на экране
        :param width: габариты
        :param height: габариты
        :param color: цвет

        :param surface: внешний вид
        :param rect: координаты тела
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

        self.surface = pygame.Surface(size=(self.width, self.height))
        self.surface.fill(color=self.color)
        self.rect = self.surface.get_rect(topleft=(x, y))

    def load_sprite(self, name: str, path: str, update: int = 6):
        """
        Метод для загрузки спрайтов
        :param name: название спрайтов (есть список служебных слов, которые должны содержаться в названии спрайтов для
        отображающих базовые действий: run_left, run_right, attack_right, attack_left, stand_right, stand_left)
        :param path: путь до папки со спрайтами
        :param update: частота обновления данного спрайта
        :return: список загруженных спрайтов, если нужно
        """
        spriteList = [pygame.image.load(path + name) for name in os.listdir(path)]
        self.spritesDict[name] = {'spriteList': spriteList,
                                  'updateConst': update,
                                  'update': update}
        return spriteList

    def sprite_update(self, name: str):
        """
        Метод для обновления спрайтов
        :param name: название спрайтов в spritesDict
        :return: None
        """

        self.spritesDict[name]['update'] -= 1  # использовать из spritesDict 'update'

        if self.spritesDict[name]['update'] == 0:
            self.sprite_id += 1
            self.spritesDict[name]['update'] = self.spritesDict[name]['updateConst']

            if self.sprite_id == len(self.spritesDict[name]['spriteList']):
                self.sprite_id = 0

    def animation_rebuild(self, name: str):
        """
        Мето для перестройки хитбокса на основе текущего спрайта
        :param name: название спрайтов в spritesDict
        :return: None
        """

        self.surface = self.spritesDict[name]['spriteList'][self.sprite_id]
        self.rebuild(rect=self.surface.get_rect())

    def play_animation(self):
        """
        Запуск анимации спрайтов
        :return: None
        """
        self.sprite_update(self.action)
        self.animation_rebuild(self.action)

    def rebuild(self, width=None, height=None, color=None, rect=None):
        """
        Метод для перестройки хитбоксов
        :param width: габариты
        :param height: габариты
        :param color: цвет
        :param rect: общие данные о хитбоксе
        :return: None
        """
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
        """
        Отрисовка на родительском окне
        :param surface: родительское окно
        :return: None
        """
        surface.blit(source=self.surface, dest=self.rect)
