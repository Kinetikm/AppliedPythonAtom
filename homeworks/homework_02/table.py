import sys
import re
from checker import *
from maketable import *


def new_print_table(table):
    col_width = [max(len(x) for x in col) for col in zip(*table)]
    length = sum(col_width) + 21
    flag = True
    for tline in table:
        test1 = (
                "|  " +
                "  |  ".join(
                    "{:^{}}".format(
                        x,
                        col_width[i])for i,
                    x in enumerate(tline)) +
                "  |")
        if len(test1) != length:
            print('Формат не валиден')
            flag = False
            break
        test2 = (
                "|  " + "  |  ".join(
                    "{:{}}".format(x, col_width[i])for i,
                    x in enumerate(tline[:len(tline) - 1])) +
                "  |  " + '{:>{}}'.format(tline[-1], col_width[-1]) + "  |")
        if len(test2) != length:
            print('Формат не валиден')
            flag = False
            break
    if flag is True:
        print('-' * length)
        count = 1
        for line in table:
            if count == 1:
                print(
                    "|  " +
                    "  |  ".join(
                        "{:^{}}".format(
                            x,
                            col_width[i])for i,
                        x in enumerate(line)) +
                    "  |")
                count += 1
            else:
                print(
                    "|  " + "  |  ".join(
                        "{:{}}".format(x, col_width[i])for i,
                        x in enumerate(line[:len(line) - 1])) +
                    "  |  " + '{:>{}}'.format(line[-1], col_width[-1]) + "  |")
        print('-' * length)


def print_file(path):
    frmt = chech_valid(path)
    if frmt is not False:
        if frmt == 'json':
            data = make_json_table(path)
        elif frmt == 'tsv':
            data = make_tsv_table(path)
        lensum = 0
        for i in data:
            lensum += len(i)
        if lensum != 0 and len(data) >= 1:
            new_print_table(data)
        else:
            print('Формат не валиден')


if __name__ == '__main__':
    try:
        filename = sys.argv[1]
        print_file(filename)
    except(IndexError, AssertionError):
        print('Формат не валиден')
