import telebot;
bot = telebot.TeleBot('5345054662:AAHjmzzNwUXRShqykpUy9rJ1cFnFzLktsTk')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):





bot.polling(none_stop=True, interval=0)