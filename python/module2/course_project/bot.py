import requests
from pprint import pprint


class Bot:
    base_url = 'https://api.vk.com/method/'
    methods = {'get_wall': 'wall.get?',
               'like': 'likes.add?'}
    full_url = None
    data = []

    def __init__(self, owner_id, token):
        self.owner_id = owner_id
        self.token = token
        self.base_params = f'owner_id=-{self.owner_id}&' \
                           f'access_token={self.token}&' \
                           f'v=5.21&'

    def create_url(self, count=1, offset=0):
        params = self.base_params + \
                 f'count={count}&' \
                 f'offset={offset}'

        self.full_url = self.base_url + self.methods['get_wall'] + params

        return self.full_url

    def get_data(self):
        """ Собирает данный об объекте:
        input: url to object
        output: id, поставил ли пользователь лайк, text """

        response = requests.get(self.full_url)
        json_obj = response.json()

        items_list = json_obj['response']['items']
        for item in items_list:
            data = {'id': item['id'],
                    'like': item['likes']['user_likes'],
                    'text': item['text']}

            self.data.append(data)

        return self.data

    def like(self):
        likes = 0
        for i in self.data:
            if i['like']:
                pprint(i)
                print('Уже было отмечено')
            else:
                params = self.base_params + \
                         f'item_id={i["id"]}&' \
                         f'type=post'
                like = self.base_url + self.methods['like'] + params
                requests.get(like)

                pprint(i)
                print('Лайк поставлен')
                likes += 1

        return likes
