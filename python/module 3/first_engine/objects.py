import pygame
import os


class Object:
    sprites = {}
    last_action = 'right'
    time_to_sprite_update = 6
    sprite_id = 0

    def __init__(self, parent: pygame.Surface, width=40, height=40, x=0, y=0, color=(255, 255, 255)):
        self.parent = parent
        self.x, self.y = x, y
        self.color = color

        self.skin = pygame.Surface(size=(width, height))
        self.skin.fill(color=color)
        self.body = self.skin.get_rect(topleft=(x, y))

    def load_sprites(self, name: str, path: str):
        """
        Метод для загрузки скинов и созданния тел
        :param name: str - имя под которым будем хранить загруженные скины и созданные тела
        :param path: str - путь до папки с файлами
        :return skin_body: dict - возвращаем только что загруженные скины и созданные тела
        """
        path = path if path[-1] == '/' else path + '/'

        skin = [pygame.image.load(path + i) for i in os.listdir(path)]
        self.sprites[name] = skin
        return skin

    def remake_for_skin(self, name, idx=0):
        self.skin = self.sprites[name][idx]
        self.body = self.skin.get_rect(topleft=(self.x, self.y))

    def sprite_update(self, name, time_update=6):
        """
        Метод обновляющий спрайты по очереди
        :param name: str - принимает имя спрайтов похраненных в словарь sprites
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

    def blit(self):
        self.parent.blit(source=self.skin, dest=self.body)
        return self.parent

    def recolor(self, color):
        self.skin.fill(color=color)
        return color

    def replace(self, x=None, y=None):
        if x:
            self.x = x
        if y:
            self.y = y
        self.body.x = round(self.x) if round(self.x) > 0 else 1
        self.body.y = round(self.y) if round(self.y) > 0 else 1
        return self.body.x, self.body.y


class Character(Object):
    def __init__(self, parent: pygame.Surface, width=40, height=40, x=0, y=0, color=(255, 255, 255), speed=1):
        super().__init__(parent, width, height, x, y, color)
        self.speed = speed

    def __diagonal_speed(self):
        speed_xy = (self.speed ** 2 + self.speed ** 2) ** (1 / 2)  # находим длину вектора x + y по пифагору
        speed_xy = self.speed / speed_xy  # находим долю скорости от суммы векторов
        speed_xy *= self.speed  # теперь находим скорость по диагонали
        return speed_xy

    def __motion_control(self):
        left = pygame.key.get_pressed()[97]
        right = pygame.key.get_pressed()[100]
        up = pygame.key.get_pressed()[119]
        down = pygame.key.get_pressed()[115]

        speed = self.__diagonal_speed() if (left + right + up + down) > 1 else self.speed
        sides = {'left': -left * speed, 'right': right * speed,
                 'up': -up * speed, 'down': down * speed}
        return sides

    def motion_left(self, sprites_active=None, sprite_inactive=None, time_to_update=6):
        left = self.__motion_control()['left']
        if left:
            self.x += left
            self.replace()
            self.last_action = 'left'
            if sprites_active:
                self.sprite_update(name=sprites_active, time_update=time_to_update)
                self.remake_for_skin(name=sprites_active, idx=self.sprite_id)
        elif sprite_inactive and not left and self.last_action == 'left':
            self.sprite_update(name=sprite_inactive, time_update=time_to_update)
            self.remake_for_skin(name=sprite_inactive, idx=self.sprite_id)
        return left

    def motion_right(self, sprites_active=None, sprite_inactive=None, time_to_update=6):
        right = self.__motion_control()['right']
        if right:
            self.x += right
            self.replace()
            self.last_action = 'right'
            if sprites_active:
                self.sprite_update(name=sprites_active, time_update=time_to_update)
                self.remake_for_skin(name=sprites_active, idx=self.sprite_id)
        elif sprite_inactive and not right and self.last_action == 'right':
            self.sprite_update(name=sprite_inactive, time_update=time_to_update)
            self.remake_for_skin(name=sprite_inactive, idx=self.sprite_id)
        return right

    def motion_up(self, sprites_active=None, sprite_inactive=None, time_to_update=6):
        up = self.__motion_control()['up']
        if up:
            self.y += up
            self.replace()
            self.last_action = 'up'
            if sprites_active:
                self.sprite_update(name=sprites_active, time_update=time_to_update)
                self.remake_for_skin(name=sprites_active, idx=self.sprite_id)
        elif sprite_inactive and not up and self.last_action == 'up':
            self.sprite_update(name=sprite_inactive, time_update=time_to_update)
            self.remake_for_skin(name=sprite_inactive, idx=self.sprite_id)
        return up

    def motion_down(self, sprites_active=None, sprite_inactive=None, time_to_update=6):
        down = self.__motion_control()['down']
        if down:
            self.y += down
            self.replace()
            self.last_action = 'down'
            if sprites_active:
                self.sprite_update(name=sprites_active, time_update=time_to_update)
                self.remake_for_skin(name=sprites_active, idx=self.sprite_id)
        elif sprite_inactive and not down and self.last_action == 'down':
            self.sprite_update(name=sprite_inactive, time_update=time_to_update)
            self.remake_for_skin(name=sprite_inactive, idx=self.sprite_id)
        return down

    def change_speed(self, speed):
        self.speed = speed
        return speed


class Barrier(Object):
    def __init__(self, parent: pygame.Surface, objects: list, width=40, height=40, x=0, y=0, color=(255, 255, 255)):
        super().__init__(parent, width, height, x, y, color)
        self.objects = objects

    def resistance(self):
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

                return collision
        return 0
