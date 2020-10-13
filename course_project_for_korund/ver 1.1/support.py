from datetime import date


# FUNCTIONS
def date_type(date_string):
    """get date in string format and convert it in date type"""

    # BASE VARIABLES
    seps = '/ . - '.split()  # init separators
    date_list = 'no list'  # init list for date in string format

    # SPLIT STRING
    i = 0  # init index counter
    while i < len(seps):  # check index value
        if seps[i] in date_string:  # check separators in argument
            sep = seps[i]  # init separator type
            date_list = date_string.split(sep=sep)  # split string
        i += 1  # up index value

    # CONVERT IN INTEGER
    i = 0  # init index counter
    while i < len(date_list):  # check index value
        date_list[i] = int(date_list[i])  # change type
        i += 1  # up index value

    # FINISH
    day, month, year = date_list  # split list on variables
    return date(year, month, day)  # convert and return
