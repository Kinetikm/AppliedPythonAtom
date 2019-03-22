import sys

# Ваши импорты
from table_package.detect_encoding import detect_enc
from table_package.make import make_table
from table_package.read_tsv import r_tsv
from table_package.read_json import r_json

if __name__ == '__main__':

    filename = sys.argv[1]

    # Ваш код
    try:
        encoding = detect_enc(filename)
    except FileNotFoundError:
        print("Файл не валиден")
        sys.exit()
    try:
        data = r_json(filename, encoding)
    except ValueError:
        data = r_tsv(filename, encoding)
    try:
        make_table(data)
    except:
        print("Формат не валиден")