from tkinter import *
from datetime import datetime

from support import date_type

# import pandas as pd

# INIT DATABASE
# df = pd.DataFrame(
#     columns=['ФИО', 'Возраст', 'Дата рождения', 'Языки программирования', 'Дата регистрации']
# )

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

    language_list = []
    booleans_lang = bool_py, bool_ja, bool_1c, bool_an, bool_no
    languages_name = 'Python', 'Java', '1C', 'Другой', 'Никакой'
    i = 0
    while i < len(booleans_lang):
        bool_language = booleans_lang[i]
        if bool_language.get() == 1:
            language_list.append(languages_name[i])
        i += 1

    data['Языки программирования'] = language_list

    # CLEAN STRINGS
    ent_name.delete(0, END)
    ent_b_date.delete(0, END)

    # COLLECT
    # global df
    # df = df.append(data, ignore_index=True)


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
# FLAGS OF LANGUAGES
bool_py = BooleanVar()
bool_py.set(0)
flag_py = Checkbutton(master=lang_frame, text='Python', variable=bool_py, onvalue=1, offvalue=0)

bool_ja = BooleanVar()
bool_ja.set(0)
flag_ja = Checkbutton(master=lang_frame, text='Java', variable=bool_ja, onvalue=1, offvalue=0)

bool_1c = BooleanVar()
bool_1c.set(0)
flag_1c = Checkbutton(master=lang_frame, text='1C', variable=bool_1c, onvalue=1, offvalue=0)

bool_an = BooleanVar()
bool_an.set(0)
flag_an = Checkbutton(master=lang_frame, text='Другой', variable=bool_an, onvalue=1, offvalue=0)

bool_no = BooleanVar()
bool_no.set(0)
flag_no = Checkbutton(master=lang_frame, text='Никакой', variable=bool_no, onvalue=1, offvalue=0)

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
