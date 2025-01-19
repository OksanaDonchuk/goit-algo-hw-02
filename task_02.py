from collections import deque
from typing import List

def is_palindrome(input_str: str) -> str:
    """
    Перевіряє, чи є заданий рядок паліндромом.
    
    Аргументи:
    input_str (str): Вхідний рядок, який потрібно перевірити.
    
    Повертає:
    str: Повідомлення, чи є рядок паліндромом.
    """
    # Приведення рядка до нижнього регістру та видалення пробілів
    normalized_str = ''.join(input_str.lower().split())

    # Створення двосторонньої черги з символів рядка
    char_deque = deque(normalized_str)

    # Порівняння символів з початку та кінця черги
    while len(char_deque) > 1:
        # Порівнюємо символи на обох кінцях
        if char_deque.popleft() != char_deque.pop():
            return f"'{input_str}': Це не паліндром"

    return f"'{input_str}': Це паліндром"


# Тестування функції
test_words: List[str] = [
    "Hello world",
    "Madam",
    "Solos",
    "Level",     
    "Niagara o roar again",
    "Python",
]

for test in test_words:
    print(is_palindrome(test))