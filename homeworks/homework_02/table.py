import sys
from TsvParser import TsvParser as tp
from JsonParser import JsonParser as jp

# Ваши импорты

if __name__ == '__main__':
    filename = sys.argv[1]
    parser = tp.TsvParser()
    try:
        parser.open(filename)
    except FileNotFoundError:
        print('Файл не валиден')
        exit(-1)
    if not parser.valid:
        parser = jp.JsonParser()
        parser.open(filename)
    if not parser.valid:
        print("Формат не валиден")
    else:
        parser.get_table().print()

    # Ваш код
