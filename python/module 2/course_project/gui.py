from main import BotLiker
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title(string='Бот - VK лайкер')
root.resizable(False, False)

Label(text="Введите Id странички в VK:").grid(row=0, column=0)
group_id = Entry()
group_id.insert(0, '44273004')
group_id.grid(row=0, column=1)

Label(text="Введите число постов:").grid(row=1, column=0)
post_count = Entry()
post_count.insert(0, '1')
post_count.grid(row=1, column=1)

Label(text="Введите путь до токена:").grid(row=2, column=0)
path_to_token = Entry()
path_to_token.insert(0, 'E:token.txt')
path_to_token.grid(row=2, column=1)


def run(count):
    likes = BotLiker(
        group_id=int(group_id.get()),
        path_to_token=path_to_token.get()
    ).run(count=int(count))
    messagebox.showinfo(
        title='Отчет о работе',
        message=f'Число поставленных лайков {likes}'
    )


Button(
    text='Run',
    command=lambda: run(post_count.get())
).grid(row=3, column=1)

root.mainloop()
