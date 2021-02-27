import random


class Enemy:

    def __init__(self, name, HP, DMG):
        self.name = name
        self.HP = HP
        self.DMG = DMG

    def attack(self, target_HP):
        DMG = random.choice(self.DMG)
        target_HP -= DMG
        return target_HP, DMG
