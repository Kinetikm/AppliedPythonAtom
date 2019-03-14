import sys

from checker import *
from read_file import read_file
from print_table import print_table


if __name__ == '__main__':
    path = sys.argv[1]

    # path = 'files/posts-utf8.json'

    extensions = check_validation(path)
    if extensions == False:
        pass
    else:
        table = read_file(path, extensions)
        print_table(table)



