import logging
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters, ConversationHandler
import telegram
import config

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
logger = logging.getLogger()
if __name__=="__main__"
    my_bot = telegram.Bot(token=config.TOKEN)
    updater = Updater(my_bot.token)
    print(my_bot.getMe())
    dp = updater.dispatcher

REPETIR=0

def start_cback(update, context):
    update.message.reply_text("Estoy vivo")
    return 0
def repite_cback(update, context):
    update.message.reply_text("Mandame algo para repetir:")
    return REPETIR
def arepetir_cback(update, context):
    mid = update.message.from_user.id
    context.bot.send_message(
        chat_id=mid,
        parse_mode='MarkdownV2',
        text=update.message.text
    )

dp.add_handler(CommandHandler('start',start_cback))
dp.add_handler(ConversationHandler(
    entry_points=[CommandHandler('repite',repite_cback)],
    states={
        REPETIR: [MessageHandler(Filters.text, arepetir_cback)]
    },
    fallbacks=[]
))
updater.start_webhook("0.0.0.0", config.PORT, config.TOKEN, webhook_url="https://examensito-bot.herokuapp.com/" + TOKEN)
updater.idle()>>>>>>>


