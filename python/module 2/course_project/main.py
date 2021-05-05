from scr import read_file  # импортируем фуекцию для чтения токена
from bot import Bot  # импортируем класс-конструктор бота
from pprint import pprint


class BotLiker:
    __GROUP_ID = 44273004  # корунд
    __token = read_file('F:token.txt')

    def run(self):
        bot = Bot(
            owner_id=self.__GROUP_ID,
            token=self.__token
        )  # Создаем бота через наш конструктор

        url = bot.create_url(count=2)  # бот - создай ссылку
        data = bot.get_data()  # бот - достань данные
        count = bot.add_likes()  # бот - поставь лайки

        print(f'\nБыло поставлено {count} лайков')
        print(f'\nСсылка до постов:\n{url}')
        print(f'\nСостояние данных:\n{data}')


BotLiker().run()
