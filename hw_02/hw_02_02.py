from collections import deque
import re

def is_palindrome(input_string):
    # Видалення пробілів та перетворення рядка до нижнього регістру
    text= input_string.lower().replace(" ", "")
    formatted_string = re.sub("[^\w\s]", "", text).lower()

    # Створення двосторонньої черги з символів тексту
    char_deque = deque(formatted_string)

    # Перевірка символів з обох кінців черги
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

    return True

# Перевірка
phrases = ["Сам ти паліндром",
           "Уму – мінімуму",
           "123454321",
           "привіт",
           "А баба на волі — цілована баба"]

for phrase in phrases:
    print(f"{phrase}: {is_palindrome(phrase)}")

