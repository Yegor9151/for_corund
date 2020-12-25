import requests
import time
from pprint import pprint


def read_token(path) -> str:
    # https://oauth.vk.com/authorize?client_id=ID_APP&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=offline,wall&response_type=token&v=5.52
    with open(path, 'r', encoding='utf-8') as f:
        token = f.read()
        return token


def get_obj(item_list, obj: str) -> list:
    item_ids = [item[obj] for item in item_list]

    if len(item_ids) > 10:
        print(f'{item_ids[:5]} ... {item_ids[-5:]}')
        print(len(item_ids))
    else:
        print(f'{item_ids}')
        print(len(item_ids))

    return item_ids


class BaseVariables:
    token = read_token(path='token.txt')

    base_url = 'https://api.vk.com/method/'

    methods = {'wall': {'get': 'wall.get?',
                        'get_comments': 'wall.getComments?'},
               'like': 'likes.add?'}

    groups_id = {'MTI': 717965,
                 'WDC': 170973719}


class Like:
    bv = BaseVariables

    def __init__(self, name):
        self.owner_id = self.bv.groups_id[name]

    def wall(self):
        bv = self.bv
        url_method = bv.base_url + bv.methods['wall']['get']
        count = 100

        offset = 0
        parameters = f'owner_id=-{self.owner_id}&' \
                     f'count={count}&' \
                     f'offset={offset}&' \
                     f'access_token={bv.token}&' \
                     f'v=5.126'
        full_urs = url_method + parameters

        response = requests.get(full_urs)
        json_obj = response.json()

        items = json_obj['response']['items']
        ids = get_obj(item_list=items, obj='id')

        return ids

    def comments(self, post_id):
        bv = self.bv
        url_method = bv.base_url + bv.methods['wall']['get_comments']
        count = 100

        offset = 0
        parameters = f'owner_id=-{self.owner_id}&' \
                     f'post_id={post_id}&' \
                     f'count={count}&' \
                     f'offset={offset}&' \
                     f'access_token={bv.token}&' \
                     f'v=5.95'
        full_urs = url_method + parameters

        response = requests.get(full_urs)
        json_obj = response.json()

        items = json_obj['response']['items']
        ids = get_obj(item_list=items, obj='id')

        return ids

    def under_comment(self, post_id, comment_id):
        bv = self.bv
        url_method = bv.base_url + bv.methods['wall']['get_comments']
        count = 100

        offset = 0
        parameters = f'owner_id=-{self.owner_id}&' \
                     f'post_id={post_id}&' \
                     f'comment_id={comment_id}&' \
                     f'count={count}&' \
                     f'offset={offset}&' \
                     f'access_token={bv.token}&' \
                     f'v=5.95'
        full_urs = url_method + parameters

        response = requests.get(full_urs)
        json_obj = response.json()

        items = json_obj['response']['items']
        ids = get_obj(item_list=items, obj='id')

        return ids

    def like(self, idx, type_item):
        bv = self.bv
        url_method = bv.base_url + bv.methods['like']

        parameters = f'type={type_item}&' \
                     f'owner_id=-{self.owner_id}&' \
                     f'item_id={idx}&' \
                     f'access_token={bv.token}&' \
                     f'v=5.21'
        full_urs = url_method + parameters

        response = requests.get(full_urs)
        json_obj = response.json()

        pprint(json_obj)

    def place_likes(self):
        post_ids = self.wall()
        for p_i in post_ids:
            time.sleep(0.5)
            self.like(idx=p_i, type_item='post')
            comment_ids = self.comments(post_id=p_i)
            for c_i in comment_ids:
                time.sleep(0.5)
                self.like(idx=c_i, type_item='comment')
                under_comment_ids = self.under_comment(post_id=p_i, comment_id=c_i)
                for u_c_i in under_comment_ids:
                    print(f'подкомментарий: {u_c_i}')
                    time.sleep(0.3)
                    self.like(idx=u_c_i, type_item='comment')


wdc_data = Like('WDC')
wdc_data.place_likes()
