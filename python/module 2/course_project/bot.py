from pprint import pprint
import requests


class Bot:
    __base_url = 'https://api.vk.com/method/'
    __methods = {'wall_get': 'wall.get?',
                 'likes_add': 'likes.add?'}

    __full_url = None  # заполнится поле create_url
    __data_list = []  # здесь храним информацию о постах

    def __init__(self, group_id, token):
        self.__base_params = f'owner_id=-{group_id}&' \
                             f'access_token={token}&' \
                             f'v=5.21&'

    def create_url(self, count=1, offset=0):
        self.__full_url = self.__base_url + \
                          self.__methods['wall_get'] + \
                          self.__base_params + \
                          f'count={count}&' \
                          f'offset={offset}&'
        return self.__full_url

    def get_data(self):
        data = requests.get(self.__full_url)
        data = data.json()
        try:
            data = data['response']['items']
            for post in data:
                data_dict = {'text': post['text'],
                             'id': post['id'],
                             'like': post['likes']['user_likes']}
                self.__data_list.append(data_dict)
            return self.__data_list
        except KeyError:
            return data['error']['error_msg']

    def add_likes(self):
        count = 0  # счетчик лайков

        for post in self.__data_list:
            if post['like']:
                print(f"Для {post['id']} лайк уже был поставлен")
            else:
                url = self.__base_url + \
                      self.__methods['likes_add'] + \
                      self.__base_params + \
                      f"type=post&" \
                      f"item_id={post['id']}&"

                requests.get(url)
                print(f'{post["id"]} - лайк поставлен')
                count += 1
        return count
