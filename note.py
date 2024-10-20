def sum_stydent(stydents:str)-> str:
    stydents_list = stydents.split(',')
    return sum(stydents_list)

text = input("Введите фамишию и оценки студента через запятную: ")
print(sum_stydent(text))