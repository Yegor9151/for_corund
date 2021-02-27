import random
import time


class Hero:

    def __init__(self, name, place, weapon):
        self.name = name
        self.place = place
        self.max_HP = 100
        self.HP = self.max_HP
        self.weapon = weapon

    @staticmethod
    def chose():
        return int(input('Дейсевие: '))

    def move(self, replace):
        self.place = replace

    def attack(self, target_HP):
        DMG = random.choice(self.weapon.dmg)
        target_HP -= DMG

        return target_HP, DMG

    def rest(self):
        while True:
            print(f'Здоровье: {self.HP}')
            time.sleep(0.5)
            if self.HP < self.max_HP:
                self.HP += 1
            else:
                break
