x = int(input())
a = (x % 10) + (x // 1000)
b = ((x // 10) % 10) - ((x // 100) % 10)
# if a == b:
#     print("ДА")
# else:
#     print("НЕТ")
print(a, b)