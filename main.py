import random
import re
import telebot
import requests
from boto_req_endpoint import send_message_for_inference


# {'label': 'LABEL_0', 'score': 0.9968411326408386}
LABEL_NORMAL = 'LABEL_0'
normal_labels = ['LABEL_0', 'LABEL_18']
flirt_labels = ['LABEL_5', 'LABEL_6']
token = '1928238940:AAH6GLnnthf1yek4jX71OgH1BEtstQ8ZYmE'

img_for_reaction = ['https://media1.giphy.com/media/JdSUpdPV4iPxm84oJF/giphy.gif?cid=790b7611898a73b8ab209b363288b65927bdd4d15c75f3d1&rid=giphy.gif&ct=g',
                    'https://media3.giphy.com/media/vLPPebBAjmsFr2Tgob/giphy.gif?cid=790b7611b5fac8ddff08370d3618a51a6b9e4e38027cd537&rid=giphy.gif&ct=g',
                    'https://media1.giphy.com/media/JdSUpdPV4iPxm84oJF/giphy.gif?cid=790b7611898a73b8ab209b363288b65927bdd4d15c75f3d1&rid=giphy.gif&ct=g']

img_for_flirt = ['https://media3.giphy.com/media/RHrnUvQcIfgj6FAFiO/giphy.gif?cid=790b7611735d8b11bca24306f8268049522739a10c56d3bc&rid=giphy.gif&ct=g',
                 'https://media0.giphy.com/media/3SiLCCMCw0DLTdpdxQ/giphy.gif?cid=790b761120c548ec105bd6555ae1726682c9a3e1cf5867fb&rid=giphy.gif&ct=g',
                 'https://media1.giphy.com/media/VZHVRHe1L5l6dhD7l5/giphy.gif?cid=790b7611c910b52819dc368ad5d7265d993309ebd2b5ac6a&rid=giphy.gif&ct=g'
                 ]

bot = telebot.TeleBot(token)

# main looppy
@bot.message_handler(content_types="text")
def phu(message):

    words = message.text
    words = re.sub("[^а-яА-Я ]+", "", words).strip()
    is_toxic_msg = is_toxic(send_message_for_inference(words))
    print(words)
    print(is_toxic_msg)
    if is_toxic_msg:
        img_indx = random.randint(0,len(img_for_reaction) - 1)
        bot.send_message(message.chat.id, '@Wild314HackSuperRes_bot says:')
        bot.send_message(message.chat.id, '🤮')
        bot.send_animation(message.chat.id, img_for_reaction[img_indx])



def is_toxic(results):
    item = results[-1]
    sentiment = item.get('label', LABEL_NORMAL)
    print(sentiment)
    return sentiment not in normal_labels

def is_toxic(results):
    item = results[-1]
    sentiment = item.get('label', LABEL_NORMAL)
    print(sentiment)
    return sentiment not in normal_labels


if __name__ == "__main__":
    bot.polling(none_stop=True)
