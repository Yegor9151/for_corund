def read_file(path):
    with open(file=path, mode='r', encoding='utf-8') as file:
        return file.read()
