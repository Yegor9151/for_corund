import pygame


class Object:

    def __init__(self, parent: pygame.Surface,
                 width=40, height=40, x=0, y=0,
                 color=(255, 255, 255),
                 speed=1):
        self.parent = parent
        self.x = x
        self.y = y
        self.color = color

        self.speed = speed

        self.skin = pygame.Surface(size=(width, height))
        self.skin.fill(color=color)
        self.body = self.skin.get_rect(topleft=(x, y))

    def blit(self):
        return self.parent.blit(source=self.skin, dest=self.body)

    def recolor(self, color):
        self.skin.fill(color=color)
        return color

    def __diagonal_speed(self):
        speed_xy = (self.speed ** 2 + self.speed ** 2) ** (1 / 2)  # находим длину вектора x + y по пифагору
        speed_xy = self.speed / speed_xy  # находим долю скорости от суммы векторов
        speed_xy *= self.speed  # теперь находим скорость по диагонали
        return speed_xy

    def motion(self):
        self.body.x, self.body.y = self.x, self.y

    def motion_control(self):
        left = pygame.key.get_pressed()[97]
        right = pygame.key.get_pressed()[100]
        up = pygame.key.get_pressed()[115]
        down = pygame.key.get_pressed()[119]

        speed = self.__diagonal_speed() if (left + right + up + down) > 1 else self.speed

        self.x -= left * (speed - 1)
        self.x += right * speed
        self.y += up * speed
        self.y -= down * (speed - 1)

        self.motion()
        return speed

    def change_speed(self, speed):
        self.speed = speed
        return speed
