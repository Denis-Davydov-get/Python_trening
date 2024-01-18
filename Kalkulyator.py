import random
pravilno = 0
nepravilno = 0
while nepravilno < 5 and pravilno < 5:
	pervoe = random.randint(1, 100)
	vtoroe = random.randint(1, 100)
	summa = pervoe + vtoroe
	print(f'Сколько будет?:', pervoe, '+', vtoroe)
	otvet = int(input())
	if summa == otvet:
		pravilno += 1
		print(f'Правильно')
		print(f'Правильно: ', pravilno, "Неправильно: ", nepravilno)
	else:
		nepravilno += 1
		print(f'Неправильно, будет', summa)
		print(f'Правильно: ', pravilno, "Неправильно: ", nepravilno)
print(f'Правильно ответили', pravilno)
print(f'Неправильно ответили', nepravilno)

