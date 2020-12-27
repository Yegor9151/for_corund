def read_file(path) -> str:
    """ Читает содержимое файла """

    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
        return text
