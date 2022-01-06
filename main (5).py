 from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
import requests
import re
import logging
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

#enabling logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
                    
logger = logging.getLogger(__name__)

def start(update, context):
    user = update.message.from_user
    logger.info(user.first_name, update.message.text)
    update.message.reply_text('Hi {}, Here is Pratiksha to help you. I hold conversation with you here. '
                              'Here are command list you can use. '
                              'Send /about , /passion , /education , /sport , /hobby , /cancel '.format(update.message.from_user.first_name), reply_markup=ReplyKeyboardRemove())
    
    print(logger.info)
    
def about(update, context):
    user = update.message.from_user
    logger.info(user.first_name, update.message.text)
    update.message.reply_text('<Enter here details> .'
                              'To know more send /passion , /education , /sport , /hobby . '
                              'If want to stop send /cancel', reply_markup=ReplyKeyboardRemove())
    
def passion(update, context):
    user = update.message.from_user
    logger.info(user.first_name, update.message.text)
    update.message.reply_text('<Enter here details>. '
                              'To know more send /education , /sport , /hobby . '
                              'If want to stop send /cancel', reply_markup=ReplyKeyboardRemove())

def education(update, context):
    user = update.message.from_user
    logger.info(user.first_name, update.message.text)
    update.message.reply_text('<Enter here details>. '
                              'To know more send /sport , /hobby . '
                              'If want to stop send /cancel', reply_markup=ReplyKeyboardRemove())

def sport(update, context):
    user = update.message.from_user
    logger.info(user.first_name, update.message.text)
    update.message.reply_text('<Enter here details>. '
                              'To know more send /hobby . '
                              'If want to stop send /cancel', reply_markup=ReplyKeyboardRemove())

def hobby(update, context):
    user = update.message.from_user
    logger.info(user.first_name, update.message.text)
    update.message.reply_text('<Enter here details>. '
                              'Thank for chatting with me, see you soon!', reply_markup=ReplyKeyboardRemove())

def cancel(update, context):
    user = update.message.from_user
    logger.info("User %s canceled the conversation. ", user.first_name)
    update.message.reply_text('Bye! I hope we can talk again some day.', reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

def main() -> object:

    updater = Updater('HTTP token ID', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('about', about))
    dp.add_handler(CommandHandler('passion', passion))
    dp.add_handler(CommandHandler('education', education))
    dp.add_handler(CommandHandler('sport', sport))
    dp.add_handler(CommandHandler('hobby', hobby))
    dp.add_handler(CommandHandler('cancel', cancel))
    
    #Starting the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()