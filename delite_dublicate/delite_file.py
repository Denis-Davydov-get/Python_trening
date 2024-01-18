import os;
from pathlib import Path, PureWindowsPath

folder = Path('G:/Общие/')
list_files = []
with open("data_base_dublicate.txt", "r") as file:
    for i in file:
        new_path = str(folder) + i
        path_on_windows = PureWindowsPath(new_path)
        list_files.append(new_path)
        # print(new_path)
        os.remove(new_path)

print(list_files)