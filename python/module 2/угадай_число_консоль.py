from random import randint

print('Загадайте число от 1 до 100')
input('Для продолжения нажмите "Enter"')

MIN, MAX = 1, 100

print('''Машина запоминает Ваши ответы, но по мимо этого у нее есть 2 метода угадывания числа.
Выберите алгоритм по которому машина будет угадывать Ваше число:
1. Рандомное угадывание
2. Логарифмический алгоритм''')
answer_alg = int(input())


def random_prediction():
    return randint(MIN, MAX)


def log_prediction():
    return int(MIN + ((MAX - MIN + 1) / 2))


algorithm = None

if answer_alg == 1:
    algorithm = random_prediction
    print('рандомное угадывание')
elif answer_alg == 2:
    algorithm = log_prediction
    print('логарифмический алгоритм')

ATTEMPTS = 0

# true = randint(1, 100)

while True:
    ATTEMPTS += 1
    print(MIN, MAX)

    predict = algorithm()
    print(
        f'''Вы загадали число {predict}?
        1. Да
        2. Нет, меньше
        3. Нет, больше''')

    # if true == predict:
    #     print(f'{true} = {predict}')
    #     print(f'Ура, я угадал с {ATTEMPTS} попытки!')
    #     break
    # elif true < predict:
    #     print(f'{true} < {predict}')
    #     MAX = predict - 1
    # elif true > predict:
    #     print(f'{true} > {predict}')
    #     MIN = predict + 1

    answer = int(input())
    if answer == 1:
        print(f'Ура, я угадал с {ATTEMPTS} попытки!')
        break
    elif answer == 2:
        MAX = predict - 1
    elif answer == 3:
        MIN = predict + 1
