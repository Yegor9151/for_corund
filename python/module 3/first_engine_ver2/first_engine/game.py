import pygame


class Game:
    cycle = True
    bg = None  # задник

    def __init__(self, size=(600, 400)):
        self.w, self.h = size
        self.surface = pygame.display.set_mode(size)
        self.__clock = pygame.time.Clock()

    def load_bg(self, path_to_bg):
        """Сохраняет задник"""
        self.bg = pygame.image.load(path_to_bg)
        return self.bg

    @staticmethod
    def get_events():
        return pygame.event.get()

    @staticmethod
    def display_update():
        pygame.display.update()

    def close(self, event):
        if event.type == 256 or (event.type == 768 and event.key == 27):
            pygame.quit()
            self.cycle = False
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
