import sys
from type_is import json_or_tsv
from parse import read_data, print_data
from file import open_file
from encode import find_encode


if __name__ == '__main__':
    filename = sys.argv[1]
    if not open_file(filename):
        raise SystemExit("Can not open file")
    type_f = find_encode(filename)
    encoding = json_or_tsv(filename, type_f)
    if encoding is None:
        raise SystemExit("Can not open Encoding")
    print_data(read_data(filename, type_f, encoding))
