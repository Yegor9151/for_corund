# ГРУППА - СРЕДА В 18.00

# библотеки + модули
from tkinter import *  # GUI
from datetime import datetime
from scripts import *
from pprint import pprint


def get_data():
    name = ent_name.get()
    # name = 'Сорокин ЕЛ'

    b_date = ent_date.get()  # вытаскиваем из Entry дату рождения
    # b_date = '12/12/2000'

    b_date = str_to_date(b_date)
    now_date = datetime.now().date()
    age = ((now_date - b_date) / 365.25).days

    if radio_var.get() == 0:
        gender = 'мужской'
    else:
        gender = 'женский'

    # словарь для данных
    dataDict = {'ФИО': name,
                'Дата рождения': b_date,
                'Дата регистрации': now_date,
                'Возраст': age,
                'Пол': gender,
                'Интересы': get_interests()}

    pprint(dataDict)

    add_db(file='users.csv', data=dataDict)

    ent_name.delete(first=0, last=END)  # Entry
    ent_date.delete(first=0, last=END)  # Entry

    idx = 0
    while idx < len(interests_varList):
        interests_varList[idx].set(0)
        idx += 1


def get_interests():
    """Это функция собирает ответы пользователя с флагов интересов
    и возвращает спок имен отмеченных интересов"""
    interestsList = []

    idx = 0
    while idx < len(interests_varList):
        if interests_varList[idx].get():
            interestsList.append(interest_names[idx])
        idx += 1

    return interestsList


# БАЗОВЫЕ ПЕРЕМЕННЫЕ
# РОДИТЕЛЬСКОЕ ОКНО
root = Tk()
root.title('Регистрационный лист')

# ФРЕЙМ ДЛЯ ФИО И ДАТА РОЖДЕНИЯ
text_frame = Frame(master=root)

# ФИО
lbl_name = Label(master=text_frame, text='Введите свое ФИО:')
ent_name = Entry(master=text_frame)  # собирает ФИО

# ДАТА РОЖДЕНИЯ
lbl_date = Label(master=text_frame, text='Введите дату рождения:')
ent_date = Entry(master=text_frame)  # собирает дату рождения


def open_text():
    # Фрейм
    text_frame.pack(side=TOP, anchor=W, pady=10, padx=10)
    # ФИО
    lbl_name.grid(row=0, column=0, sticky=E)
    ent_name.grid(row=0, column=1, sticky=W)
    # Дата рождения
    lbl_date.grid(row=1, column=0, sticky=E)
    ent_date.grid(row=1, column=1, sticky=W)


# ФРЕЙМ ДЛЯ ВЫБОР ПОЛА
gender_frame = Frame(master=root)
lbl_gender = Label(master=gender_frame, text='Ваш пол:')

# РАДИОКНОПКИ
radio_var = IntVar()
radio_var.set(0)

male_radio = Radiobutton(master=gender_frame, text='Мужчина',
                         variable=radio_var, value=0)
female_radio = Radiobutton(master=gender_frame, text='Женщина',
                           variable=radio_var, value=1)


def open_radio():
    # Фрейм
    gender_frame.pack(side=TOP, anchor=W, padx=10)
    # "Ваш пол"
    lbl_gender.pack(side=TOP, anchor=W)
    # Радиокнопки - выбор пола
    male_radio.pack(side=LEFT, anchor=W)
    female_radio.pack(side=LEFT, anchor=W)


# ФРЕЙМ ДЛЯ ИНТЕРЕСОВ
flag_frame = Frame(master=root, bg='#ffccff')
lbl_flag = Label(master=flag_frame, text='Выберите интересы:')

interest_names = 'Наука', 'Техника', 'Иcкусство', \
                 'Путешествие', 'Спорт', 'Другое'


def create_interest(name):
    var = BooleanVar()
    but = Checkbutton(master=flag_frame, text=name,
                      variable=var, onvalue=1, offvalue=0)
    return but, var


interests_buttonList = []
interests_varList = []

idx = 0
while idx < len(interest_names):
    interestBut, interestVar = create_interest(
        name=interest_names[idx]  # первый объект 0 - Наука
    )
    interests_buttonList.append(interestBut)
    interests_varList.append(interestVar)
    idx += 1


def open_interests():
    """создание флажков интересов"""
    flag_frame.pack(side=TOP, anchor=W, padx=10, pady=10)
    lbl_flag.pack(side=TOP, anchor=W)  # Выюерите интересы

    # перебираем список заролектированных флажков
    idx = 0
    while idx < len(interests_buttonList):
        interests_buttonList[idx].pack(side=TOP, anchor=W)
        idx += 1


# ФРЕЙМ ДЛЯ КНОПОК SAVE & CLOSE
but_frame = Frame(master=root)
enter = Button(master=but_frame, text='Enter',
               bg='#cbffc3', width=10, command=get_data)
close = Button(master=but_frame, text='Close',
               bg='#ffcccb', width=10, command=root.destroy)


def open_buttons():
    but_frame.pack(side=TOP, anchor=E, padx=10, pady=10)
    enter.pack(side=LEFT, anchor=W, padx=10)
    close.pack(side=LEFT, anchor=W)


# РАЗВЕРТКИ
open_text()
open_radio()
open_interests()
open_buttons()

# родительское окно
root.mainloop()

read_file('users.csv')
