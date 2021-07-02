from datetime import date
import pandas as pd


def str_to_date(dateStr):
    """
    Фуекция для перевода даты из str в тип date
    :param dateStr: '12/12/1212'
    :return date: 1212-12-12
    """
    sepsTuple = '/', '.', '-', ' '
    date_type = None

    idx = 0  # индекс
    while idx < len(sepsTuple):
        if sepsTuple[idx] in dateStr:
            dateList = dateStr.split(sep=sepsTuple[idx])

            date_type = date(day=int(dateList[0]),
                             month=int(dateList[1]),
                             year=int(dateList[2]))
        idx += 1

    return date_type


def read_file(name):
    return pd.read_csv(name, index_col=0)


def add_db(file, data):
    df = read_file(file)  # pd.read_csv(name, index_col=0)

    df = df.append(data, ignore_index=True)
    df = df.drop_duplicates(subset=df.columns[:-2], keep='first')

    df.to_csv(file, index=True)
