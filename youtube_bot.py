import telebot
from pytube import YouTube
import os
import datetime

# url = input("скинь ссылку на видео из YOUTUBE: ")
# YouTube(url).streams.first().download()
# vid = YouTube(url).streams.get_by_resolution('vid')
# # video = YouTube(url)

# print(datetime.datetime.now())
current_path = os.path.abspath(os.getcwd())
token = "2028164755:AAE4_dk8TWO-QWuArg6SsLZhEu0hYuwAUkE"
bot = telebot.TeleBot(token)

@bot.message_handler(commands= ["start", "старт"])
def start_messsage(message):
    username = message.from_user.first_name
    ness = 'Приветствуем вас ' + username + ' отправьте мне ссылку на видео из  YouTube и я вам его скачаю'
    bot.send_message(message.chat.id, ness)


@bot.message_handler(content_types='text')
def downloader(message):
    url_from_youtube = message.text
    down_path = current_path+'/videos/'
    filename = str(datetime.datetime.now())
    yout = YouTube(url_from_youtube)
    bot.send_message(message.chat.id, 'падажжи пчел...')
    YouTube(url_from_youtube).streams.filter(res="720p").first().download(filename = filename, output_path=down_path)
    path_url = down_path+filename
    bot.send_message(message.chat.id, 'готово')
    vid = open(path_url, 'rb')
    bot.send_video(message.chat.id, vid)

print('bot is working')
bot.infinity_polling()
