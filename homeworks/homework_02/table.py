import sys

from print_table import *

# path = 'files/posts-cp1251.json'

if __name__ == '__main__':
    try:
        filename = sys.argv[1]
        print_file(filename)
    except(IndexError, AssertionError):
        print('Формат не валиден')
