import telebot
from PIL import Image
import os
from dotenv import load_dotenv
load_dotenv()


API_KEY = os.environ['API_KEY']

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start', 'help'])
def greet(message): 
    bot.reply_to(message, 'Hey, how is it going.?')


@bot.message_handler(commands=['hello'])
def hello(message):
    bot.send_message(message.chat.id, 'Hello')
   


@bot.message_handler(content_types=['photo'])
def handle_docs_audio(message):
    # img = Image.open("message")
    # img.convert("1").save("result.jpg")
    # bot.sendPhoto(message.chat.id, photo=open('img', 'rb'))
    bot.send_message(message.chat.id, 'Hello')
bot.polling()




