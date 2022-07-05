from dataclasses import Field
import logging
import settings
from telegram.ext import (Updater, CommandHandler, MessageHandler, MessageHandler,MessageHandler,
Filters, ConversationHandler, CallbackQueryHandler)
from heandlers import greet_user, send_weather, talk_to_me
from anketa import anketa_start, anketa_name, anketa_end

logging.basicConfig(
filename='bot.log',
format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
level=logging.INFO)


def main():
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    anketa = ConversationHandler(
    entry_points=[
        MessageHandler(Filters.regex('^(Анкета)$'), anketa_start)
        ], 
    states={
        'name' : [MessageHandler(Filters.text,anketa_name)],
        'year' : [MessageHandler(Filters.text,anketa_end)]},
    fallbacks=[])
    dp.add_handler(anketa)    
   # dp.add_handler(CallbackQueryHandler())
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
