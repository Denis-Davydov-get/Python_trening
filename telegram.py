import telebot
bot = telebot.TeleBot('5345054662:AAHjmzzNwUXRShqykpUy9rJ1cFnFzLktsTk')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Здравствуйте, спасибо за интерес к компании "Caprigo".  Чем можем помочь? ')
@bot.message_handler(content_types=['text', 'document', 'audio'])
def send_message(message):
    bot.send_message(message.chat.id,'Мы передали ваше сообщение, с Вами свяжется первый освободившийся менеджер.')
bot.polling(none_stop=True, interval=0)