from scr import read_file  # импортируем фуекцию для чтения токена
from bot import Bot  # импортируем класс-конструктор бота
from pprint import pprint


class BotLiker(Bot):  # делаем нашего бота наследником класса Bot
    def __init__(self, group_id, path_to_token):  # метод конструктор
        # обращаемся к методу конструктору родительского класса
        super().__init__(group_id, token=read_file(path_to_token))

    def run(self, count=1):
        likes = 0  # считаем число лайков
        # запускаем цикл в условии которого стоит число пакетов от заявленного числа постов
        for offset in (range(count // 100) if count % 100 == 0 else range((count // 100) + 1)):
            url = self.create_url(count=count, offset=offset * 100)  # бот - создай ссылку
            data = self.get_data()  # бот - достань данные
            likes += self.add_likes()  # бот - поставь лайки

            # эта часть для разработчика
            print(f'\nСсылка до постов:\n{url}')
            if type(data) == str:
                print(f'\nПроизошла ошибка:\n{data}')
            else:
                print(f'\nСостояние данных:\n')
                pprint(data)

        return likes  # возвращаем число лайков
