import logging
import os
import pathlib

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p',
                    filename='loging.log')


# /Volumes/Flash 4 GB/#2Маши Мама я танцую.mp3

def rename_file_count_in_files(user_path):
    for root, dirs, files in os.walk(user_path):
        for file in files:
            if pathlib.Path(file).suffix == ".mp3":
                for i in range(1, len(files)):
                    old_file_name_path = f'{root}/{file}'
                    new_name = f'{root}/{i}_{file}'
                    os.rename(old_file_name_path, new_name)
                    yield old_file_name_path


def del_count_in_files(user_path):
    for root, dirs, files in os.walk(user_path):
        for file in files:
            file_beginner = file[0:2]
            if file_beginner == "._" and pathlib.Path(file).suffix == ".mp3":
                os.remove(f'{root}/{file}')


if __name__ == '__main__':
    THIS_PATH = pathlib.Path("C:\\Users\slim2\\iCloudDrive\\Music\\Вечная русская поп-музыка")
    logger = logging.getLogger(__name__)
    logger.info(rename_file_count_in_files(THIS_PATH))
    # logger.info(del_count_in_files(THIS_PATH))
    # print(del_count_in_files(THIS_PATH))
