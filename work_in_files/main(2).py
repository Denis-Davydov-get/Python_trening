import logging
import os

PATH = "C:\\Users\slim2\\iCloudDrive\\Music\\Вечная русская поп-музыка"
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p',
                    filename='loging.log',
                    encoding = "UTF-8")


# rename_file_count_in_files(PATH)

def read_folder(path_folder):
    for path, dirs, files in os.walk(PATH):
        for file in files:
            return os.rename(file, f'')


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.info((read_folder(PATH)))
