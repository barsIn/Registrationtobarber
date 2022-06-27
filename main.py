import pandas as pd
import json, os
from openpyxl.workbook import Workbook
from datetime import datetime, date, time, timedelta

def read(FILENAME):
    if os.path.isfile(FILENAME):
        with open(FILENAME) as f:
            data = json.load(f)
    return data

def save(data, FILENAME):
    with open(FILENAME, "w") as f:
        json.dump(data, f)


def wrightToExcel(excelfile, checktime, barberType, username):
    data = readFromExcel('./schedule.xlsx')
    print(data)
    datetstart = checktime
    delta = timedelta(hours=+1, minutes=-1)
    dateend = datetstart + delta
    barberType = barberType
    username = username
    if barberType.lower() == 'стрижка':
        coast = 1200
    elif barberType.lower() == 'борода':
        coast = 800
    else:
        coast = 2000
    last = len(data.get('id'))
    data.get('id').append(last)
    data.get('Начало').append(datetstart)
    data.get('Окончание').append(dateend)
    data.get('Тип стрижки').append(barberType)
    data.get('Имя').append(username)
    data.get('Стоимость').append(coast)
    # datax = {
    #     'id': data.get('id').append(last),
    #     'Начало': data.get('Начало').append(datetstart),
    #     'Окончание': data.get('Окончание').append(dateend),
    #     'Тип стрижки': data.get('Тип стрижки').append(barberType),
    #     'Имя': data.get('Имя').append(username),
    #     'Стоимость': data.get('Стоимость').append(coast),
    # }

    dt = pd.DataFrame(data)
    dt.to_excel(excelfile)

def readFromExcel(excelfile):
    excelData = pd.read_excel(excelfile, usecols=['id', 'Начало', 'Окончание', 'Тип стрижки', 'Имя', 'Стоимость'], header = 0)
    id = excelData['id'].tolist()
    datetstart = excelData['Начало'].tolist()
    dateend = excelData['Окончание'].tolist()
    barbType = excelData['Тип стрижки'].tolist()
    name = excelData['Имя'].tolist()
    coast = excelData['Стоимость'].tolist()


    data = {'id': id, 'Начало': datetstart, 'Окончание': dateend, 'Тип стрижки': barbType, 'Имя': name, 'Стоимость': coast}

    return data
#
# data = datetime(2022, 5, 11, 12, 30)
# barbertypy = 'Стрижка'
# username = 'Igor1'
# wrightToExcel('./schedule.xlsx', data, barbertypy, username)
# a = readFromExcel('./schedule.xlsx')
# print(data)
# readFromExcel('./flowers.xlsx', 'flowerlist.json')
# datetstart = datetime.utcnow()
# delta = timedelta(hours=+1)
#
# day1 = 11
# month = 1
# h = 13
# m = 00
# datetstart = datetime(datetstart.year, month, day1, h, m)
# dateend = datetstart + delta
# needdate = datetime(2022, 1, 11, 13, 30)
# print(f'начало {datetstart} окончание {dateend}')
#
# print(needdate)
# print(needdate <= dateend and needdate >= datetstart)