import telebot

bot = telebot.TeleBot('6979410035:AAHqM9ARr0f9UCmMk8DLEi2H9wM-A-D3ni0')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send.message(message.chat.id,
                     'Привет, это мой первый бот, поэтому не суди строго. Если хочешь, чтобы я рассказал тебе анекдот, напиши мне /anekdot. Если хочешь узнать где я сделал этого бота, напиши мне /link.')


@bot.message_handler(commands=['anekdot'])
def main(message):
    bot.send.message(message.chat.id,
                     '- Здравствуйте, а вы кем работаете? /n- Здравствуйте, я аудитор /n- Я тогда бмвтор')


@bot.message_handler(commands=['link'])
def main(message):
    bot.send.message(message.chat.id,
                     'Я смотрю, тебе интересно где я сделал этого крутого бота. Держи тогда ссылку на сайт. [Нажми на меня](https://pastebin.com)')


bot.infinity_polling()