import pygame
import sys
import random

import characters
from interface import HealthBar
from objects import Object

"""
Это главный модуль в котором конструируется вся игра

В данном модуле происходит: 
    Создание родительского окна
    Создание персонажа
    Запуск игрового цикла
    Отрисовываются объектов
"""

# цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH = 1600  # ширина родительского окна
HEIGHT = 800  # высота родительского окна

FPS = 60  # кадры в секунду

BG = pygame.image.load('./location/forest.jpg')
HERO_SKIN = './characters/mage_right.png'
ENEMY = './characters/mon.png', './characters/enemy_right.png'

# ОСНОВНЫЕ ОБЪЕКТЫ
parentSurface = pygame.display.set_mode((WIDTH, HEIGHT))  # родительское окно
parentRect = parentSurface.get_rect()
clock = pygame.time.Clock()  # четчик FPS

# ДОПОЛНИТЕЛЬНЫЕ СОБЫТИЯ
pygame.time.set_timer(pygame.USEREVENT, 2000)

# ФИЗИЧЕСКИЕ ОБЪЕКТЫ

# ПЕРСОНАЖИ
hero = characters.Player(parentSurface,
                         img_file=HERO_SKIN,
                         position=[WIDTH // 2, HEIGHT // 2],
                         speed=2, health=100, damage=10)  # главный герой

enemyList = []


def spawn_enemy():
    if event.type == 32774 and len(enemyList) < 5:  # событие произходящее каждые 5 секунд
        enemyList.append(
            characters.Enemy(parentSurface,
                             img_file=random.choice(ENEMY),
                             position=[random.randint(0, WIDTH), random.randint(0, HEIGHT)],
                             speed=1, health=50, damage=5)
        )  # добавление в список врагов


# ИНТЕРФЕЙС
health_bar = HealthBar(parentSurface, hero, xy=(50, 750))


# ОСНОВНЫЕ ФУНКЦИИ
def quit_game():
    """
    Функция для выхода из игры
    256 - нажание на X
    768, 27 - нажатие на кнопку ESC
    """
    if event.type == 256 or (event.type == 768 and event.key == 27):
        pygame.quit()  # деинициализация модулей pygame
        sys.exit()  # выход из интерпритатора python


def motion():
    """
    Функция активации и деактивации напраления перемещения персонажа
    :returns event.type, event.key: тип события и нажатие кнопки направления
    """
    if event.type == 768:  # нажатие на кнопку
        if event.key == 97:
            hero.LEFT = True
        if event.key == 100:
            hero.RIGHT = True
        if event.key == 119:
            hero.UP = True
        if event.key == 115:
            hero.DOWN = True

        return event.type, event.key

    elif event.type == 769:  # отжатие кнопки
        if event.key == 97:
            hero.LEFT = False
        if event.key == 100:
            hero.RIGHT = False
        if event.key == 119:
            hero.UP = False
        if event.key == 115:
            hero.DOWN = False

        return event.type, event.key


# СТРЕЛЬБА
projList = []


def fire():
    if event.type == 1025:
        projectile = hero.attack(event.pos)
        projList.append(projectile)


# ВЗАИМОДЕЙСТВИЯ
def window_barrier():
    if hero.bodyRect.bottom >= HEIGHT:
        hero.bodyRect.bottom = HEIGHT
    elif hero.bodyRect.top <= 0:
        hero.bodyRect.top = 0
    if hero.bodyRect.right >= WIDTH:
        hero.bodyRect.right = WIDTH
    elif hero.bodyRect.left <= 0:
        hero.bodyRect.left = 0


def damage_hero():
    if en.bodyRect.colliderect(hero.bodyRect):
        hero.health -= en.damage
        hero.bodyRect.center = (WIDTH // 2, HEIGHT // 2)


def damage_enemy():
    for enemy in enemyList:
        if enemy.bodyRect.collidepoint(proj.position):
            enemy.health -= hero.damage
            try:
                projList.remove(proj)
                if enemy.health <= 0:
                    enemyList.remove(enemy)
            except ValueError as err:
                print(err)


blocks = [Object(parentSurface, position=[0, HEIGHT-150], size=(WIDTH, 150))]

characterList = None


def block_place():
    for obj in characterList:
        obj.bodyRect.bottom += 2
        for block in blocks:
            # block.place()
            if block.bodyRect.colliderect(obj.bodyRect):
                obj.bodyRect.bottom = block.bodyRect.top


while True:
    for event in pygame.event.get():
        # print(event)  # отслеживание событий
        quit_game()  # выход из игры
        motion()  # комманды для перемещения персонажа
        fire()  # принажатии на моус 1 происходит выстрел
        spawn_enemy()

    # РОДИТЕЛЬСКОЕ ОКНО
    clock.tick(FPS)  # частота обновления кадров
    pygame.display.update()  # обносление кадров
    parentSurface.blit(BG, (0, 0))  # заливка родительского окна

    # ПЕРСОНАЖИ
    # Герой
    hero.place()  # отрисовка персонажа
    hero.move()  # перемещение персонажа

    # Враги
    for en in enemyList:
        en.place()
        damage_hero()

    characterList = enemyList + [hero]

    # # ОБЪЕКТЫ
    block_place()

    for proj in projList:
        if parentRect.collidepoint(proj.position):
            proj.place()
            proj.fly()
            damage_enemy()
        else:
            projList.remove(proj)

    # ИНТЕРФЕЙС
    health_bar.place()

    # ВЗАИМОДЕЙСТВИЯ
    window_barrier()
