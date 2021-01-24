def read_file(path) -> str:
    """ Читает содержимое файла
    input: path to file
    output: text """

    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
        return text
