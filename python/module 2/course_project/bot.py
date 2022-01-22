from itertools import count
import requests


class VkBot:

    def __init__(self, token, owner_id) -> None:
        self.token = token
        self.owner_id = owner_id
    
    def url_to_wall(self, count=100, offset=0) -> str:
        """
        Создает ссылку до стены в vk.com

        Params:
            count: число постов
            offset: сколько постов пропустить
        """
        
        wall = f"https://api.vk.com/method/wall.get?" + \
                    f"access_token={self.token}&" + \
                    f"owner_id=-{self.owner_id}&" + \
                    f"v=5.81&" + \
                    f"count={count}&" + \
                    f"offset={offset}&"

        return wall

    def get_wall(self, count=100, offset=0):
        wall = self.url_to_wall(count, offset)
        wall = requests.get(wall)
        wall = wall.json()

        try:
            wall = wall["response"]['items']

            self.posts = []
            for post in wall:
                post = {"id": post["id"],
                        "text": post["text"],
                        "like": post["likes"]["user_likes"]}

                self.posts.append(post)
            
            return self.posts

        except KeyError:
            return wall["error"]["error_msg"]

    def url_to_like(self, post_id):
        url = f"https://api.vk.com/method/likes.add?" + \
              f"access_token={self.token}&" + \
              f"owner_id=-{self.owner_id}&" + \
              f"v=5.81&" + \
              f"type=post&" + \
              f"item_id={post_id}&"

        return url

    def add_likes(self):
        count = 0
        for post in self.posts:
            if post['like']:
                print(f"Для поста - {post['id']} лайк уже был поставлен")
            else:
                url = self.url_to_like(post['id'])
                requests.get(url)
                print(f"{post['id']} - лайк поставлен")
                count += 1

        return count

