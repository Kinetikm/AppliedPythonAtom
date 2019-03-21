import sys

# Ваши импорты

from homeworks.homework_02.checking import tsv_format, json_format
from homeworks.homework_02.print_table import print_table

if __name__ == '__main__':
    filename = sys.argv[1]

    # Ваш код
    try:
        data = None
        if json_format(filename)[0]:
            data = json_format(filename)[1]
        elif tsv_format(filename)[0]:
            data = tsv_format(filename)[1]
        else:
            print('Формат не валиден')
        print_table(data)

    except FileNotFoundError:
        print('Файл не валиден')
    except (UnicodeError, ValueError):
        print('Формат не валиден')
