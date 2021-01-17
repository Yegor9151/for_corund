from support import *
from bot import Bot
from pprint import pprint

# https://oauth.vk.com/authorize?
# client_id=ID_APP&
# display=page&
# redirect_uri=https://oauth.vk.com/blank.html&
# scope=offline,wall&
# response_type=token&
# v=5.52

# ТОКЕН
path_to_token = '..\\token.txt'
token = read_file(path_to_token)

# ID ГРУППЫ
corundum_id = 44273004

# ИНИЦИАЛИЗАЦИЯ БОТА
corundum_liker = Bot(token=token, owner_id=corundum_id)

# ССЫЛКА НА JSON СТЕНЫ
wall_url = corundum_liker.create_url(count=1)

# ОТВЕТ СО СТЕНЫ
result = get_data(wall_url)
pprint(result)
