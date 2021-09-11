import telebot
import requests
from boto_req_endpoint import send_message_for_inference

# {'label': 'LABEL_0', 'score': 0.9968411326408386}
LABEL_NORMAL = 'LABEL_0'
token = '1928238940:AAH6GLnnthf1yek4jX71OgH1BEtstQ8ZYmE'



bot = telebot.TeleBot(token)

toxic_count = 0
# main looppy
@bot.message_handler(content_types="text")
def phu(message):

    global toxic_count

    words = message.text

    is_toxic_msg = is_toxic(send_message_for_inference(words))
    if is_toxic_msg:
        toxic_count += 1

    if toxic_count > 0:
        bot.send_message(message.chat.id, words + str(is_toxic_msg))
        bot.send_animation(message.chat.id, 'https://i.giphy.com/media/l1J9NRpOeS7i54xnW/giphy.webp')
        toxic_count = 0
    # bot.send_message(message.chat.id, response.text)
    # bot.forward_message('558800780', message.chat.id, message.message_id)


def is_toxic(results):
    item = results[-1]
    sentiment = item.get('label', LABEL_NORMAL)
    return sentiment != LABEL_NORMAL

if __name__ == "__main__":
    bot.polling(none_stop=True)
