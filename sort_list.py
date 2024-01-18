# Отсортируйте словарь по значению в порядке возрастания и убывания.
a = [1, 15, 2, 10, 5, 88, 13, 21, 34, 55, 89]

def sort_min(list):
    for i in range(len(list)-1):
        if list[i] < list[i + 1]:
            list[i] = list[i+1]
    return list
# def sort_max(list):
#     temp = 0
#     for i in range(len(list) - 1):
#         if list[i] > list[i + 1]:
#             list[i] = list[i + 1]
#     return list
print(sort_min(a))
# print(sort_max(a))
