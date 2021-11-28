from datetime import date
import pandas as pd


def str_to_date(bdate):
    bdate = bdate.split(sep='/')  # разбиваем строку
    bdate = [int(i) for i in bdate]  # переводим строки в числа
    bdate = date(day=bdate[0],
                 month=bdate[1],
                 year=bdate[2])  # переводим числа в дату
    return bdate


def read_db(path):
    return pd.read_csv(path)


def rewrite_db(df, data):
    return df.append(data, ignore_index=True)


def save_db(df, path):
    df.to_csv(path, index=False)
