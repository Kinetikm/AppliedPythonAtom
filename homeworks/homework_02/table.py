import sys

# Ваши импорты

from homeworks.homework_02.checking_d import true_format
from homeworks.homework_02.print_table_d import print_table

if __name__ == '__main__':
    filename = sys.argv[1]

    # Ваш код
    try:
        flag, data = true_format(filename)
        if flag == -1:
            print('Формат не валиден')
        else:
            print_table(data)

    except FileNotFoundError:
        print('Файл не валиден')
    except (UnicodeError, ValueError):
        print('Формат не валиден')

