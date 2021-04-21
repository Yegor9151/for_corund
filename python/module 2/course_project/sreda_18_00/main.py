"""
Структура проекта:
    main.py, bot.py, scr.py
"""

from sreda_18_00.scr import read_file
from sreda_18_00.bot import Bot


class BotLiker:

    __GROUP_ID = 44273004  # корунд
    __token = read_file('F:token.txt')

    full_url = f'https://api.vk.com/method/wall.get?' \
               f'owner_id=-44273004&' \
               f'access_token={__token}&' \
               f'v=5.21&' \
               f'count=1&' \
               f'offset=0&'
    print(full_url)

    def run(self):
        pass


BotLiker().run()
