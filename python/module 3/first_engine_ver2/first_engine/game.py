import pygame


class Game:

    def __init__(self, size=(600, 400)):
        self.w, self.h = size
        self.surface = pygame.display.set_mode(size)
        self.__clock = pygame.time.Clock()

    @staticmethod
    def get_events():
        return pygame.event.get()

    @staticmethod
    def display_update():
        pygame.display.update()

    @staticmethod
    def close(event):
        if event.type == 256 or (event.type == 768 and event.key == 27):
            raise SystemExit

    def fps_control(self, frames=60):
        self.__clock.tick(frames)
        
    def resistance(self, objs: list):
        for obj in objs:
            if obj.rect.x < 0:
                obj.rect.x = 0
            if obj.rect.y < 0:
                obj.rect.y = 0
            if obj.rect.right > self.w:
                obj.rect.right = self.w
            if obj.rect.bottom > self.h:
                obj.rect.bottom = self.h
