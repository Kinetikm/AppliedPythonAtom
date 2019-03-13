import sys

from access_check import check_json, check_csv, check_format
from encording_test import check_utf8, check_utf16, \
    check_cp1251, check_encording
from table_print import print_tab


def main():
    try:
        try:
            filename = sys.argv[1]
        except IndexError:
            raise SystemExit("Argument not found")
        file_descriptor, Encording = check_encording(filename)
        # file_descriptor, Encording = check_encording("files/posts-utf8.json")
        buffer = check_format(file_descriptor)
        print_tab(buffer)
    except UnicodeError:
        print("Неверная кодировка")
    except FileNotFoundError:
        print("Файл не валиден")
    except Warning:
        print("Формат не валиден")


if __name__ == '__main__':
    main()
