import pygame

from objects import Object


class Projectile:
    """
    Класс содержит в себе следующие методы:
        __init__ - принимает параметров класса
        place - отрисовывает снаряд
        trajectory - расчитывает траекторию
        fly - меняет местоположение снаряда

    :var GREEN: tuple - цвет снаряда по умолчанию
    :var speed_factor: tuple - скорость с которой снаряд будет изменять свое место положение
    """

    speed_factor = (0.0, 0.0)

    def __init__(self,
                 parentSurface: pygame.Surface = None,
                 img_file: str = None, color: tuple = (255, 100, 0), size: tuple = (20, 20),
                 position: list = None, target: tuple = None,
                 speed: float = 15):
        """
        Метод для принимания параметров класса

        :param parentSurface: Surface - родительское окно
        :param position: list - начальное положение снаряда
        :param target: tuple - цель
        :param speed: коеффициент скорости
        """
        self.parentSurface = parentSurface  # родительское окно

        # СКИН ПЕРСОНАЖА
        if img_file:
            self.bodySurface = pygame.image.load(img_file)  # создание пересонажа
            self.bodySurface.set_colorkey((255, 255, 255))
        else:
            self.bodySurface = pygame.Surface(size)  # создание пересонажа
            self.bodySurface.fill(color)  # заполнение персонажа

        self.bodyRect = self.bodySurface.get_rect(topleft=position)

        self.position = position
        self.target = target
        self.speed = speed

    def place(self) -> pygame.Rect:
        """
        Рисует снаряд на родительском окне
        :return Rect: тело снаряда
        """

        if self.position:
            return self.parentSurface.blit(self.bodySurface, self.position)

    def trajectory(self):
        """
        Считать направление движения снаряда от начальной позиции к цели

        :return self.speed_factor: направление снаряда по XY
        """
        distance_to_target = (self.target[0] - self.position[0],  # X
                              self.target[1] - self.position[1])  # Y
        distance_sum = sum(tuple(map(abs, distance_to_target)))

        self.speed_factor = ((distance_to_target[0] / distance_sum) * self.speed,  # X
                             (distance_to_target[1] / distance_sum) * self.speed)  # Y

        return self.speed_factor

    def fly(self):
        """
        Меняет местоположение снаряда
        :return self.position: list - текущее положение снаряда
        """

        if self.position:
            self.position[0] += self.speed_factor[0]
            self.position[1] += self.speed_factor[1]
            return self.position
