from homeworks.homework_02.tabletask import InvalidFormat
from homeworks.homework_02.tabletask.data_check import get_data_and_type
from homeworks.homework_02.tabletask.print_table import print_table
import sys

if __name__ == '__main__':
    try:
        filename = sys.argv[1]
        data_type, data = get_data_and_type(filename)
        table = print_table(data)
    except (IndexError, InvalidFormat):
        print("Файл не валиден")
