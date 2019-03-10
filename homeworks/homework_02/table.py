import os  # проверка существования файла
import sys

from table import file_encodings, file_formats, file_printing


def print_file_data(f_name: str) -> None:
    """
    Метод для вывода содержимого файла
    на экран в табличном формате
    :param f_name: имя файла
    """
    # проверка существования файла через os.path
    # альтернативы - try...except или from pathlib import Path
    if not os.path.isfile(f_name):
        print("Файл не валиден")
        # raise FileNotFoundError("Файл не валиден")
        return None

    # определение кодировки
    f_encoding = file_encodings.get_charset(f_name=f_name)
    if not f_encoding:
        print("Формат не валиден")
        # raise UnicodeError("Формат не валиден")

    # определение формата
    f_format = file_formats.get_format(f_name=f_name, f_encoding=f_encoding)
    if not f_format:
        print("Формат не валиден")
        # raise ValueError("Формат не валиден")

    # печать на экран
    file_printing.print_table(f_name=f_name,
                              f_encoding=f_encoding,
                              f_format=f_format)


if __name__ == '__main__':
    # проверка что передали все необходимые параметры
    if len(sys.argv) < 2:
        print("Имя файла обязательный параметр")
        # raise SystemExit("Имя файла обязательный параметр")
        exit(1)

    print_file_data(f_name=sys.argv[1])
