from tkinter import *
import random

root = Tk(className='Угадай число')
# root.geometry('400x400')

min_, max_ = 1, 100
num = None


def predict(more=None, less=None):
    global min_, max_, num

    if more:
        min_ = num + 1
    elif less:
        max_ = num - 1

    num = random.randint(min_, max_)
    answer['text'] = num

    print(more, less)
    print(min_, max_)


def finish():
    Label(text='Ура, я выиграл!', font='Times 30').pack(side=BOTTOM)


Button(text='Больше',
       command=lambda more=True: predict(more=more),
       font='Times 30'
       ).pack(side=RIGHT)

answer = Button(command=finish, font='Times 64', width=4)
answer.pack(side=RIGHT)
predict()

Button(text='Меньше',
       command=lambda less=True: predict(less=less),
       font='Times 30'
       ).pack(side=RIGHT)

root.mainloop()
