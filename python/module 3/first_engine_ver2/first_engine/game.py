import pygame


class Game:
    """
    Класс для создания игр нра его основек

    :param cycle: включить выключить цикл
    :param bg: хранит задний фон, для загрузки использовать load_bg()
    """

    cycle = True
    bg = None  # задник

    def __init__(self, size=(600, 400)):
        """
        Конструктор для инициализации игры
        :param size: размер окна, помещается в свойства w и h
        :param w: ширина
        :param h: высота
        :param surface: окно игры
        """
        self.w, self.h = size
        self.surface = pygame.display.set_mode(size)
        self.__clock = pygame.time.Clock()

    def load_bg(self, path_to_bg):
        """
        Загрузка задника игры
        :param path_to_bg: путь до задника
        :return: загруженный задник
        """
        self.bg = pygame.image.load(path_to_bg)
        return self.bg

    @staticmethod
    def get_events():
        """
        перебор событий
        :return: события
        """
        return pygame.event.get()

    @staticmethod
    def display_update() -> None:
        """
        Перересовывает экран
        :return: None
        """
        pygame.display.update()

    def close(self, event):
        """
        Закрывает окно игры
        :param event: события
        :return: None
        """
        if event.type == 256 or (event.type == 768 and event.key == 27):
            pygame.quit()
            self.cycle = False
            raise SystemExit

    def fps_control(self, frames=60):
        """
        Управляет FPS - частотой обновления кадров в секунду
        :param frames: число кадров в секунду
        :return: None
        """
        self.__clock.tick(frames)

    def resistance(self, objs: list):
        """
        Препятствует выходу объектов за экран
        :param objs: список объектов, которые не смогут выйти за экран
        :return: None
        """
        for obj in objs:
            if obj.rect.x < 0:
                obj.rect.x = 0
            if obj.rect.y < 0:
                obj.rect.y = 0
            if obj.rect.right > self.w:
                obj.rect.right = self.w
            if obj.rect.bottom > self.h:
                obj.rect.bottom = self.h
