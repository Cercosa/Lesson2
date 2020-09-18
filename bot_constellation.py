import ephem
from datetime import datetime
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(filename = "bot.log", level = logging.INFO)

def greet_user(update, context):
    print("Called / start")
    print(update)
    update.message.reply_text("Hello User!")

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def constellation(update, context):
    
    user_text = update.message.text.split(' ') 
    print(user_text)
    planet = user_text[1]
    if planet == 'Mercury':
        planet = ephem.Mercury(datetime.now())
        constellation = ephem.constellation(planet)

    elif planet == "Mars":
        planet = ephem.Mars(datetime.now())
        constellation = ephem.constellation(planet)

    else:
        update.message.reply_text("Wrong planet name")
  
    update.message.reply_text(constellation)
    

def main():
    mybot = Updater(settings.API_KEY, use_context = True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start",greet_user))
    dp.add_handler(CommandHandler("planet", constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Bot is started")
    mybot.start_polling()
    mybot.idle()

    

if __name__ == "__main__":
    main()