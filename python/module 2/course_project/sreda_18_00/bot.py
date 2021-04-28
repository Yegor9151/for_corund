from pprint import pprint
import requests


class Bot:
    base_url = 'https://api.vk.com/method/'
    method = {
        'wall_get': 'wall.get?'
    }
    full_url = None

    def __init__(self, owner_id, token):
        self.base_params = f'owner_id=-{owner_id}&' \
                           f'access_token={token}&' \
                           f'v=5.21&'

    def create_url(self, count=1, offset=0):
        self.full_url = self.base_url + \
                        self.method['wall_get'] + \
                        self.base_params + \
                        f'count={count}&' \
                        f'offset={offset}&'
        return self.full_url
