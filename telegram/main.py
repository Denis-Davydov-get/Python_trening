import requests


api_url = ' http://numbersapi.com/43/'

response = requests.get(api_url)  # Отправляем GET-запрос и сохраняем ответ в переменной response

if response.status_code == 200:  # Если код ответа на запрос - 200, то смотрим, что пришло в ответе
    with open('telegram/result.txt', 'w', encoding="utf-8") as f:
        f.write(response.text)
else:
    print(response.status_code)  # При другом коде ответа выводим этот код