class Bot:
    __api_method_url = 'https://api.vk.com/method/'
    __methods = 'wall.get?'

    def __init__(self, owner_id, token):
        self.owner_id = owner_id
        self.token = token

    def create_url(self):
        count = 100
        offset = 0
        parameters = f'owner_id=-{self.owner_id}&' \
                     f'count={count}&' \
                     f'offset={offset}&' \
                     f'access_token={self.token}&' \
                     f'v=5.126'

        full_url = self.__api_method_url + self.__methods + parameters

        return full_url
