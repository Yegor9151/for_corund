import utils
from pprint import pprint
from bot import VkBot

# ПОЛУЧЕНИЕ ТОКЕНА
URL_TO_TOKEN = utils.generate_token(client_id=1234567)
PATH_TO_TOKEN = "E:\\token.txt"

# НАСТРОЙКИ
TOKEN = utils.get_token(PATH_TO_TOKEN)
OWNER_ID = 44273004
COUNT = 100
OFFSET = 0

# ССЫЛКА ДО СТЕНЫ
bot = VkBot(TOKEN, OWNER_ID)
data = bot.get_wall(5, OFFSET)
like = bot.add_likes()

pprint(data)
print(like)