import sys

# Ваши импорты
from table_package.decoder import check_codec
from table_package.parser import js
from table_package.printer import Print_JSON

if __name__ == '__main__':
    filename = sys.argv[1]

    cdc = check_codec(filename)
    data = js(filename, cdc)
    #    print(data)

    jp = Print_JSON(data)
    jp.print_line()
    jp.print_head()
    jp.print_body()
    jp.print_line()

    # dic = {}
    # list = []
    #
    # for dic in data:
    #     for col_name, value in dic.items():
    #         print(value, end=' ')
    #     print()

    # for i in data:
    #     print(type(i))
    #     for k, v in i.items():
    #         print(type(k), type(v))
    #         print(k)
    #         print(v)
