from tkinter import *

root0 = Tk()
root1 = Tk()
root2 = Tk()
root3 = Tk()


def create_table(
        master: Tk,
        name: str,
        coord: str = '325x75',
        negative: bool = False
) -> 'true table':

    """Функция для развертывания таблиц истинности

    master      - привязывает объекты к окну,
    name        - переименовывает таблицу
    coord       - резулирует размер и положение окна
    negative    - меняет значения лейблов слева принимает значение True / False
    """

    master.title(f'True table - {name}')
    master.geometry(coord)

    text1, text2 = 'True', 'False'

    lbl00 = Label(master=master, text=name)
    lbl01 = Label(master=master, text=text1)
    lbl02 = Label(master=master, text=text2)

    if negative:
        text1, text2 = 'not True', 'not False'

    lbl10 = Label(master=master, text=text1)
    entry11 = Entry(master=master)
    entry12 = Entry(master=master)

    lbl20 = Label(master=master, text=text2)
    entry21 = Entry(master=master)
    entry22 = Entry(master=master)

    # размещение объектов
    lbl00.grid(row=0, column=0)
    lbl01.grid(row=0, column=1)
    lbl02.grid(row=0, column=2)

    lbl10.grid(row=1, column=0)
    entry11.grid(row=1, column=1)
    entry12.grid(row=1, column=2)

    lbl20.grid(row=2, column=0)
    entry21.grid(row=2, column=1)
    entry22.grid(row=2, column=2)


create_table(master=root0, name='And', negative=False)
create_table(master=root1, name='Or', negative=False)
create_table(master=root2, name='And not', negative=True)
create_table(master=root3, name='Or not', negative=True)

root0.mainloop()
