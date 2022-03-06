"""
В этом модуле проектируем класс бота
"""
import requests


class VkBot:
    # Свойства
    __BASE_URL = "https://api.vk.com/method/"

    # Методы
    def __init__(self, v: float = 5.81):
        # Конструктор
        self.v = v

    def user_settings(self, access_token: str, owner_id: int):
        self.access_token = access_token
        self.owner_id = owner_id

    def url_to_wall(self, posts=1, offset=0):
        """
        Создает ссылку до постов со стены
        example:
        URL = f"https://api.vk.com/method/wall.get?" \
              f"access_token={TOKEN}&" \
              f"v=5.81&" \
              f"owner_id=44273004&" \
              f"count=100&" \
              f"offset=0&"
        :param offset: сколько постов пропустить
        :param posts: число постов
        Доступные методы сохраняются зараннее в свойстве класса methods
        :return: url
        """
        url = f"{self.__BASE_URL}wall.get?" \
              f"v={self.v}&" \
              f"access_token={self.access_token}&" \
              f"owner_id={self.owner_id}&" \
              f"count={posts}&" \
              f"offset={offset}&"
        return url

    def parse_wall(self, url):
        """
        Собирает данные с постов
        :param url: ссылка до постов
        :return: словарь {id, text, like}
        """
        req = requests.get(url)  # response 200
        req = req.json()  # большой словарь со ВСЕМИ данными

        posts = []
        items = req["response"]["items"]
        for item in items:
            idx = item["id"]
            text = item["text"]
            user_likes = item["likes"]["user_likes"]

            post_info = {"id": idx,
                         "text": text,
                         "like": user_likes}

            posts.append(post_info)

        return posts

    def url_to_like(self, post_id):
        """
        Собирает команда серверу на постановку лайка под постом
        :param post_id: идентификатор поста
        :return: ссылка для отправки команды
        """
        url = f"{self.__BASE_URL}likes.add?" \
              f"v={self.v}&" \
              f"access_token={self.access_token}&" \
              f"owner_id={self.owner_id}&" \
              f"type=post&" \
              f"item_id={post_id}"

        return url

    def like_add(self, url):
        req = requests.get(url)  # response 200
        req = req.json()  # большой словарь со ВСЕМИ данными
        return req
