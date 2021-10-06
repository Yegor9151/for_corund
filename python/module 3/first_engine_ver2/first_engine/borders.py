from .objects import Object
import pygame


class Border(Object):

    def __init__(self, width=40, height=40, color=(255, 255, 255), x=10, y=10):
        super().__init__(width, height, color, x, y)

    def resistance(self, objs: list) -> list[str]:
        for obj in objs:
            if self.rect.colliderect(obj.rect):
                resist_sides = {
                    'left': abs(self.rect.left - obj.rect.right),
                    'right': abs(self.rect.right - obj.rect.left),
                    'top': abs(self.rect.top - obj.rect.bottom),
                    'bottom': abs(self.rect.bottom - obj.rect.top)
                }

                min_deep = [key for key, val in resist_sides.items() if val == min(resist_sides.values())]

                if 'left' in min_deep:
                    obj.rect.right = self.rect.left
                if 'right' in min_deep:
                    obj.rect.left = self.rect.right
                if 'top' in min_deep:
                    obj.rect.bottom = self.rect.top
                if 'bottom' in min_deep:
                    obj.rect.top = self.rect.bottom

                return min_deep

