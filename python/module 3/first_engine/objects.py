"""
Модуль для создания объектов типа:
Character - класс для создания персонажей
Barrier - класс для создания непроходимых препятствий
"""

import pygame
import os


class Object:
    """
    Основной класс на основе которого строятся другие классы, представляющие разные типы объектов
    Содержит в себе основные методы для управление всеми объектами
    :var sprites: Dict - сохраняет спрайты созданного на его основе объекта
    :var last_action: str - информация о последнем действии объекта
    :var time_to_sprite_update: int - вряме до смены спрайта, если предполагается анимация
    :var sprite_id: int - индекс спрайта
    """
    sprites = {}
    last_action = 'right'
    time_to_sprite_update = 6
    sprite_id = 0
    drop_speed = 1

    def __init__(self, parent: pygame.Surface, width=40, height=40, x=0, y=0, color: tuple = (255, 255, 255)):
        """
        Метод для построения объекта
        :param parent: pygame.Surface - родимтельское окно
        :param width: int
        :param height: int
        :param x: int
        :param y: int
        :param color: tuple - цвет в RGB
        :var skin: pygame.Surface - скин объекта - по умолчанию
        :var body: Rect - тело объекта - по умолчанию
        """
        self.parent = parent
        self.x, self.y = x, y
        self.color = color
        self.width = width
        self.height = height

        self.skin = pygame.Surface(size=(width, height))
        self.skin.fill(color=color)
        self.body = self.skin.get_rect(topleft=(x, y))

    def load_sprites(self, name: str, path: str):
        """
        Метод для загрузки спрайтов в sprites
        :param name: str - имя под которым будем хранить загруженные скины и созданные тела
        :param path: str - путь до папки с файлами
        :return skins: dict - возвращаем только что загруженные скины и созданные тела
        """
        path = path if path[-1] == '/' else path + '/'

        skins = [pygame.image.load(path + i) for i in os.listdir(path)]
        self.sprites[name] = skins
        return skins

    def sprite_update(self, name, time_update=6):
        """
        Метод обновляющий спрайты по очереди
        :param name: str - принимает имя спрайтов сохраненных в словаре sprites
        :param time_update: int - принимает время до смены спрайта на новый
        :return: int - возвращает id текущего спрайта
        """
        self.time_to_sprite_update -= 1
        if self.time_to_sprite_update == 0:
            self.sprite_id += 1
            self.time_to_sprite_update = time_update
            if self.sprite_id == len(self.sprites[name]):
                self.sprite_id = 0
        return self.sprite_id

    def remake_for_skin(self, name: str, idx: int = 0):
        """
        Метод для переделывания скина и тела по индексу скина и его названия в sprites
        :param name: str название скинов
        :param idx: int индекс
        :return: pygame.Surface
        """
        self.skin = self.sprites[name][idx]
        self.body = self.skin.get_rect(topleft=(self.body.x, self.body.y))
        self.x, self.y = self.body.x, self.body.y
        self.width = self.body.width
        self.height = self.body.height
        return self.skin

    def blit(self):
        """
        Метод для отображения объекта
        :return: pygame.Surface
        """
        self.parent.blit(source=self.skin, dest=self.body)
        return self.parent

    def recolor(self, color):
        """
        Метод для сметы цвета
        :return: RGB
        """
        self.skin.fill(color=color)
        return color

    def drop(self, speed_up=1, max_speed=15):
        """
        Падение персонажа
        :return: int положение тела
        """
        self.body.y += self.drop_speed
        if self.drop_speed < max_speed:
            self.drop_speed += speed_up
        return self.drop_speed


class Character(Object):
    """
    Класс для создания персонажей
    """
    def __init__(self, parent: pygame.Surface, width=40, height=40, x=0, y=0, color=(255, 255, 255),
                 speed=1, height_jump=20):
        """
        :param parent: pygame.Surface - родимтельское окно
        :param width: int
        :param height: int
        :param x: int
        :param y: int
        :param color: tuple - цвет в RGB
        :param speed: int - скорость персонажа
        """
        super().__init__(parent, width, height, x, y, color)
        self.speed = speed
        self.height_jump = height_jump

    def motion_left(self, sprites_active: str = None, sprite_inactive: str = None, time_to_update: int = 6):
        """
        Метод для движения влево, можно подключить загруженные спрайты
        :param sprites_active: имя спрайтов движения
        :param sprite_inactive: имя спрайтов дездействия
        :param time_to_update: время до смены спрайта
        :return: int - скорость
        """
        left = pygame.key.get_pressed()[97] * self.speed
        if left:
            self.body.x -= left
            self.last_action = 'left'
            if sprites_active:
                self.sprite_update(name=sprites_active, time_update=time_to_update)
                self.remake_for_skin(name=sprites_active, idx=self.sprite_id)
        elif sprite_inactive and not left and self.last_action == 'left':
            self.sprite_update(name=sprite_inactive, time_update=time_to_update)
            self.remake_for_skin(name=sprite_inactive, idx=self.sprite_id)
        return left

    def motion_right(self, sprites_active=None, sprite_inactive=None, time_to_update=6):
        """
        Метод для движения вправо, можно подключить загруженные спрайты
        :param sprites_active: имя спрайтов движения
        :param sprite_inactive: имя спрайтов дездействия
        :param time_to_update: время до смены спрайта
        :return: int - скорость
        """
        right = pygame.key.get_pressed()[100] * self.speed
        if right:
            self.body.x += right
            self.last_action = 'right'
            if sprites_active:
                self.sprite_update(name=sprites_active, time_update=time_to_update)
                self.remake_for_skin(name=sprites_active, idx=self.sprite_id)
        elif sprite_inactive and not right and self.last_action == 'right':
            self.sprite_update(name=sprite_inactive, time_update=time_to_update)
            self.remake_for_skin(name=sprite_inactive, idx=self.sprite_id)
        return right

    def motion_up(self, sprites_active=None, sprite_inactive=None, time_to_update=6):
        """
        Метод для движения вверх, можно подключить загруженные спрайты
        :param sprites_active: имя спрайтов движения
        :param sprite_inactive: имя спрайтов дездействия
        :param time_to_update: время до смены спрайта
        :return: int - скорость
        """
        up = pygame.key.get_pressed()[119] * self.speed
        if up:
            self.body.y -= up
            self.last_action = 'up'
            if sprites_active:
                self.sprite_update(name=sprites_active, time_update=time_to_update)
                self.remake_for_skin(name=sprites_active, idx=self.sprite_id)
        elif sprite_inactive and not up and self.last_action == 'up':
            self.sprite_update(name=sprite_inactive, time_update=time_to_update)
            self.remake_for_skin(name=sprite_inactive, idx=self.sprite_id)
        return up

    def motion_down(self, sprites_active=None, sprite_inactive=None, time_to_update=6):
        """
        Метод для движения вниз, можно подключить загруженные спрайты
        :param sprites_active: имя спрайтов движения
        :param sprite_inactive: имя спрайтов дездействия
        :param time_to_update: время до смены спрайта
        :return: int - скорость
        """
        down = pygame.key.get_pressed()[115] * self.speed
        if down:
            self.body.y += down
            self.last_action = 'down'
            if sprites_active:
                self.sprite_update(name=sprites_active, time_update=time_to_update)
                self.remake_for_skin(name=sprites_active, idx=self.sprite_id)
        elif sprite_inactive and not down and self.last_action == 'down':
            self.sprite_update(name=sprite_inactive, time_update=time_to_update)
            self.remake_for_skin(name=sprite_inactive, idx=self.sprite_id)
        return down

    def action_jump(self):
        if self.y == self.body.y and self.drop_speed != 1:
            self.drop_speed = 1
            if pygame.key.get_pressed()[32]:
                self.drop_speed = -self.height_jump
        self.y = self.body.y


class Barrier(Object):
    """
    Класс для создания непроходимых объектов
    """

    def __init__(self, parent: pygame.Surface, objects: list, width=40, height=40, x=0, y=0, color=(255, 255, 255)):
        """
        :param parent: pygame.Surface - родимтельское окно
        :param objects:
        :param width: int
        :param height: int
        :param x: int
        :param y: int
        :param color: tuple - цвет в RGB
        """
        super().__init__(parent, width, height, x, y, color)
        self.objects = objects

    def resistance(self):
        """
        Метод, который отвечает за препятствывание передвижения
        :return: boolean - есть сопротивление или нету
        """
        for obj in self.objects:
            collision = self.body.colliderect(obj.body)
            if collision:
                resist_sides = {
                    'left': abs(self.body.left - obj.body.right),
                    'right': abs(self.body.right - obj.body.left),
                    'top': abs(self.body.top - obj.body.bottom),
                    'bottom': abs(self.body.bottom - obj.body.top)
                }
                min_dip = [key for key, val in resist_sides.items() if val == min(resist_sides.values())]

                if 'left' in min_dip:
                    obj.body.right = self.body.left
                elif 'right' in min_dip:
                    obj.body.left = self.body.right
                elif 'top' in min_dip:
                    obj.body.bottom = self.body.top
                elif 'bottom' in min_dip:
                    obj.body.top = self.body.bottom
                return min_dip
