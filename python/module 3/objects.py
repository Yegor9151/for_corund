import pygame


class Object:

    def __init__(self,
                 parentSurface: pygame.Surface = None,
                 img_file=None,
                 position: list = (0, 0),
                 size: tuple = (40, 40),
                 color: tuple = (150, 150, 150)):

        self.parentSurface = parentSurface  # родительское окно

        # СКИН ПЕРСОНАЖА
        if img_file:
            self.bodySurface = pygame.image.load(img_file)  # создание пересонажа
            self.bodySurface.set_colorkey((255, 255, 255))
        else:
            self.bodySurface = pygame.Surface(size)  # создание пересонажа
            self.bodySurface.fill(color)  # заполнение персонажа

        self.bodyRect = self.bodySurface.get_rect(topleft=position)

    def place(self) -> pygame.Rect:
        """
        Метод для отрисовки на родитеском окне
        output: Rect родитеского окна
        """
        self.parentSurface.blit(self.bodySurface, self.bodyRect)
        return self.bodyRect
