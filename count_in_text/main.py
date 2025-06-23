from collections import Counter
import re


def find_most_common_word(text):
    """
    Функция находит самое часто встречающееся слово в тексте

    Параметры:
    text (str) - входной текст

    Возвращает:
    tuple - кортеж с самым частым словом и количеством его повторений
    """
    # Приводим текст к нижнему регистру
    text = text.lower()

    # Очищаем текст от знаков препинания и спецсимволов
    # Оставляем только буквы и цифры
    cleaned_text = re.sub(r'[^\w\s]', '', text)

    # Разбиваем текст на слова
    words = cleaned_text.split()

    # Подсчитываем частоту каждого слова
    word_counts = Counter(words)

    # Находим самое частое слово
    most_common = word_counts.most_common(1)

    return most_common[0] if most_common else None


# Пример использования

text = (open("text.txt").read()
        .replace(" и ", "")
        .replace(" в ", "")
        )
result = find_most_common_word(text)
print(f"Самое частое слово: '{result[0]}' (встречается {result[1]} раз/a)")
