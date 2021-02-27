from location import *
from hero import Hero
from enemy import Enemy
from weapon import Weapon

# ЛОКАЦИИ
town = Location(name='Васянск')
forest = DangerousLocation(name='Лес')

# ОРУЖИЕ
fist = Weapon()

# МОБЫ
orc_to_hit = Enemy(name='Орк для битья', HP=10, DMG=[2, 4])
rat_men = Enemy(name='Крысолюд', HP=5, DMG=[1, 2])

# ГЕРОЙ
hero = Hero(name=input('Введите имя героя: '), place=town.name, weapon=fist)

while True:
    if hero.place == town.name:
        town.events(hero=hero, another_loc=[forest.name])
    if hero.place == forest.name:
        forest.events(hero=hero, enemies=[orc_to_hit, rat_men], another_loc=[town.name])
