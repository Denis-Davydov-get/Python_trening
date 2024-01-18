import time
with open('yandex_roistat.txt', 'r') as file:
    for i in file:
        i = str(i)
        result = int(time.mktime(time.strptime(i, '%Y-%m-%d %H:%M:%S')))

