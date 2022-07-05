import logging
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup
from weather import weather_by_city

logging.basicConfig(
filename='bot.log',
format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
level=logging.INFO)

# Настройки прокси
#PROXY = {'proxy_url': settings.PROXY_URL
#, 'urllib3_proxy_kwargs': {'assert_hostname': 'False', 'cert_reqs': 'CERT_NONE'}
#        }

# Если SOCKS5:
#PROXY = {'proxy_url': settings.PROXY_URL,
   # 'urllib3_proxy_kwargs': {
   #     'username': settings.PROXY_USERNAME,
    #    'password': settings.PROXY_PASSWORD
  #  }
#}
def greet_user(update, context):
    print('Вызван /start')
    my_keyboard = ReplyKeyboardMarkup([['погода в Москве']])
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start',reply_markup = my_keyboard)


def talk_to_me(update, context):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)       

def send_weather(update, context):
    weather=weather_by_city('Moscow,Russia')
    my_weather=f"сейчас в Москве {weather['temp_C']}C"
    print(my_weather)
    update.message.reply_text(my_weather)

def main():
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    mybot = Updater(settings.API_KEY, use_context=True)
    #, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.regex('^(погода в Москве)$'), send_weather))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    
    # Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()



# Вызываем функцию main() - именно эта строчка запускает бота
if __name__ == "__main__":
    main()
