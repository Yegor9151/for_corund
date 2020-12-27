from support import read_file
from bot import Bot

# https://oauth.vk.com/authorize?
# client_id=ID_APP&
# display=page&
# redirect_uri=https://oauth.vk.com/blank.html&
# scope=offline,wall&
# response_type=token&
# v=5.52

path_to_token = '..\\token.txt'
token = read_file(path_to_token)

corundum_id = 44273004

corundum_liker = Bot(token=token, owner_id=corundum_id)
print(corundum_liker.create_url())
