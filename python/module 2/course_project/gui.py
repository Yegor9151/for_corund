from course_project.main import BotLiker
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Бот - Лайкер')
root.resizable(False, False)


def create_line(text='Сдесь чет по красивее', row=0, column=0, default=None):
    Label(text=text).grid(row=row, column=column)
    data = Entry()
    if default:
        data.insert(0, default)
    data.grid(row=row, column=column + 1)
    return data.get()


owner_id = create_line(text='Введите Id странички в VK:',
                       row=0, column=0, default='44273004')

post_count = create_line(text='Введите число постов:',
                         row=1, column=0, default='1')

path_to_token = create_line(text='Введите путь до токена:',
                            row=2, column=0, default='F:token.txt')


def run():
    likes = BotLiker(
        owner_id=owner_id, path_to_token=path_to_token).run(count=int(post_count))

    messagebox.showinfo(
        title='Отчет о работе', message=f'Число поставленных лайков {likes}')


Button(text='Погнали!', command=run).grid(row=3, column=1)

root.mainloop()
