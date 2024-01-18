frend_speed_1 = 1
frend_speed_2 = 2
dog_speed = 5
count = 0
frend = 2
distace = 1000
distace_min = 1
frend = 1
while distace > distace_min:
    if frend == 1:
        distace -= frend_speed_1 + dog_speed
        count += 1
        frend = 2
    elif frend == 2:
        distace -= frend_speed_2 + dog_speed
        count += 1
        frend = 1
    else:
        print('Something\'s wrong.')
print(f'The dog will run', count, 'once')
