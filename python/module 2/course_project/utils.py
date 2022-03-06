"""
В этом модуле хранятся удобные утилиты
"""


def generate_token(client_id):
    """
    Эта фунция создает ссылку до токена

    :param client_id: id приложения в vk.com
    :return: ссылка
    """
    url = f"https://oauth.vk.com/authorize?" \
          f"client_id={client_id}&" \
          f"display=page&" \
          f"redirect_uri=https://oauth.vk.com/blank.html&" \
          f"scope=wall,offline&" \
          f"response_type=token&" \
          f"v=5.81&"

    return url


def read_token(path):
    """
    Функция для чтения токена (файла)

    :param path: путь до файла
    :return: содержимое файла
    """
    try:
        with open(file=path, mode="r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError as e:
        print(f"Путь не найден: {e}")
