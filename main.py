import logging
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters, ConversationHandler
import telegram
from config import TOKEN, PORT

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger()

if __name__ == "__main__":
    # TOKEN=""
    my_bot = telegram.Bot(token=TOKEN)
    updater = Updater(my_bot.token)
    print(my_bot.getMe())


REPETIR = 0


def start_callback(update, context):
    update.message.reply_text("Estoy probandome ...4")
    return 0


def repite_callback(update, context):
    update.message.reply_text("Mandame algo para repetir:")
    return REPETIR


def arepetir_callback(update, context):
    mid = update.message.from_user.id
    context.bot.send_message(
        chat_id=mid,
        parse_mode='MarkdownV2',
        text=update.message.text,
    )

dp = updater.dispatcher
dp.add_handler(CommandHandler('start', start_callback))
dp.add_handler(ConversationHandler(
    entry_points=[CommandHandler('repite', repite_callback)],
    states={
        REPETIR: [MessageHandler(Filters.text, arepetir_callback)]
    },
    fallbacks=[]
))
updater.start_webhook("0.0.0.0", PORT, TOKEN, webhook_url="https://examensitobot.herokuapp.com/" + TOKEN)
# updater.start_polling()
updater.idle()