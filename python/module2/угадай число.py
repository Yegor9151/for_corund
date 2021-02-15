from random import randint

# print('Загадайте число от 1 до 100')
# input('Для продолжения нажмите "Enter"')

MIN, MAX = 1, 100
ATTEMPTS = 0

true = randint(1, 100)

while True:
    ATTEMPTS += 1
    print(MIN, MAX)

    # predict = randint(MIN, MAX)
    predict = int(MIN + ((MAX - MIN + 1) / 2))
    # print(
    #     f'''Вы загадали число {predict}?
    #     1. Да
    #     2. Нет, меньше
    #     3. Нет, больше''')

    if true == predict:
        print(f'{true} = {predict}')
        print(f'Ура, я угадал с {ATTEMPTS} попытки!')
        break
    elif true < predict:
        print(f'{true} < {predict}')
        MAX = predict - 1
    elif true > predict:
        print(f'{true} > {predict}')
        MIN = predict + 1

    # answer = int(input())
    # if answer == 1:
    #     print(f'Ура, я угадал с {ATTEMPTS} попытки!')
    #     break
    # elif answer == 2:
    #     MAX = predict - 1
    # elif answer == 3:
    #     MIN = predict + 1
