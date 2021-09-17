import random
import re
import telebot
import requests
from boto_req_endpoint import send_message_for_inference

LABEL_NORMAL = 'LABEL_0'
normal_labels = ['LABEL_0', 'LABEL_18']
flirt_labels = ['LABEL_5', 'LABEL_6', 'LABEL_11', 'LABEL_78']
token = '<token>'

img_for_reaction = [
    'https://media4.giphy.com/media/u7VvSQke5wsIiUlRdE/giphy.gif?cid=790b7611b7a75294d0c2e418626fecb46f264c1c0ea66f00&rid=giphy.gif&ct=g',
    'https://media3.giphy.com/media/2fW7VB8VeHEoVIPjWB/giphy.gif?cid=790b7611ca4a6b3e3294ce46476b42f761c781e084daf732&rid=giphy.gif&ct=g',
    'https://media0.giphy.com/media/ldNBX4gB2e6cypIebh/giphy.gif?cid=790b7611a2c20af2f401ed8375de462e826734766a9adca0&rid=giphy.gif&ct=g',
    'https://media1.giphy.com/media/JdSUpdPV4iPxm84oJF/giphy.gif?cid=790b7611898a73b8ab209b363288b65927bdd4d15c75f3d1&rid=giphy.gif&ct=g'
]

img_for_flirt = [
    'https://media4.giphy.com/media/KmWnPq5c5CSIH9zkEU/giphy.gif?cid=790b7611ebe389d49b5dfd4c1bd3410f5d72485a7f77b4bb&rid=giphy.gif&ct=g',
    'https://media3.giphy.com/media/JxJjfVsRypMUvI0xKQ/giphy.gif?cid=790b761124f2b512c4a77850466a557bc4da80d2dd151feb&rid=giphy.gif&ct=g',
    'https://media3.giphy.com/media/wCnzMKw34Mc0A1tvuv/giphy.gif?cid=790b76117ff5fc5988e93b8c5846c9f8d79f898bb35107ae&rid=giphy.gif&ct=g',
    'https://media0.giphy.com/media/3SiLCCMCw0DLTdpdxQ/giphy.gif?cid=790b761120c548ec105bd6555ae1726682c9a3e1cf5867fb&rid=giphy.gif&ct=g'
    ]

bot = telebot.TeleBot(token)


# main looppy
@bot.message_handler(content_types="text")
def phu(message):
    words = message.text
    words = re.sub("[^а-яА-Я ]+", "", words).strip()
    inf_res = send_message_for_inference(words)
    is_toxic_msg = is_toxic(inf_res)
    is_flirt_msg = is_flirt(inf_res)
    print(words)
    print(is_toxic_msg)

    is_hot_gf_chat = message.chat.title == 'Hot Girlfriend'

    if is_hot_gf_chat and is_flirt_msg:
        img_indx = random.randint(0, len(img_for_flirt) - 1)
        bot.send_message(message.chat.id, '@Wild314HackSuperRes_bot says:')
        bot.send_message(message.chat.id, '❤️')
        bot.send_animation(message.chat.id, img_for_flirt[img_indx])
    elif is_toxic_msg:
        img_indx = random.randint(0, len(img_for_reaction) - 1)
        bot.send_message(message.chat.id, '@Wild314HackSuperRes_bot says:')
        bot.send_message(message.chat.id, '🙉🛑🤬')
        bot.send_animation(message.chat.id, img_for_reaction[img_indx])


def is_toxic(results):
    item = results[-1]
    sentiment = item.get('label', LABEL_NORMAL)
    print(sentiment)
    return sentiment not in normal_labels


def is_flirt(results):
    item = results[-1]
    sentiment = item.get('label', LABEL_NORMAL)
    return sentiment in flirt_labels


if __name__ == "__main__":
    bot.polling(none_stop=True)
