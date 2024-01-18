import random
number_user = int(input("input number: "))
number_random = random.randint(1, 8)
if number_random == number_user:
    print("you dead")
else:
    print("you live")