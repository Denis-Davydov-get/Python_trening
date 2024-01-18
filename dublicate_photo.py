import os
import shutil
from PIL import Image, ImageChops

print('Введите ПОЛНЫЙ путь к папке: ', end = '')
file_path = r"G:\из icloud 07.11.2023\iCloud Photos"

directory = os.fsencode(file_path)
imgs = os.listdir(file_path)
dublicates = {}
count = 0
try:
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        last_name = file_path
        last_name += '\\' + filename
        f_info = os.stat(last_name)
        if f_info.st_size in dublicates:
            image_1 = Image.open(last_name)
            image_2 = Image.open(dublicates[f_info.st_size])
            result = ImageChops.difference(image_1, image_2)
            result = result.getbbox()
            if result == None:
                count += 1
                print(f'Найден дубликат: [{last_name} и {dublicates[f_info.st_size]}]')
            else:
                dublicates[f_info.st_size] = last_name
except:
    print('Ошибка поиска директории!')

print(f'Программа завершила работу, файлов обработано [{count}].')