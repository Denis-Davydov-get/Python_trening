# Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
a = a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
def sort_list(list):
    temp = 0
    for i in range(list - 1):
        for j in range(list - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list

print(sort_list(a))
