import os
from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Updater


load_dotenv()
secret_token = os.getenv('TOKEN')
