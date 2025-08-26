# Удалить первые символы строки python
# Напишите программу, которая удаляет первые n символов из строки, и верните новую строку


def remove_str(text:str, count_sim:int)->str:
    if len(text) <= 0 or len(text) <= count_sim:
        return f"Количество символов больше или меньше длины строки, количество символов строки {len(text)}"
    else:
        return text[count_sim:]

text = 'Удалить первые символы строки python'
count_sim = 5
print(remove_str(text, count_sim))