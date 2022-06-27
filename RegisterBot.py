import telebot
from datetime import datetime
from Token import token
from main import wrightToExcel, readFromExcel, timedelta


bot = telebot.TeleBot(f'{token}')
data = readFromExcel('./schedule.xlsx')

def regist(message):
    if message.text.lower()[0:6] == 'запись':
        return True
    return False

def check(message):
    if message.text.lower()[0:13] == 'введи команду':
        return True

def checkDate(date):
    delta = timedelta(hours=+1, minutes=-1)
    thisend = date + delta
    data = readFromExcel('./schedule.xlsx')
    startTime = data.get('Начало')
    endtime = data.get('Окончание')
    print(len(startTime))

    for i in range(len(startTime)):

        if startTime[i] <= date <= endtime[i] or startTime[i] <= thisend <= endtime[i]:
            print(startTime[i])
            print(endtime[i])
            return False
    return True


def registration(message):
    textdata = message.text[6:]
    if len(textdata) > 12:
        if textdata[1:3].isdigit() and textdata[4:6].isdigit() and textdata[7:9].isdigit() and textdata[10:12].isdigit():
            thisDay = int(textdata[1:3])
            thisMonth = int(textdata[4:6])
            thisHour = int(textdata[7:9])
            thisMinute = int(textdata[10:12])
            checktime = datetime(2022, thisMonth, thisDay, thisHour, thisMinute)
            barberType = textdata[13:]
        else:
            return f'Неверный формат'
    else:
        return f'Неверный формат'
    if checkDate(checktime):
        wrightToExcel('./schedule.xlsx', checktime, barberType, message.from_user.username)

        return f'Запись успешно произведена на {checktime}\n ЖДЁМ ВАС в {checktime.hour}:{checktime.minute}👌'
    else:
        return f'Это время уже занято'



@bot.message_handler(commands=['start'])
def greeteengs(message: telebot.types.Message):
    text = "Тут можно записаться на стрижку \nВведи команду запись и через пробел дату в формате дд.мм чч:мм пример: 01.02 12:00 \n введи команду проверить дату и дату в формате дд.мм \n тип стрижки Стрижка/Борода/Полностью"
    bot.send_message(message.chat.id, text)


@bot.message_handler(func=regist)
def start(message):
    text = registration(message)
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=check)
def start(message):
    text = "На эту дату записи нет"
    bot.send_message(message.chat.id, text)

@bot.message_handler()
def start(message):
    bot.send_message(message.chat.id, 'нет такой команды')
    print(message.text.lower()[0:5])






bot.polling()
