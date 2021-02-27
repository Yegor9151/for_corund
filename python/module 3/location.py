class Location:

    def __init__(self, name):
        self.name = name

    def events(self, hero, another_loc):

        while True:
            print(
                f'Место положение: {self.name}\n'
                f'Здоровье: {hero.HP}\n'
                f'Оружие: {hero.weapon.name}\n '
                f'\tурон: {hero.weapon.dmg[0]} - {hero.weapon.dmg[1]}\n'
            )
            print(
                f'\t1. Переход в {another_loc[0]}\n'
                f'\t2. Отдыхать\n'
            )
            act = hero.chose()

            if act == 1:  # переход
                hero.move(replace=another_loc[0])
                break
            elif act == 2:  # отдых
                hero.rest()
                print()
                break


class DangerousLocation:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def battle(hero, enemy):

        while True:
            print(
                f'{enemy.name}\n'
                f'\tЗдоровье {enemy.HP}\n'
                f'\tУрон {enemy.DMG[0]} - {enemy.DMG[1]}\n'
            )
            print(
                f'\t1. Отступление\n'
                f'\t2. Атака\n'
            )
            act = hero.chose()

            if act == 1:  # отступление
                hero.HP, DMG = enemy.attack(target_HP=hero.HP)
                print(
                    f'Вы получили урон, {DMG}\n'
                    f'Ваше здоровье: {hero.HP}\n'
                )
                break
            elif act == 2:  # атака

                enemy.HP, DMG = hero.attack(target_HP=enemy.HP)
                print(f'Вы нанесли урон, {DMG}')
                if enemy.HP <= 0:
                    print(f'{enemy.name} подежден!')
                    break
                print(f'{enemy.name} здоровье: {enemy.HP}')

                hero.HP, DMG = enemy.attack(target_HP=hero.HP)
                print(
                    f'Вы получили урон, {DMG}\n'
                    f'Ваше здоровье: {hero.HP}\n'
                )

    def events(self, hero, enemies, another_loc):

        while True:  # все события
            print(
                f'Место положение: {self.name}\n'
                f'Здоровье: {hero.HP}\n'
                f'Оружие: {hero.weapon.name}\n '
                f'\tурон: {hero.weapon.dmg[0]} - {hero.weapon.dmg[1]}\n'
            )
            print(
                f'\t1. Переход в {another_loc[0]}\n'
                f'\t2. Отдыхать\n'
                f'\t3. Вступить в бой {enemies[0].name}\n'
                f'\t4. Вступить в бой {enemies[1].name}\n'
            )
            act = hero.chose()

            if act == 1:  # переход
                hero.move(replace=another_loc[0])
                break
            elif act == 2:  # отдых
                hero.rest()
                print()
                break
            elif act == 3 or 4:  # бой

                enemy = None
                if act == 3:
                    enemy = enemies[0]
                elif act == 4:
                    enemy = enemies[1]

                self.battle(hero=hero, enemy=enemy)
