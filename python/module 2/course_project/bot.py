from pprint import pprint
import requests


class Bot:
    base_url = 'https://api.vk.com/method/'
    methods = {'wall_get': 'wall.get?',
               'likes_add': 'likes.add?'}

    full_url = None  # заполнится поле create_url
    data_list = []  # здесь храним информацию о постах

    def __init__(self, owner_id, token):
        self.base_params = f'owner_id=-{owner_id}&' \
                           f'access_token={token}&' \
                           f'v=5.21&'

    def create_url(self, count=1, offset=0):
        self.full_url = self.base_url + \
                        self.methods['wall_get'] + \
                        self.base_params + \
                        f'count={count}&' \
                        f'offset={offset}&'
        return self.full_url

    def get_data(self):
        data = requests.get(self.full_url)
        data = data.json()
        try:
            data = data['response']['items']
            for post in data:
                data_dict = {'text': post['text'],
                             'id': post['id'],
                             'like': post['likes']['user_likes']}
                self.data_list.append(data_dict)
            return self.data_list
        except KeyError:
            return data['error']['error_msg']

    def add_likes(self):
        count = 0  # счетчик лайков

        for post in self.data_list:
            if post['like']:
                print(f"Для {post['id']} лайк уже был поставлен")
            else:
                url = self.base_url + \
                      self.methods['likes_add'] + \
                      self.base_params + \
                      f"type=post&" \
                      f"item_id={post['id']}&"

                requests.get(url)
                print(f'{post["id"]} - лайк поставлен')
                count += 1

        return count
