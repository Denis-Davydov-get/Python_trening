import os


def gen_files(count_files):
    for i in range(count_files):
        with open(str(i) + '.file_' + str(i) + '.txt', 'w') as f:
            f.write(str(i) + '.file' + '.txt')


def del_count_in_files(path_folder):
    for root, dirs, files in os.walk(path_folder):
        for file in files:
            try:
                if file.endswith('.mp3'):
                    os.rename(file, '.'.join(file.split('.')[1::]))
            except FileNotFoundError as e:
                print(e)


del_count_in_files('E:\\попса')
# gen_files(8)
