import telebot
from classes.order.order import Order
from classes.keyboard.keyboard import Keyboard

bot = telebot.TeleBot('6933355922:AAEA4136OyARlJV2UnT4W1G_EiD1CfljoHs')

kwargs = {}

@bot.message_handler(commands=['start'])
def get_text_messages(message):
    keyboard = Keyboard('start')
    bot.send_message(message.chat.id, text="Привет, чем я могу тебе помочь?", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def order(call):
    global kwargs

    if call.data == 'order_yes':
        kwargs = {'order': Order()}
        keyboard = Keyboard('taste')
        bot.send_message(call.message.chat.id, "Давай определимся по вкусу", reply_markup=keyboard)

    if call.data in ('fruits', 'berries'):
        kwargs['order'].taste = call.data
        keyboard = Keyboard('strong')
        bot.send_message(call.message.chat.id, "Давай определимся по крепости", reply_markup=keyboard)

    if call.data in ('low', 'medium', 'strong'):
        kwargs['order'].strong = call.data
        keyboard = Keyboard('frosty')
        bot.send_message(call.message.chat.id, "Давай определимся по холодку", reply_markup=keyboard)

    if call.data in ('yes', 'no'):
        kwargs['order'].frosty = call.data
        bot.send_message(call.message.chat.id, str(kwargs['order']))
        kwargs = {}




bot.polling(none_stop=True, interval=0)
