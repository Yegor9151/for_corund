from pprint import pprint
import requests


class Bot:
    base_url = 'https://api.vk.com/method/'
    methods = {'wall': 'wall.get?',
               'like': 'likes.add?'}

    full_url = None
    url_to_like = None

    data_list = []

    def __init__(self, owner_id, token):
        self.owner_id = owner_id
        self.token = token
        self.base_params = f'owner_id=-{self.owner_id}&' \
                           f'access_token={self.token}&' \
                           f'v=5.21&'

    def create_url(self, count=1, offset=0):

        self.full_url = self.base_url + \
                        self.methods['wall'] + \
                        self.base_params + \
                        f'count={count}&' \
                        f'offset={offset}&'

        return self.full_url

    def get_data(self):
        response = requests.get(self.full_url)  # 200
        json_data = response.json()

        items_list = json_data['response']['items']

        for item in items_list:
            data = {'id': item['id'],
                    'like': item['likes']['user_likes'],
                    'text': item['text']}

            self.data_list.append(data)

        return self.data_list

    def like_add(self):
        likes = 0

        for data in self.data_list:
            if data['like'] == 1:
                print(f'{data["id"]} - лайк был поставлен')
            else:
                self.url_to_like = self.base_url + \
                                   self.methods['like'] + \
                                   self.base_params + \
                                   f'type=post&' \
                                   f'item_id={data["id"]}&'
                requests.get(self.url_to_like)

                pprint(data)
                print('Лайк поставлен')

                likes += 1

        print(f'было проставлено {likes}')

        return self.url_to_like
