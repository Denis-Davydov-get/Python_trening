import requests
file = open('../url_testing.txt', 'r')
for i in file:
    result = requests.get(i)
    if result.status_code == 200:
        print(i, 'ok')
    else:
        print('error')

file.close()