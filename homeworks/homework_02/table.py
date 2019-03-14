import sys
from check_encodings import *
from output_json import *
from output_tsv import *


if __name__ == '__main__':
    try:
        filename = sys.argv[1]
        enc = get_encoding(filename)
        try:
            print_json(filename, enc)
        except (ValueError, RuntimeError):
            print_tsv(filename, enc)
    except (FileNotFoundError, IndexError):
        print("Файл не валиден")
    except (ValueError, RuntimeError):
        print("Формат не валиден")
	