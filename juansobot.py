#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
import logging

from telegram import Update, ForceReply, message
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text("Estas buscando los comandos?")
    update.message.reply_text("/comandos")

    # user = update.effective_user
    # update.message.reply_markdown_v2(
    #     fr'Hi {user.mention_markdown_v2()}\!',
    #     reply_markup=ForceReply(selective=True),
    


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def comandos(update: Update, context:CallbackContext) -> None:
    update.message.reply_text("Estas buscando los comandos?")
    update.message.reply_text("/spotify")
    update.message.reply_text("/cordoba")
    update.message.reply_text("/diciembre")
    update.message.reply_text("/misRedes")
    update.message.reply_text("/loginUnnoba")
    


def redes(update,context):
    update.message.reply_text("https://ijjhbnms22rxthljroob7w-on.drv.tw/Redes/Redes/")

def loginUnnoba(update,context):
    update.message.reply_text("https://login.unnoba.edu.ar/")




# def sumar(update,context):
#     try:
#         numero1: int(context.args[0])
#         numero2: int(context.args[1])
#         suma= numero1+numero2
#         update.message.reply_text("La suma es "+str(suma))
#     except(ValueError):
#         update.message.reply_text("Por favor utilice 2 numeros")

def spotify(update,context):
    if(update.message.text.upper().find("SPOTIFY")>0):
        update.message.reply_text("Que pasa? Andas manija? Tranqui. Juanso te la levanta con esta lista:")
        update.message.reply_text("https://open.spotify.com/playlist/0qyqZHivNRTMJPkjviAWrZ?si=4c8f5c67912447aa")
        update.message.reply_text("Dale con todo paa 🔥🔥🔥")

def diciembre(update,context):
    if(update.message.text.upper().find("DICIEMBRE")>0):
        update.message.reply_text("📚FINALES DE DICIEMBRE ")
        update.message.reply_text("📚AMB:14/12")
        update.message.reply_text("📚REDES:14/12")
        update.message.reply_text("📚SO :14/12")
        update.message.reply_text("📚IPOO:13/12")

def enero(update,context):
    if(update.message.text.upper().find("CORDOBA")>0):
        
        update.message.reply_text("Corrrdoba 2022 Papaa🔥🔥")
        update.message.reply_text("Fecha: 02/01 al 12/01🔥🔥")
        update.message.reply_text("Se vienen las Cordobesass bien perrrasss🔥🔥")
        update.message.reply_text("Te dejo un regalo asi te manijeas.  https://www.youtube.com/watch?v=1y6oCQHk0Cs")


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("2132690915:AAESDuZ7VXgKf33g17rtpaTsRc26CfxCLq4")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    # dispatcher.add_handler(CommandHandler("sumar", sumar))
    dispatcher.add_handler(CommandHandler("spotify", spotify))
    dispatcher.add_handler(CommandHandler("misRedes", redes))
    dispatcher.add_handler(CommandHandler("cordoba", enero))
    dispatcher.add_handler(CommandHandler("comandos", comandos))
    dispatcher.add_handler(CommandHandler("loginUnnoba",loginUnnoba))
    

    # on non command i.e message - echo the message on Telegram
    #dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, pizza))
    dispatcher.add_handler(CommandHandler("diciembre", diciembre))
    #dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, enero))

    # Start the Bot
    updater.start_polling()

    

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()