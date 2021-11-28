from tkinter import *
from datetime import datetime
from util import *


# ЛОГИКА
def save():
    # name.insert(0, 'Sorokin YL')
    # date.insert(0, '29/01/1991')

    bdate = date.get()

    asd = [interests_list[idx] for idx in range(len(interesting)) if interesting[idx].get()]

    today = datetime.now().date()  # сегодняшняя дата и время
    bdate = str_to_date(bdate)  # дата рождения

    data = {
        "имя": name.get(),
        "дата рождения": bdate,
        "пол": "М" if gender_value.get() else "Ж",
        "интересы": asd,
        "дата регистрации": today,
        "возраст": ((today - bdate) / 365.25).days
    }

    path = "./users.csv"
    df = read_db(path)
    df = rewrite_db(df, data)
    save_db(df, path)


def clear_data():
    name.delete(0, END)
    date.delete(0, END)


# ОСНОВНЫЕ ПЕРЕМЕННЫЕ
WIDTH = 400
HEIGHT = 350
root = Tk()

root.title('Регистрационный лист')
root.geometry(f'{WIDTH}x{HEIGHT}')
root.resizable(False, False)

# ФИО и ДАТА РОЖДЕНИЯ
name_dateF = Frame(padx=10, pady=10)
Label(master=name_dateF, text='Введите ФИО:').grid(sticky=E, row=0, column=0)
Label(master=name_dateF, text='Введите дату рождения:').grid(sticky=E, row=1, column=0)
name = Entry(master=name_dateF, width=40)
date = Entry(master=name_dateF, width=40)

name.grid(row=0, column=1)
date.grid(row=1, column=1)
name_dateF.pack(anchor=W)

# ВЫБОР ПОЛА
genderF = Frame(padx=10, pady=10)
gender_value = BooleanVar(value=True)  # проверить если True

Label(master=genderF, text='Ваш пол:').pack(anchor=W)
Radiobutton(master=genderF, text='Мужской', variable=gender_value, value=True).pack(side=LEFT)
Radiobutton(master=genderF, text='Женский', variable=gender_value, value=False).pack(side=LEFT)
genderF.pack(anchor=W)

# ВЫБОР ИНТЕРЕСОВ
interestsF = Frame(padx=10, pady=10)
interests_list = ['компьютерные игры', 'чипушествия', 'мультики', 'спорт', 'другое']

Label(master=interestsF, text='Выберите интересы:').pack(anchor=W)

interesting = []
for i in interests_list:
    interest_value = BooleanVar()
    # onvalue, offvalue
    Checkbutton(master=interestsF, text=i, variable=interest_value).pack(anchor=W)
    interesting.append(interest_value)

interestsF.pack(anchor=W)

# SAVE & DELETE & CLOSE
buttonsF = Frame(padx=10, pady=10)
Button(master=buttonsF, bg='#E0FFDC', width=8, text='save', command=save).pack(side=LEFT)
Button(master=buttonsF, bg='#DCFFFD', width=8, text='delete', command=clear_data).pack(side=LEFT, padx=2)
Button(master=buttonsF, bg='#FFE9DC', width=8, text='close', command=root.destroy).pack(side=LEFT)
buttonsF.pack(side=BOTTOM, anchor=E)

# ЗАПУСК ПРОГИ
root.mainloop()
