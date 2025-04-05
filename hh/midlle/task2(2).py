# Нужно отсортировать кандидатов по набранному баллу за этот этап и выявить всех,
# чей средний балл выше пяти. Каждого кандидата оценил минимум один менеджер и HR по десятибалльной шкале,
# оценка участника — среднее от полученных баллов.
# Формат ввода
# От 2 до 100 строк.
# Каждая строка содержит фамилию кандидата, несколько оценок от менеджеров и HR.
# Число оценок может варьироваться, но их не менее двух.
# Фамилия и оценки разделены запятой, без пробелов. Гарантируется, что фамилии уникальны.
# Формат вывода
# Отсортированный рейтинг кандидатов, у которых средний балл за интервью — 5 и выше.
# В начале списка кандидат с самым высоким средним баллом, в конце — с самым низким.
# Если средняя оценка совпадает у нескольких кандидатов, расположите их относительно друг друга в алфавитном порядке.
# В одной строке — фамилия кандидата и его средний балл, разделенные запятой без пробела.
# Округлите средние оценки до десятых, выводите их с одной цифрой после точки
# (в том числе целые числа, например, «1.0»). Если никто не набрал 5 баллов и выше, выведите «Никто».
# Пример 1
# Входные данные:
# Ivanov, 5, 6, 7, 8
# Lisii, 9, 8, 10, 9
# Sokolova, 5, 6, 8, 5
# Tritonov, 7, 2, 3, 4
# Chernov, 8, 8, 8, 8
# Svetova, 4, 5, 3, 6
# Zayatz, 5, 5, 5, 5
# Rezhik, 6, 6, 6, 6


# Выходные данные:
# Lisii,9.0
# Chernov,8.0
# Ivanov,6.5
# Rezhik,6.0
# Sokolova,6.0
# Zayatz,5.0
# Пример 2
# Входные данные:
# Ivanov,4,3,2,1
# Lisii,2,2,3,1
# Sokolova,3,4,2,1
# Tritonov,1,1,2,1
# Выходные данные:
# Никто

def select_candidates(candidate_strings: list) -> list:
    std_dict = {}
    list_save = []
    count = 0
    for candidates in candidate_strings:  # перебираем все строки в листе
        candidate = candidates.split(", ")
        for i in candidate[1:]:
            count += int(i) # Суммирование оценок
        count /= len(candidate[1:]) # Среднее значение
        if count >= 5:
            list_save.append(f'{candidate[0]}, {count}')
    return list_save

lines = []
while True:
    try:
        line = input()
        if line == "":
            break
    except EOFError:
        break
    lines.append(line)

for candidate in select_candidates(lines):
    print(candidate)
