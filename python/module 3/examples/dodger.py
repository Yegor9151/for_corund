from first_engine.game import Game
from first_engine.characters import Character
from first_engine.borders import Border
from first_engine.objects import Object
import random


class MyGame(Game):

    def run(self):  # рабочая область

        start_posX = self.w // 2 - 20
        start_posY = self.h - 40
        char = Character(width=40, height=40,
                         x=start_posX, y=start_posY,
                         speed=4)
        enemies = []
        game_over = False
        time_to_spawn = 60

        while True:
            if not game_over:
                self.fps_control()
                self.display_update()
                self.surface.fill((0, 0, 0))

                self.resistance(objs=[char])

                char.blit(self.surface)
                char.motion()

                time_to_spawn -= 1
                if time_to_spawn == 0:
                    enemies.append(Object(x=random.randint(0, self.w - 40), y=-40))
                    time_to_spawn = 60

                for enemy in enemies:
                    enemy.blit(self.surface)
                    enemy.rect.y += 2
                    if enemy.rect.colliderect(char.rect):
                        game_over = True
                    if enemy.rect.top == self.surface.get_rect().bottom:
                        enemies.remove(enemy)

            for event in self.get_events():
                self.close(event)
                if event.type == 768 and event.key == 114:  # R
                    char.rect.x, char.rect.y = start_posX, start_posY
                    enemies.clear()
                    game_over = False


MyGame().run()
