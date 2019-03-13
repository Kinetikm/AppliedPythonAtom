import sys

from encodings_check import define_encoding
from json_parsing import parse_json
from csv_parsing import parse_csv

if __name__ == '__main__':
    try:
        filename = sys.argv[1]
        encode = define_encoding(filename)
        try:
            parse_json(filename, encode)
        except ValueError:
            parse_csv(filename, encode)
    except FileNotFoundError:
        print("Файл не валиден")
    except (KeyError, ValueError, IndexError):
        print("Формат не валиден")
