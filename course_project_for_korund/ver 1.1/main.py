from tkinter import *
from datetime import datetime

from support import date_type

import pandas as pd


def collect_data():
    """get data and collect it in data base"""

    # BASE VARIABLES
    data = {}  # init dict for data

    # DATA FROM STRINGS
    name = ent_name.get()  # get name
    data['ФИО'] = name  # collect in dict

    b_date = ent_b_date.get()  # get birth date
    data['дата рождения'] = date_type(b_date)  # collect in dict

    datetime_now = datetime.now()  # get today date
    data['дата регистрации'] = datetime_now.date()  # get date only

    age = (data['дата регистрации'] - data['дата рождения']) / 365.25  # calculate age
    data['возраст'] = age.days  # days out

    if var.get() == 0:
        data['пол'] = 'Мужской'
    elif var.get() == 1:
        data['пол'] = 'Женский'

    interest_list = flags_data()
    data['интересы'] = ', '.join(interest_list)

    # clean_text()

    global df
    df = df.append(data, ignore_index=True)


def add_in_bd(data):
    pass


def clean_text():
    """Очищает текстовые строки"""
    ent_name.delete(0, END)
    ent_b_date.delete(0, END)
    i = 0
    while i < len(booleans_interest):
        booleans_interest[i].set(0)
        i += 1


def flags_data():
    """Собирает отмеченные интересы"""
    interest_list = []
    i = 0
    while i < len(booleans_interest):
        if booleans_interest[i].get() == 1:
            interest_list.append(interest_names[i])
        i += 1

    return interest_list


def create_flag(name):
    """Создант флаг"""
    boolean = BooleanVar()
    boolean.set(0)
    flag = Checkbutton(master=interest_frame, text=name, variable=boolean,
                       onvalue=1, offvalue=0)
    return flag, boolean


# FUNCTIONS OPEN
def text_open():
    top_frame.pack(side=TOP, anchor=W, padx=10, pady=10)

    lbl_name.grid(row=0, column=0, sticky=E)
    ent_name.grid(row=0, column=1, sticky=W)

    lbl_b_date.grid(row=1, column=0, sticky=E)
    ent_b_date.grid(row=1, column=1, sticky=W)


def radio_open():
    radio_frame.pack(side=TOP, anchor=W, padx=10)
    lbl_sex.pack(side=TOP, anchor=W)

    male.pack(side=LEFT, anchor=W)
    female.pack(side=LEFT, anchor=W)


def flags_open():
    interest_frame.pack(side=TOP, anchor=W, padx=10, pady=10)

    interest_lbl.pack(side=TOP, anchor=W)

    i = 0
    while i < len(flags):
        flags[i].pack(side=TOP, anchor=W)
        i += 1


def buttons_open():
    but_frame.pack(side=TOP, anchor=E)

    but_data.pack(side=LEFT, pady=10)
    but_close.pack(side=LEFT, padx=10, pady=10)


# OPEN DATABASE
df = pd.read_csv('users.csv', index_col=0)

# INIT MASTER
root = Tk()
root.title('Лист регистрации')  # rename master window

# BASE DATA
top_frame = Frame(master=root)
# STRING NAME
lbl_name = Label(master=top_frame, text='Введите ФИО:')
ent_name = Entry(master=top_frame, width=40)
# STRING BIRTH DATE
lbl_b_date = Label(master=top_frame, text='Введите дату рождения:')
ent_b_date = Entry(master=top_frame, width=40)

# SEX RADIO BUTTONS
radio_frame = Frame(master=root)
# CREATE SEX BUTTONS
lbl_sex = Label(master=radio_frame, text='Выберите пол:')

var = IntVar()
var.set(0)
male = Radiobutton(master=radio_frame, text='Мужской', variable=var, value=0)
female = Radiobutton(master=radio_frame, text='Женский', variable=var, value=1)

# CHOICE INTEREST
interest_frame = Frame(master=root)
interest_lbl = Label(master=interest_frame, text='Выберите интересы:')
# INTEREST LIST
interest_names = 'Наука', 'Техника', 'Икусство', 'Путешествие', 'Спорт', 'Другое'
# CREATE FLAGS
flag_sc, bool_sc = create_flag(name=interest_names[0])
flag_tech, bool_tech = create_flag(name=interest_names[1])
flag_art, bool_art = create_flag(name=interest_names[2])
flag_tr, bool_tr = create_flag(name=interest_names[3])
flag_sp, bool_sp = create_flag(name=interest_names[4])
flag_an, bool_an = create_flag(name=interest_names[5])
# PACK FLAGS IN VARIABLE
flags = flag_sc, flag_tech, flag_art, flag_tr, flag_sp, flag_an
booleans_interest = bool_sc, bool_tech, bool_art, bool_tr, bool_sp, bool_an

# BUTTON GET DATA
but_frame = Frame(master=root)
# COMMANDS
but_data = Button(master=but_frame, bg='#cbffc3', text='Save', width=10, command=collect_data)
but_close = Button(master=but_frame, bg='#ffcccb', text='Close', width=10, command=root.destroy)

# OPEN PEACES
text_open()
radio_open()
flags_open()
buttons_open()

# OPEN WINDOWS
root.mainloop()

# CHECK DF
df = df.drop_duplicates(subset=df.columns[:-2], keep='last')
df.to_csv('users.csv', index=True)
