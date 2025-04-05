from datetime import datetime


def is_valid_date(str_date):
    try:
        year = int(str_date[:4])
        month = int(str_date[4:6])
        day = int(str_date[6:8])
        datetime(year, month, day)
        return True
    except ValueError:
        return False


# Пример использования
data = "20241141"
year = int(data[:4])
month = int(data[4:6])
day = int(data[6:8])
if is_valid_date(data):
    print(f"Дата {year, month, day} существует.")
else:
    print(f"Дата {year, month, day} не существует.")