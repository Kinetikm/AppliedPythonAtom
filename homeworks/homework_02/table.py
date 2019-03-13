import sys
import os

from checker import *
from read_file import read_file
from print_table import print_table


if __name__ == '__main__':
    # path = sys.argv[1]
    path = 'files/posts-utf8.tsv'
    if os.path.isfile(path) is False:
        print('Формат не валиден')
    else:
        encoding = check_encoding(path)
        extention = check_extensions(path)
        if check_validation(path, encoding, extention) is True:
            table = read_file(path, encoding, extention)
            print_table(table)
