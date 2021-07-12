from telegram import ReplyKeyboardMarkup
from telegram import Update
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from covid19 import Covid19

buttons = ReplyKeyboardMarkup([['Statistka'], ['Dunyo']], resize_keyboard=True)
covid = Covid19()
def start(update, context):
    update.message.reply_text(
        'Assalom aleykum {}'.format(update.message.from_user.first_name), reply_markup=buttons)
    return 1
def status(update, context):

    data = covid.getByCountryCode('UZ')
    print(data)
    update.message.reply_html(
        '<b>Yuqtirganlar:</b> {}\n<b>Sogayganlar:</b> {}\n<b>Vafot etganlar:</b> {}'.format(
            5,
            3,
            3
        ),
        reply_markup=buttons
    )
def world(update, context):
    update.message.reply_text(
        'Dunyo belgilandi', reply_markup=buttons
    )
updater = Updater('1854074920:AAHlkvTYzL-l8YwhqLAbW8pGGjW_8CqGs3M', use_context=True)
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
      1:[
            MessageHandler(Filters.regex('^(Statistka)$'), status),
            MessageHandler(Filters.regex('^(Dunyo)$'), world),
        ]
    },
    fallbacks=[MessageHandler(Filters.text, start)]
)

updater.dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()