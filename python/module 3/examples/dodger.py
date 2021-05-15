from first_engine.game import Game
from first_engine.objects import Object
import random


class FirstGame(Game):

    def run(self):
        RED = (255, 200, 200)
        YELLOW = (255, 255, 200)
        GREEN = (200, 255, 200)
        BLUE = (200, 200, 255)

        colors = BLUE, GREEN, YELLOW, RED

        game_over = False

        hero_width, hero_height = 40, 40
        start_position_x = self.body.width // 2 - hero_width // 2
        start_position_y = self.body.height - hero_height

        hero = Object(
            parent=self.surface, speed=4,
            width=hero_width, height=hero_height,
            x=start_position_x, y=start_position_y
        )
        enemies = []

        timer = 60
        while self.RUNNER:
            if not game_over:
                self.fps_counter(60)
                self.window_borders(objects=[hero])
                self.display_update()
                self.window_fill()

                hero.blit()
                hero.motion_control()

                timer -= 1
                if timer == 0:
                    enemy_speed = random.randint(1, 4)
                    enemies.append(Object(
                        parent=self.surface, speed=enemy_speed, color=colors[enemy_speed - 1],
                        x=random.randint(0, self.body.width - hero_width), y=-40
                    ))
                    timer = 60

                for enemy in enemies:
                    enemy.blit()
                    enemy.y += enemy.speed
                    enemy.replace()
                    if enemy.body.colliderect(hero.body):
                        game_over = True
                    if enemy.body.top == self.body.bottom:
                        enemies.remove(enemy)

            for event in self.events():
                # print(event)  # отслеживание событий

                if event.type == 768 and event.key == 114:  # при нажатии на R игра начинается заново
                    hero.replace(x=start_position_x, y=start_position_y)  # обновляем позицию героя
                    enemies.clear()  # отчищаем список врагов
                    game_over = False  # отключаем конец игры

                self.close(event)


FirstGame(width=800, height=800).run()
