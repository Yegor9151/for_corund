from .objects import Object
import pygame


class Character(Object):
    """
    Класс для создания персонажа
    """
    __gravitation_const = 15
    __gravitation_value = 15

    def __init__(self, x=10, y=10, width=40, height=40, color=(255, 255, 255), speed=1):
        super().__init__(x, y, width, height, color)
        """
        Конструктор, класса для инициализации персонажа
        :param x: местоположение
        :param y: местоположение
        :param width: габариты
        :param height: габариты
        :param color: цвет
        :param speed: скорость пердвижения

        """
        self.speed = speed

        self.action = 'stand_right'

    def motion(self):
        """
        Метод для отслеживания нажатий: left, right, up, down, space, mouse1, mouse2. mouse3, space, default
        :return: словать - название нажатия: наличие нажатия
        """

        right = pygame.key.get_pressed()[100]
        left = pygame.key.get_pressed()[97]
        up = pygame.key.get_pressed()[119]
        down = pygame.key.get_pressed()[115]
        space = pygame.key.get_pressed()[32]

        mouse1 = pygame.mouse.get_pressed(3)[0]
        mouse2 = pygame.mouse.get_pressed(3)[1]
        mouse3 = pygame.mouse.get_pressed(3)[2]

        default = (left + right + up + down + space + mouse1 + mouse2 + mouse3) == 0

        if default and 'left' in self.action:
            self.action = 'stand_left'
        elif default and 'right' in self.action:
            self.action = 'stand_right'

        self.actions = {'left': left, 'right': right, 'up': up, 'down': down,
                        'mouse1': mouse1, 'mouse2': mouse2, 'mouse3': mouse3,
                        'space': space, 'default': default}

        return self.actions

    def attack(self):
        """
        отрисовывает атаку, если спрайты загружены
        :return: "left" / "right"
        """

        attack = self.motion()['mouse1']

        if 'left' in self.action and attack:
            self.action = 'attack_left'
            return 'left'

        elif 'right' in self.action and attack:
            self.action = 'attack_right'
            return 'right'

    def motion_right(self):
        """
        отрисовывает движение вправо, если спрайты загружены
        :return: выполнение действия
        """
        right = self.motion()['right']
        if right:
            self.rect.x += right * self.speed
            self.action = 'run_right'

        return right

    def motion_left(self):
        """
        отрисовывает движение влево, если спрайты загружены
        :return: выполнение действия
        """
        left = self.motion()['left']
        if left:
            self.rect.x -= left * self.speed
            self.action = 'run_left'

        return left

    def set_gravitation(self, value):
        """
        Добавляет силу гравитации
        :param value: значение
        :return: None
        """
        self.__gravitation_const = value
        self.__gravitation_value = value

    def drop(self):
        """
        Заставляет объект падать
        :return: None
        """
        self.rect.y += self.__gravitation_value

    def jump(self, floor: list, start_jump_speed=20):
        """
        совершает прыжки
        :param floor: поверхность для отталкивания
        :param start_jump_speed:
        :return:
        """
        surf = []
        for fl in floor:
            surf += fl

        if 'top' in surf and self.motion()['space']:
            self.__gravitation_value = -start_jump_speed

        if self.__gravitation_value < self.__gravitation_const:
            self.__gravitation_value += 1
