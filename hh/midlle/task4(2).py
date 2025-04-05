# Вы разрабатываете модуль для обработки текстовых данных.
# Вам необходимо извлечь из текста список всех уникальных email-адресов.
# Email-адрес считается допустимым, если он:
# Содержит только латинские буквы (в любом регистре) string.isalpha(),
# цифры isdigit(), символы «.», «-» и «_»; [",", "-", "_", "@"]
# Начинается с буквы или цифры;
# Содержит один символ «@»;
# Завершается одним из следующих способов: .ru, .com, .org или .net   str.endswith("Geeks")
# Формат ввода
# Одна строка текста произвольной длины до 1000 символов.
# Формат вывода
# Если найдены email-адреса, каждый найденный адрес выводится на отдельной строке.
# Если адресов не найдено, выводится «Не найдено».
# Пример 1
# Входные данные:
# Это текст с email user123@example.com и user456@mail.ru, но не example.com
# Выходные данные:
# user123@example.com
# user456@mail.ru
# Пример 2
# Входные данные:
# Это пример текста с невалидными адресами: user@, @domain.com
# Выходные данные:
# Не найдено

import re, doctest


class TextProcessor:
    def __init__(self, text):
        self.text = text  # need to .lower to tell input data one register

    def extract_emails(self):
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, self.text):
            return self.text
        else:
            return "Не найдено"


# input_text = input()
test_list = ["user123@example.com",
             "user456@mail.ru",
             "user@",
             "@domain.com"]
for text in test_list:
    text1 = TextProcessor(text)
    print(text1.extract_emails())
