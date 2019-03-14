import sys

# Ваши импорты
from encode import check_encoding
from check_format import check_file_format
from construct_table import take_data

if __name__ == '__main__':
    filename = sys.argv[1]
    try:
        f = open(filename)
        f.close()
    except FileNotFoundError:
        raise SystemExit("Файл не валиден")
    coding = str(check_encoding(filename))
    ext = check_file_format(filename, coding)
    take_data(ext, filename, coding)
