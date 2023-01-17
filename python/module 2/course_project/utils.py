def get_token(client_id, scope="wall,offline"):
    """Функция для получения токена

    :param client_id: id приложения в vk
    :param scope: расширения для токена
    :return: ссылка на страницу в адресе которой будет токен
    """
    url = f"https://oauth.vk.com/authorize?" \
          f"client_id={client_id}&" \
          f"display=page&" \
          f"redirect_uri=https://oauth.vk.com/blank.html&" \
          f"scope={scope}&" \
          f"response_type=token&" \
          f"v=5.131"
    return url

# print(get_token(12345678))

def open_file(path, mode='r', text=None, encoding="utf-8"):
    """Читает или запысывает файл

    :param path: str - путь до файла
    :param mode: char = 'r' - читать (r) или записать (w)
    :param text: str - если на запись, то можно написать текст для записи
    :param encoding: str - в какой кадировке читать или записывать файл
    :return: str - тект файла
    """
    with open(path, mode=mode, encoding=encoding) as f:
        if mode == 'r':
            return f.read()
        elif mode == 'w':
            f.write(text)
            return text

