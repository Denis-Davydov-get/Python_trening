# Проверка палиндрома
# Определить, является ли строка палиндромом: "казак", "радар".

def is_palindrome(input_temp:str)->bool:
    return str(input_temp) == str(input_temp)[::-1]

list_str = ["радар", "казак", "роза"]

for item in list_str:
    if is_palindrome(item):
        print(item)
    else:
        print("Not a palindrome")
