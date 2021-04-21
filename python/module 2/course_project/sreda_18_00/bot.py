from pprint import pprint
import requests


class Bot:
    base_url = 'https://api.vk.com/method/'
    method = 'wall.get?'

    full_url = base_url + method

    answerCode = requests.get(url=full_url)
    answerJson = answerCode.json()
