from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from emoji import emojize

def first_inline_keyboard():
    smile = emojize (':hankey:', use_aliases=True)
    inlinekeyboard = [
        [InlineKeyboardButton("Это супер-пупер Button1", callback_data='Anketa'),
        InlineKeyboardButton(f"это {smile} Button2", callback_data='weather')],
        [InlineKeyboardButton(emojize (':wine_glass:', use_aliases=True)+f'наше дело правое', callback_data='1')],
        [InlineKeyboardButton(f"это", callback_data='11'),
        InlineKeyboardButton("будет", callback_data='12'),
        InlineKeyboardButton(f"работать позже", callback_data='13')
        ]
       # [InlineKeyboardButton('Button3')]
    ]
    return InlineKeyboardMarkup(inlinekeyboard)

def first_text_keyboard():
    return ReplyKeyboardMarkup([['/test'],['погода в Москве','Анкета']])