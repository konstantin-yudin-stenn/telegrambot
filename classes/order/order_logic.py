questions = [
    {"taste": "Выберите вкус:", "options": ["Фрукты", "Ягоды"]},
    {"strong": "Выберите крепость:", "options": ["Слабая", "Средняя", 'Сильная']},
    {"frosty": "Выберите холод:", "options": ["Да", "Нет"]}
]

class OrderFlow:
    def __init__(self, questions):
        self.order = Order()
        self.questions = questions
        self.current_question_index = 0

    def send_next_question(self, chat_id):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            message_text = f"{question['taste']}\n"
            options = question['options']
            keyboard = Keyboard(options)
            bot.send_message(chat_id, message_text, reply_markup=keyboard)
            self.current_question_index += 1
        else:
            # Все вопросы заданы, завершаем процесс
            bot.send_message(chat_id, str(self.order))
            self.current_question_index = 0  # Сбрасываем состояние

order_flow = OrderFlow(questions)

@bot.callback_query_handler(func=lambda call: True)
def order(call):
    current_question_index = order_flow.current_question_index

    if current_question_index < len(questions):
        # Обработка ответа на текущий вопрос
        question = questions[current_question_index]
        answer = call.data
        setattr(order_flow.order, question['taste'], answer)

        # Отправляем следующий вопрос
        order_flow.send_next_question(call.message.chat.id)