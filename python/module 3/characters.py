import pygame

from weapon import Projectile
from objects import Object

"""
Данный модуль, содержит в себе такие классы как:

Player - служащий для создания персонажа.
"""


class Character(Object):
    """
    Класс для создания персонажа

    Данный класс содержит в себе такие методы как:

    __init__ - служит для принятия аргуметров класса
    place - служит для отрисовки персонажа
    """

    def __init__(self, parentSurface: pygame.Surface = None,
                 img_file: str = None, color: tuple = (255, 255, 255),
                 size: tuple = (40, 40), position: list = (100, 100),
                 speed: int = 1, health: int = 100, damage: int = 5):
        """
        Метод для принятия аргументов класса

        :parameter parentSurface: родительское окно, на котором будет отрисовываться объект
        :parameter size: размер персонажа
        :parameter color: цвет персонажа
        :parameter speed: скорость персонажа
        :parameter health: здоровье персонажа
        """

        super().__init__(parentSurface, img_file, position, size, color)

        # ПАРАМЕТРЫ
        self.speed = speed
        self.health = health
        self.damage = damage

    def place(self) -> pygame.Rect:
        """
        Метод для отрисовки персонажа на родитеском окне
        output: Rect родитеского окна
        """
        if self.health > 0:
            self.parentSurface.blit(self.bodySurface, self.bodyRect)
            return self.bodyRect


class Player(Character):
    """
    Класс для создания персонажа

    Данный класс содержит в себе такие методы как:

    __init__ - служит для принятия аргуметров класса
    place - служит для отрисовки персонажа
    move - служаший для управления перемещением пермонажа
    """

    LEFT = RIGHT = UP = DOWN = False  # направления движений

    def move(self) -> pygame.Rect.topleft:
        """
        Метод для перемешения персонажа в зависимости от активации направления
        output: верхние-левые координаты персонажа
        """
        if self.LEFT:
            self.bodyRect.x -= self.speed
        if self.RIGHT:
            self.bodyRect.x += self.speed
        if self.UP:
            self.bodyRect.y -= self.speed
        if self.DOWN:
            self.bodyRect.y += self.speed

        return self.bodyRect.center

    def attack(self, target):
        projectile = Projectile(self.parentSurface,
                                img_file='./objects/Fireboll.png',
                                position=list((self.bodyRect.center[0]-50, self.bodyRect.center[1]-50)),
                                target=target,
                                speed=10)
        projectile.trajectory()

        return projectile


class Enemy(Character):
    pass