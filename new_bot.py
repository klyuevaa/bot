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
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    
    anketa = ConversationHandler(
    entry_points=[
        CallbackQueryHandler(anketa_start, pattern="111")
        ], 
    states={
        'name' : [MessageHandler(Filters.text,anketa_name)],
        'year' : [MessageHandler(Filters.text,anketa_end)]},
    fallbacks=[])

    dp.add_handler(anketa)
    dp.add_handler(CallbackQueryHandler(send_weather, pattern="222"))    
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()



# Вызываем функцию main() - именно эта строчка запускает бота
if __name__ == "__main__":
    main()
