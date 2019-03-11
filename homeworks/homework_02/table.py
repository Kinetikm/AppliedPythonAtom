import sys

from json import JSONDecodeError
from table_package.decoder import check_codec
from table_package.parser import try_json, try_tsv
from table_package.printer import Print_JSON, Print_TSV

if __name__ == '__main__':
    filename = sys.argv[1]

    cdc = check_codec(filename)
    is_json = True
    # # if json
    try:
        data = try_json(filename, cdc)
    except JSONDecodeError:
        is_json = False
        pass
    if is_json:
        jp = Print_JSON(data)
        jp.print_line()
        jp.print_head()
        jp.print_body()
        jp.print_line()

    if not is_json:
        tsv_list = try_tsv(filename, cdc)

        tsvp = Print_TSV(tsv_list)
        tsvp.print_line()
        tsvp.print_head()
        tsvp.print_body()
        tsvp.print_line()
