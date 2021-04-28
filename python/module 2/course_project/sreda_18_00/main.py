"""
Структура проекта:
    main.py, bot.py, scr.py
"""

from sreda_18_00.scr import read_file  # импортируем фуекцию для чтения токена
from sreda_18_00.bot import Bot  # импортируем класс-конструктор бота
import requests
from pprint import pprint

class BotLiker:
    __GROUP_ID = 44273004  # корунд
    __token = read_file('F:token.txt')

    def run(self):

        bot = Bot(
            owner_id=self.__GROUP_ID,
            token=self.__token
        )  # Создаем бота через наш конструктор

        bot.create_url() # бот - создай ссылку
        print(bot.full_url)

        data = requests.get(bot.full_url)
        data = data.json()
        pprint(data)
        """
        из data вытащить:
            - text
            - id
            - user_likes
        """



BotLiker().run()
