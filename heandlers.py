from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from weather import weather_by_city
from utils import first_inline_keyboard, first_text_keyboard

def greet_user(update, context):
    print('Вызван /start')
#    my_keyboard = ReplyKeyboardMarkup([['погода в Москве'],['Анкета']])
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start', reply_markup = first_text_keyboard())

def talk_to_me(update, context):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)       

def send_weather(update, context):
    weather=weather_by_city('Moscow,Russia')
    my_weather=f"сейчас в Москве {weather['temp_C']}C"
    print(my_weather)
    update.message.reply_text(my_weather)

def test_heandler(update, context):
    update.message.reply_text('Привет', reply_markup=ReplyKeyboardRemove())
    update.message.reply_text('Тестируем inline клавиатуру', reply_markup = first_inline_keyboard())