from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup,ParseMode
from telegram.ext import ConversationHandler
from utils import first_text_keyboard

def anketa_start(update,context):
    update.message.reply_text(
        "Как вас зовут? Напишите имя и фамилию",
        reply_markup=ReplyKeyboardRemove()
        )
    return 'name'

def anketa_name(update, context):
    user_name = update.message.text
    if len(user_name.split())<2:
        update.message.reply_text("Пожалуйста, напишите имя и фамилию")
        return "name"
    else: 
        context.user_data['anketa'] = {"name": user_name}
        update.message.reply_text("сколько вам годиков")
        return "year"

def anketa_end(update, context):
    user_age = update.message.text
    if user_age.lower()!=user_age.upper():
        update.message.reply_text("Пожалуйста вводите только цифры")
        return "year"
    context.user_data['anketa']['year'] =  int(user_age)
#    user_text = f"""<b>Имя Фамилия:</b> {context.user_data['anketa']['name']}
#                    <b>Возраст:</b> {context.user_data['anketa']['year']}
#                """
    user_text = f"""Привет {context.user_data['anketa']['name']}, Вам {context.user_data['anketa']['year']} лет"""
    update.message.reply_text(user_text, reply_markup=first_text_keyboard(),
                                parse_mode=ParseMode.HTML)
    return ConversationHandler.END