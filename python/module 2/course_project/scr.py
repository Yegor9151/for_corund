def read_file(file: str) -> str or None:
    """
    Функция для чтения файлов в кодировке UTF-8
    :param file: путь до файла в формате str
    :return: содержимое файла в формате str, либо возвращает None
    """
    try:
        with open(file, mode='r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print("Путь не найден / Проверьте наличие путь")
