import telebot

def keyboard(*buttons):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row(*buttons)
    return keyboard