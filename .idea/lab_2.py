import os
import re
# Словарь для преобразования цифр в их прописное представление
digit_to_word = {
    '0': 'ноль',
    '1': 'один',
    '2': 'два',
    '3': 'три',
    '4': 'четыре',
    '5': 'пять',
    '6': 'шесть',
    '7': 'семь'
                }
# Регулярное выражение для допустимых чисел
regular = re.compile(r'^([0246]|[0246][0246]|[0246][0-7][0246])$')

def proverka_8_digits(word):  # Функция проверки числа на натуральное, чётное, восьмиричное число, которое начинается на чётную цифру
    return regular.match(word)

def obrabotka_8_numbers(filename):
    if not os.path.exists(filename):
        print("Файл не найден")
        return

    with open(filename, "r", encoding="utf-8") as file: #"r" параметр чтения
        for strok in file:
            words = strok.split()
            for word in words:
                if proverka_8_digits(word):
                    min_digit, max_digit = min(word), max(word)
                    print(f"Число: {word} --- минимальная цифра: {digit_to_word[min_digit]}, максимальная цифра: {digit_to_word[max_digit]}")

filename = os.path.join(os.path.expanduser("~"), "Desktop", "input.txt")
obrabotka_8_numbers(filename)