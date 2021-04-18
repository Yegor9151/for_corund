"""БИБЛЕОТЕКИ"""
from tkinter import *
import pandas as pd
from datetime import datetime
from scr import str_in_date

"""КОНСТАНТЫ"""
WIDTH = 350
HEIGHT = 375

"""РОДИТЕЛЬСКОЕ ОКНО"""
root = Tk()
root.title('Регистрационный лист')
root.geometry(f'{WIDTH}x{HEIGHT}')
root.resizable(width=False, height=False)

"""ФИО И ДАТА - ФРЕЙМЫ"""
textFrame = Frame(master=root)  # Создаем невидимое подокно
textFrame.pack(side=TOP, anchor=W, padx=10, pady=10)  # размещаем по очереди

Label(  # Класс создающий не редактируемую строку
    master=textFrame, text='Введите ФИО'
).grid(row=0, column=0, sticky=E)  # размещаем по сетке

Label(  # --//--
    master=textFrame, text='Введите дату рождения'
).grid(row=1, column=0, sticky=E)  # --//--

nameEntry = Entry(master=textFrame, width=30)  # Класс создающий редактируемую строку
nameEntry.grid(row=0, column=1)  # --//--

b_dateEntry = Entry(master=textFrame, width=30)  # --//--
b_dateEntry.grid(row=1, column=1)  # --//--

"""ВЫБОР ПОЛА - ФРЕЙМ"""
genderFrame = Frame(master=root)
genderFrame.pack(side=TOP, anchor=W, padx=10, pady=10)

Label(master=genderFrame, text='Выберите пол').pack(anchor=W)

genderIntVar = IntVar()  # обрабативает числовое значение

maleRb = Radiobutton(master=genderFrame, text='Мужской',
                     variable=genderIntVar, value=0)
maleRb.pack(side=LEFT)

femaleRB = Radiobutton(master=genderFrame, text='Женский',
                       variable=genderIntVar, value=1)
femaleRB.pack(side=LEFT)

"""ВЫБОР ИНТЕРЕСОВ - ФРЕЙМ"""
interestFrame = Frame(master=root)
interestFrame.pack(side=TOP, anchor=W, padx=10, pady=10)

Label(master=interestFrame, text='Выберите интересы').pack(anchor=W)


def create_interest():
    """функция для слздания кнопок интересов"""

    interest_answerList = []  # создаем пустой редактируемый список

    idx = 0
    while idx < len(interestTuple):
        interestBoolVar = BooleanVar()  # считывает ответы пользователя

        interestCB = Checkbutton(  # создаем кнопку интереса
            master=interestFrame,
            text=interestTuple[idx],
            variable=interestBoolVar,
            onvalue=True, offvalue=False
        )
        interestCB.pack(anchor=W)

        # добавляем ответ пользователя в пустой список
        interest_answerList.append(interestBoolVar)
        idx += 1

    return interest_answerList  # возвращаем заполненный список


interestTuple = 'Спорт', 'Наука', 'Программирование', 'Компьютерные игры', 'Путешествия', 'Другое'

# сохранение результатов работы функции, которая создает и региструрует отметки пользователя
interest_answerList = create_interest()

"""SAVE, CLOSE - ФРЕЙМ"""
buttonsFrame = Frame(master=root)
buttonsFrame.pack(side=TOP, anchor=E, padx=10, pady=10)


def get_data():
    name = nameEntry.get()
    name = 'СорокинЕЛ'  # тестовые данные

    b_date = b_dateEntry.get()
    b_date = '29/01/1991'  # тестовые данные

    today = datetime.now().date()
    b_date = str_in_date(b_date)

    if genderIntVar.get() == 0:
        gender = 'Мужской'
    else:
        gender = 'Женский'

    dataDict = {
        'ФИО': name,  # Вытягиваем ФИО
        'Пол': gender,  # вписываем пол
        'Интересы': [get_interests()],
        'Возраст': ((today - b_date) / 365.25).days,  # расчитываем возраст
        'Дата рождения': b_date,  # Вытягиваем Дату рождения и переводим в тип дата
        'Дата регистрации': today,  # вписываем текущую дату
    }  # Словарь с данными о пользователе
    print(dataDict)

    df = pd.DataFrame(dataDict)
    print(df)


def get_interests():
    flag_interestsList = []

    idx = 0
    while idx < len(interest_answerList):
        # находим те индексы значения которых = True
        if interest_answerList[idx].get():
            flag_interestsList.append(interestTuple[idx])
        idx += 1

    return flag_interestsList


Button(
    master=buttonsFrame, text='Save',
    bg='#cbffc3', width=10, command=get_data
).pack(side=LEFT, padx=2)

Button(
    master=buttonsFrame, text='Close',
    bg='#ffcccb', width=10, command=root.destroy
).pack(side=LEFT, padx=2)

"""ФУНКЦИИ РАЗВЕРТКИ"""
root.mainloop()
