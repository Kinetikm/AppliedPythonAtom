import sys


from encodings_check import define_encoding
from file_worker import check_is_exists, print_info
from format_check import define_format

if __name__ == '__main__':
    try:
        filename = sys.argv[1]
    except IndexError:
        raise SystemExit("Argument does not exist")

    is_exist = check_is_exists(filename)
    if not is_exist:
        raise SystemExit("Unable to open file")
    encode = define_encoding(filename)
    if encode is None:
        raise SystemError("Unknown encoding")
    format = define_format(filename, encode)
    print_info(filename, format, encode)
