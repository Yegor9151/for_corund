import pygame


class Object:
    def __init__(self, parent: pygame.Surface, width=40, height=40, x=0, y=0, color=(255, 255, 255)):
        self.parent = parent
        self.x, self.y = x, y
        self.color = color

        self.skin = pygame.Surface(size=(width, height))
        self.skin.fill(color=color)
        self.body = self.skin.get_rect(topleft=(x, y))

    def blit(self):
        return self.parent.blit(source=self.skin, dest=self.body)

    def recolor(self, color):
        self.skin.fill(color=color)
        return color

    def replace(self, x=None, y=None):
        if x:
            self.x = x
        if y:
            self.y = y
        self.body.x = self.x
        self.body.y = self.y


class Character(Object):
    def __init__(self, parent: pygame.Surface, width=40, height=40, x=0, y=0, color=(255, 255, 255), speed=1):
        super().__init__(parent, width, height, x, y, color)
        self.speed = speed

    def __diagonal_speed(self):
        speed_xy = (self.speed ** 2 + self.speed ** 2) ** (1 / 2)  # находим длину вектора x + y по пифагору
        speed_xy = self.speed / speed_xy  # находим долю скорости от суммы векторов
        speed_xy *= self.speed  # теперь находим скорость по диагонали
        return speed_xy

    def motion_control(self):
        left = pygame.key.get_pressed()[97]
        right = pygame.key.get_pressed()[100]
        up = pygame.key.get_pressed()[119]
        down = pygame.key.get_pressed()[115]

        speed = self.__diagonal_speed() if (left + right + up + down) > 1 else self.speed

        self.x -= left * speed
        self.x += right * (speed + 1) if speed % 1 != 0 else right * speed
        self.y -= up * speed
        self.y += down * (speed + 1) if speed % 1 != 0 else down * speed

        self.replace()
        return -left * speed, right * speed, -up * speed, down * speed

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
