import os

path = '/Users/denisdavydov/Library/CloudStorage/GoogleDrive-davidov.denis.reklama@gmail.com/Мой диск/Проекты/Таргет/trek-metall/img'
for i in os.listdir(path):
    for j in os.listdir(os.path.join(path, i)):
        if i.endswith('.webp'):
            i.replace('.webp', '.jpg')
            os.rename(os.path.join(path, i), os.path.join(path, i.replace('.webp', '.jpg')))
        else:
            print(j)
