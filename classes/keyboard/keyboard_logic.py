from telebot import types


def create_data(keyboard, data):
    for item in data:
        keyboard.buttons.append(types.InlineKeyboardButton(text=item, callback_data=data[item]))

    for button in keyboard.buttons:
        keyboard.add(button)


def start(keyboard):
    data = {'Заказать кальянчик': 'order_yes',
            'Посмотреть миксы': 'mixes'}

    create_data(keyboard, data)


def taste(keyboard):
    data = {'Фрукты': 'fruits',
            'Ягоды': 'berries'}

    create_data(keyboard, data)


def strong(keyboard):
    data = {'Послабже': 'low',
            'Средний': 'medium',
            'Покрепче': 'strong'}

    create_data(keyboard, data)


def frosty(keyboard):
    data = {'Да': 'yes',
            'Нет': 'no'}

    create_data(keyboard, data)
