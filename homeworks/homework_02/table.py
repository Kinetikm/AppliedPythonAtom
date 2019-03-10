import sys

import awesome_table as table

if __name__ == '__main__':
    # Ваш код
    filename = sys.argv[1]
    try:
        with table.open_file(filename) as f:
            print(table.pretty_table(table.parse_file(f)))
    except FileNotFoundError:
        print("Файл не валиден")
    except (table.UnsupportedCharsetException,
            table.UnsupportedFormatException,
            table.InvalidDataException):
        print("Формат не валиден")
