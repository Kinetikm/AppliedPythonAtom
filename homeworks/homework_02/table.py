import sys
from functions.checker import define_format
from functions.data_creator import read_json, read_tsv
from functions.table_creator import create_table

if __name__ == '__main__':
    filename = sys.argv[1]

    try:
        data = None
        frmt = define_format(filename)
        if frmt == 0:
            create_table(read_json(filename))
        if frmt == 1:
            create_table(read_tsv(filename))

    except FileNotFoundError:
        print('Файл не валиден')
    except (UnicodeError, UnicodeDecodeError):
        print('Данные не валидны')
    except ValueError:
        print('Данные не валидны')
