text = '''Иванов Иван Иванович
Петров Иван Петрович
Сидоров Петр Сидорович
Васильев Василий Васильевич
Смирнов Сергей Сергеевич
Кузнецов Кузьма Кузьмич
Соколов Сергей Сергеевич
Новиков Николай Николаевич'''


def pop_evr_family(fio: str) -> list:
    list_fio = fio.split('\n')  # сплитованный список фио
    list_f = [x.split()[0] for x in list_fio]  # Список фамилиями
    list_len_f = [float(len(i)) for i in list_f]  # Список с количеством символов в фамилии
    avg_fio = sum(list_len_f) / len(list_len_f)  # ср. значение символов
    new_list = [list_fio.pop(list_f.index(item)) for item in list_f if len(item) < avg_fio]
    return new_list


print(pop_evr_family(text))
# print(text)
