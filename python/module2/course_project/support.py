import requests


def read_file(path) -> str:
    """ Читает содержимое файла """

    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
        return text


def get_data(url):
    response = requests.get(url)
    json_obj = response.json()

    json_item = json_obj['response']['items'][0]

    id_item = json_item['id']
    user_likes = json_item['likes']['user_likes']
    text = json_item['text']

    return id_item, user_likes, text
