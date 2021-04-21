from datetime import date
import pandas as pd


def str_in_date(dateStr):
    day, month, year = dateStr.split('/')

    result = date(
        year=int(year),
        month=int(month),
        day=int(day)
    )
    return result


def read_db(db='./users.csv'):
    df = pd.read_csv(db, index_col=0)
    return df


def add_data(data, db='./users.csv'):
    df = read_db(db)
    df = df.append(data, ignore_index=True)
    df = df.drop_duplicates(
        subset=['ФИО', 'Пол', 'Дата рождения'],
        keep='last'
    )
    df.to_csv(db)
    return df
