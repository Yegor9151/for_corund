"""
Модуль с основным классом-конструктором Game - для создания игры.
"""

import pygame


class Game:
    """
    Класс-конструктор, содержит основные методы и переменные для написания игр
    """

    runner = True

    def __init__(self, width=400, height=300):
        """
        :parameter width: высота окна
        :parameter height: ширина окна
        """
        self.width = width
        self.height = height

        self.parentSurface = pygame.display.set_mode(
            size=(self.width, self.height)
        )  # родительское окно

    @staticmethod
    def events():
        return pygame.event.get()

    def close(self, event) -> None:
        if event.type == 256 or (event.type == 768 and event.key == 27):  # если нажал крестик или ESC
            pygame.quit()  # деинициализируем pygame
            self.runner = False  # отключаем цикл
