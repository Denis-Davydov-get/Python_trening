# Конвертер температур
# Введите градусы в Цельсиях — получите Фаренгейты.
# Формула: F = C * 9/5 + 32

def convert_temp(c: float) -> float:
    return c * 9/5 + 32

input_temp = float(input("Enter temp in Celsius: "))
print(convert_temp(input_temp))