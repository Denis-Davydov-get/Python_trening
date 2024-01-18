def matrix(opration, rows=6, colums=6):
        list_matrix = [opration(i, j) for j in range(1, colums + 1) for i in range(1, rows + 1)]
        print(list_matrix)



rows = int(input("Введите количество строк: "))
colums = int(input("Введите количество колонок: "))
matrix(lambda x: x*x, rows, colums)
