def generate_token(client_id, display="page", scope="wall", v=5.21):
    """
    Принимает id приложения созданного в vk.com и возвращает 
    ключ доступа (токен) для общения с сервером

    Params:
        client_id: id приложения
        display: тип отображения (page - форма авторизации в отдельном окне, 
                                  popup - всплывающее окно, 
                                  mobile - авторизация для мобильных устройств)
        scope: права доступа (все варианты: https://dev.vk.com/reference/access-rights)
    """

    url = f"https://oauth.vk.com/authorize?" + \
          f"client_id={client_id}&" + \
          f"display={display}&" + \
          f"redirect_uri=https://oauth.vk.com/blank.html&" + \
          f"scope={scope}&" + \
          f"response_type=token&" + \
          f"v={v}&"

    return url


def get_token(file):
    """
    Берет токен из файла

    Params:
        file: путь до файла
    """
    try:
        with open(file=file, mode="r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("Путь до токена не найден")