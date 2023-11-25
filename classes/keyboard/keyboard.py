from classes.keyboard.keyboard_logic import *


class Keyboard(types.InlineKeyboardMarkup):
    def __init__(self, type_):
        super().__init__()
        self.buttons = []

        if type_ == 'start':
            start(self)
        if type_ == 'taste':
            taste(self)
        if type_ == 'strong':
            strong(self)
        if type_ == 'frosty':
            frosty(self)

