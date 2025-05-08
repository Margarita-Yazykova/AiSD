import os
digit_to_word = {'0': 'ноль', '1': 'один','2': 'два','3': 'три','4': 'четыре','5': 'пять','6': 'шесть','7': 'семь'}
def proverka_8_digits(word):
    if not word or len(word) > 3 or not all(c in '01234567' for c in word):
        return False
    if word[0] in '0246' and int(word) % 2 == 0:
        return True
def obrabotka_8_numbers(filename):
    if not os.path.exists(filename):
        print("Файл не найден.")
        return
    with open(filename, "r", encoding="utf-8") as file:
        for strok in file:
            words = strok.split()
            for word in words:
                if proverka_8_digits(word):
                    min_digit, max_digit = min(word), max(word)
                    print(f"Число: {word} --- минимальная цифра: {digit_to_word[min_digit]}, максимальная цифра: {digit_to_word[max_digit]}")
filename = os.path.join(os.path.expanduser("~"),"Desktop", "input.txt")
obrabotka_8_numbers(filename)