from support import read_file
from bot import Bot

corund = 44273004

# ТОКЕН
PATH_TO_TOKEN = "F:\\token.txt"
token = read_file(PATH_TO_TOKEN)

# БОТ
bot = Bot(owner_id=corund, token=token)  # создаем бота
# ДЕЙСТВИЯ БОТА
url = bot.create_url(count=100)  # бот, создай ссылку
data = bot.get_data()  # достань данные
like = bot.like_add()  # поставь лайк
