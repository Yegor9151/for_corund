from tkinter import *
from datetime import datetime

from support import date_type

import pandas as pd

# INIT DATABASE
df = pd.DataFrame(
    columns=['ФИО', 'Возраст', 'Дата рождения', 'Интересы', 'Дата регистрации']
)

# INIT MASTER
root = Tk()
root.title('Регистрация клиентов')  # rename master window


# FUNCTIONS FOR BUTTONS
def get_data():
    """get data and collect it in data base"""

    # BASE VARIABLES
    data = {}  # init dict for data

    # DATA FROM STRINGS
    name = ent_name.get()  # get name
    data['ФИО'] = name  # collect in dict

    b_date = ent_b_date.get()  # get birth date
    data['Дата рождения'] = date_type(b_date)  # collect in dict

    datetime_now = datetime.now()  # get today date
    data['Дата регистрации'] = datetime_now.date()  # get date only

    age = (data['Дата регистрации'] - data['Дата рождения']) / 365.25  # calculate age
    data['Возраст'] = age.days  # days out

    interest_list = []
    booleans_interest = bool_py, bool_ja, bool_1c, bool_an, bool_no
    interest_name = 'наука', 'техника', 'икусство', 'путешествие', 'другое'
    i = 0
    while i < len(booleans_interest):
        bool_interest = booleans_interest[i]
        if bool_interest.get() == 1:
            interest_list.append(interest_name[i])
        i += 1

    data['Интересы'] = interest_list

    # CLEAN STRINGS
    ent_name.delete(0, END)
    ent_b_date.delete(0, END)

    # COLLECT
    global df
    df = df.append(data, ignore_index=True)


def base():
    base_frame.pack(side=TOP, anchor=W, pady=10)

    lab_name.grid(row=0, column=0, sticky=E)
    ent_name.grid(row=0, column=1, sticky=W, padx=10)

    lab_b_date.grid(row=1, column=0, sticky=E)
    ent_b_date.grid(row=1, column=1, sticky=W, padx=10)


def language():
    lang_frame.pack(side=TOP, anchor=W)

    lab_languages.pack(side=TOP, anchor=W)

    flag_py.pack(side=TOP, anchor=W)
    flag_ja.pack(side=TOP, anchor=W)
    flag_1c.pack(side=TOP, anchor=W)
    flag_an.pack(side=TOP, anchor=W)


def buttons():
    but_frame.pack(side=TOP, anchor=E)

    but_data.pack(side=LEFT, pady=10)
    but_close.pack(side=LEFT, padx=10, pady=10)


# BASE DATA
base_frame = Frame(master=root)
# STRING NAME
lab_name = Label(master=base_frame, text='Введите ФИО:')
ent_name = Entry(master=base_frame, width=40)
# STRING BIRTH DATE
lab_b_date = Label(master=base_frame, text='Введите дату рождения:')
ent_b_date = Entry(master=base_frame, width=40)

# CHOICE LANGUAGE
lang_frame = Frame(master=root)
lab_languages = Label(master=lang_frame, text='Выберите языки которые знаете или изучаете:')


def create_flag(master, name):
    boolean = BooleanVar()
    boolean.set(0)
    flag = Checkbutton(master=master, text=name, variable=boolean, onvalue=1, offvalue=0)
    return flag, boolean


# FLAGS OF LANGUAGES
flag_py, bool_py = create_flag(master=lang_frame, name='наука')
flag_ja, bool_ja = create_flag(master=lang_frame, name='техника')
flag_1c, bool_1c = create_flag(master=lang_frame, name='искусство')
flag_an, bool_an = create_flag(master=lang_frame, name='путешествие')
flag_no, bool_no = create_flag(master=lang_frame, name='другое')

# BUTTON GET DATA
but_frame = Frame(master=root)
# COMMANDS
but_data = Button(master=but_frame, text='Enter', width=10, command=get_data)
but_close = Button(master=but_frame, text='Close', width=10, command=root.destroy)

# OPEN PEACES
base()
language()
buttons()
# OPEN WINDOWS
root.mainloop()
