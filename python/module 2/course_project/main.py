from scr import read_file  # импортируем фуекцию для чтения токена
from bot import Bot  # импортируем класс-конструктор бота
from pprint import pprint


class BotLiker(Bot):
    def __init__(self, owner_id, path_to_token):
        super().__init__(owner_id, token=read_file(path_to_token))

    def run(self, count=1):  # pipline
        """
        Метод для выполнения последовательности действий
        """
        offsets = range(count // 100) if count % 100 == 0 else range((count // 100) + 1)

        for offset in offsets:
            count_now = 100 if offset != offsets[-1] else count - (offsets[-1] * 100)

            url = self.create_url(count=count_now, offset=offset * 100)  # бот - создай ссылку
            data = self.get_data()  # бот - достань данные

            print(f'\nСсылка до постов:\n{url}')

            if type(data) == str:
                print(data)
            else:
                print(f'\nСостояние данных:\n')
                pprint(data)

        count_like = self.add_likes()  # бот - поставь лайки

        print(f'\nЧисло проставленных лайков {count_like}')
        return count_like
