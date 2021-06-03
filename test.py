"""Тренажёр для изучения английского языка"""

import random
import tkinter as tk

""""Словарь русских предложений"""
russian = {1: 'Я буду любить?', 2: 'Ты будешь любить?', 3: 'Мы будем любить?', 4: 'Они будут любить?',
           5: 'Он будет любить?', 6: 'Она будет любить?',
           7: 'Я любил?', 8: 'Ты любил?', 9: 'Мы любили?', 10: 'Я люблю?', 11: 'Ты любишь?', 12: 'Мы любим?',
           13: 'Они любят?', 14: 'Он любит?', 15: 'Она любит?', 16: 'Они любили?', 17: 'Он любил?', 18: 'Она любила?',
           19: 'Я буду любить.', 20: 'Мы будем любить.', 21: 'Ты будешь любить.', 22: 'Мы будем любить.',
           23: 'Он будет любить.', 24: 'Она будет любить.',
           25: 'Я люблю.', 26: 'Ты любишь.', 27: 'Мы любим.', 28: 'Они любят.', 29: 'Он любит.', 30: 'Она любит.',
           31: 'Я любил.', 32: 'Ты любил.', 33: 'Мы любили.', 34: 'Они любили.', 35: 'Он любил.', 36: 'Она любила.',
           37: 'Я не буду любить.', 38: 'Мы не будем любить.', 39: 'Ты не будешь любить.', 40: 'Они не будут любить.',
           41: 'Он не будет любить.', 42: 'Она не будет любить.',
           43: 'Я не люблю.', 44: 'Ты не любишь.', 45: 'Мы не любим.', 46: 'Они не любят.', 47: 'Он не любит.',
           48: 'Она не любит.',
           49: 'Я не любил.', 50: 'Ты не любил.', 51: 'Мы не любили.', 52: 'Они не любили.', 53: 'Он не любил.',
           54: 'Она не любила.'}

"""Словарь английских предложений"""
english = {1: 'Will i love?', 2: 'Will you love?', 3: 'Will we love?', 4: 'Will they love?', 5: 'Will he love?',
           6: 'Will she love?',
           7: 'Do i love?', 8: 'Do you love?', 9: 'Do we love?', 10: 'Do they love?', 11: 'Does he love?',
           12: 'Does she love?',
           13: 'Did i love?', 14: 'Did you love?', 15: 'Did we love?', 16: 'Did they love?', 17: 'Did he love?',
           18: 'Did she love?',
           19: 'I will love.', 20: 'You will love.', 21: 'We will love.', 22: 'They will love.', 23: 'He will love.',
           24: 'She will love.',
           25: 'I love.', 26: 'You love.', 27: 'We love.', 28: 'They love.', 29: 'He loves.', 30: 'She loves.',
           31: 'I loved.', 32: 'You loved.', 33: 'We loved.', 34: 'They loved.', 35: 'He loved.', 36: 'She loved.',
           37: 'I will not love.', 38: 'You will not love.', 39: 'We will not love.', 40: 'They will not love.',
           41: 'He will not love.', 42: 'She will not love.',
           43: 'I don`t love.', 44: 'You don`t love.', 45: 'We don`t love.', 46: 'They don`t love.',
           47: 'He does not love.', 48: 'She does not love.',
           49: 'I did not love.', 50: 'You did not love.', 51: 'We did not love.', 52: 'They did not love.',
           53: 'He did not love.', 54: 'She did not love.'}

language = {}

"""Функция выбора языка"""


def add_operation(operation):
    global language
    if operation == 'Russian':
        language = russian
    else:
        language = english
    next_()


"""Функция переключения предложений"""


def next_():
    global language
    if language != {}:
        text.delete(0, tk.END)
        value = language.get(random.randint(1, 54))
        text.insert(0, value)


"""Функция кнопки выбора языка"""


def make_operation_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red', command=lambda: add_operation(operation))


"""Функция кнопки переключения предложений"""


def make_next_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red', command=lambda: next_())


"""создание окна"""
win = tk.Tk()
win.geometry("600x130+100+200")
win.title("Изучение английского языка")
win['bg'] = "#33ffe6"

"""задаём минимальный размер колонок"""
win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=100)
win.grid_columnconfigure(2, minsize=100)
win.grid_columnconfigure(3, minsize=300)

"""задаём минимальный размер строк"""
win.grid_rowconfigure(0, minsize=60)
win.grid_rowconfigure(1, minsize=60)

"""определение работы экрана """
text = tk.Entry(win, font=('Arial', 20), width=15)  # вывод строки на экран .
text.grid(row=0, column=0, columnspan=4, stick='we', padx=5)
text.insert(0, 'Выберите язык')

"""задаём параметры кнопок"""
make_operation_button('Russian').grid(row=1, column=0, stick='wens', padx=5, pady=5)
make_operation_button('English').grid(row=1, column=1, stick='wens', padx=5, pady=5)
make_next_button('Next sentence').grid(row=1, column=2, stick='wens', padx=5, pady=5)

win.mainloop()
