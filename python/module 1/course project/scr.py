from datetime import date


def str_in_date(dateStr):
    day, month, year = dateStr.split('/')

    result = date(
        year=int(year),
        month=int(month),
        day=int(day)
    )
    return result
