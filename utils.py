from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from emoji import emojize

def first_inline_keyboard():
    inlinekeyboard = [
        [InlineKeyboardButton("Анкета", callback_data='111'),
        InlineKeyboardButton("погода в Москве", callback_data='222')],
    ]
    return InlineKeyboardMarkup(inlinekeyboard)

def first_text_keyboard():
    return ReplyKeyboardMarkup([['/test'],['погода в Москве','Анкета']])