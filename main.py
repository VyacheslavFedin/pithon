
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

updater = Updater("TOKEN")

mas = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
pc = 1

def start(update: Update, context: CallbackContext):
    global pc
    global mas
    pc=1
    mas = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    
    for i in range(len(mas)):
        update.message.reply_text(f'{mas[i][0]}          {mas[i][1]}          {mas[i][2]}')
    update.message.reply_text('игрок 1, введите номер поля (пример-"/5"):')

def game(update: Update, context: CallbackContext):
    global pc
    global mas
    if pc == 1 :
        
        msg = update.message.text
        for i in range(len(mas)):
            for i2 in range(len(mas[i])):
                if mas[i][i2] == msg[1]:
                    mas[i][i2] = 'X'
        for i in range(len(mas)):
            update.message.reply_text(f'{mas[i][0]}          {mas[i][1]}          {mas[i][2]}')
        update.message.reply_text('игрок 2, введите номер поля (пример-"/5"):')

        if mas[0][0] == 'X' and mas[0][1] == 'X' and mas[0][2] == 'X':
            update.message.reply_text('игрок 1 победил')
        elif mas[2][0] == 'X' and mas[2][1] == 'X' and mas[2][2] == 'X':
            update.message.reply_text('игрок 1 победил')
        elif mas[0][0] == 'X' and mas[1][1] == 'X' and mas[2][2] == 'X':
            update.message.reply_text('игрок 1 победил')
        elif mas[2][0] == 'X' and mas[1][1] == 'X' and mas[0][2] == 'X':
            update.message.reply_text('игрок 1 победил') 
        elif mas[0][0] == 'X' and mas[1][0] == 'X' and mas[2][0] == 'X':
            update.message.reply_text('игрок 1 победил')
        elif mas[0][1] == 'X' and mas[1][1] == 'X' and mas[2][1] == 'X':
            update.message.reply_text('игрок 1 победил')
        elif mas[0][2] == 'X' and mas[1][2] == 'X' and mas[2][2] == 'X':
            update.message.reply_text('игрок 1 победил')
        pc = 2
        
    else:
        
        msg = update.message.text
        for i in range(len(mas)):
            for i2 in range(len(mas[i])):
                if mas[i][i2] == msg[1]:
                    mas[i][i2] = 'O'
        for i in range(len(mas)):
            update.message.reply_text(f'{mas[i][0]}          {mas[i][1]}          {mas[i][2]}')
        update.message.reply_text('игрок 1, введите номер поля (пример-"/5"):')
        if mas[0][0] == 'O' and mas[0][1] == 'O' and mas[0][2] == 'O':
            update.message.reply_text('игрок 2 победил')
        elif mas[1][0] == 'O' and mas[1][1] == 'O' and mas[1][2] == 'O':
            update.message.reply_text('игрок 2 победил')
        elif mas[2][0] == 'O' and mas[2][1] == 'O' and mas[2][2] == 'O':
            update.message.reply_text('игрок 2 победил')
        elif mas[0][0] == 'O' and mas[1][1] == 'O' and mas[2][2] == 'O':
            update.message.reply_text('игрок 2 победил')
        elif mas[2][0] == 'O' and mas[1][1] == 'O' and mas[0][2] == 'O':
            update.message.reply_text('игрок 2 победил')
        elif mas[0][0] == 'O' and mas[1][0] == 'O' and mas[2][0] == 'O':
            update.message.reply_text('игрок 2 победил')
        elif mas[0][1] == 'O' and mas[1][1] == 'O' and mas[2][1] == 'O':
            update.message.reply_text('игрок 2 победил')
        elif mas[0][2] == 'O' and mas[1][2] == 'O' and mas[2][2] == 'O':
            update.message.reply_text('игрок 2 победил')
        pc = 1
        
def hello(update: Update, context: CallbackContext):
 
    update.message.reply_text('привет,это игра крестики-нолики')


updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('1', game))
updater.dispatcher.add_handler(CommandHandler('2', game))
updater.dispatcher.add_handler(CommandHandler('3', game))
updater.dispatcher.add_handler(CommandHandler('4', game))
updater.dispatcher.add_handler(CommandHandler('5', game))
updater.dispatcher.add_handler(CommandHandler('6', game))
updater.dispatcher.add_handler(CommandHandler('7', game))
updater.dispatcher.add_handler(CommandHandler('8', game))
updater.dispatcher.add_handler(CommandHandler('9', game))

updater.start_polling()
updater.idle()
