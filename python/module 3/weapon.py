import pygame


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
    GREEN = (0, 255, 0)

    speed_factor = (0.0, 0.0)

    def __init__(self,
                 parentSurface: pygame.Surface = None,
                 position: list = None, target: tuple = None,
                 speed: float = 15):
        """
        Метод для принимания параметров класса

        :param parentSurface: Surface - родительское окно
        :param position: list - начальное положение снаряда
        :param target: tuple - цель
        :param speed: коеффициент скорости
        """
        self.parentSurface = parentSurface
        self.speed = speed

        self.position = position
        self.target = target

    def place(self) -> pygame.Rect:
        """
        Рисует снаряд на родительском окне
        :return Rect: тело снаряда
        """

        if self.position:
            return pygame.draw.circle(self.parentSurface, self.GREEN, self.position, 5)

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
