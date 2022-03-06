"""
Главный модуль - тут происходит все действие
"""

# Для получения ссылки на токен раскомментировать и вставить id приложения
# from utils import generate_token
# MY_APP_ID = 1234567  # id моего приложения в вк (нужна авторизация)
# url_to_token = generate_token(client_id=MY_APP_ID)
# print(url_to_token)

from utils import read_token
from bot import VkBot
from time import sleep
from pprint import pprint


def run(path, owner_id, posts=5):

    print(path, owner_id, posts)

    mybot = VkBot()  # создаем экземпляр бота

    mytoken = read_token(path=path)  # вытаскиваем наш токен
    mybot.user_settings(
        access_token=mytoken,
        owner_id=owner_id
    )  # сохраняем настройки пользователя

    wall_url = mybot.url_to_wall(posts=posts)  # собираем и сохраняем ссылку на стену
    post_list = mybot.parse_wall(url=wall_url)  # собираем данные с постов
    for post in post_list:
        if post["like"] == 0:  # если лайк есть
            like_url = mybot.url_to_like(post_id=post["id"])  # собираем ссылку для постановки лайка
            req = mybot.like_add(url=like_url)  # ставим лайк сохраняем ответ

            print(post["text"])
            print(req)

            sleep(0.5)
