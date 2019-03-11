from collections import OrderedDict

from .errors import InvalidDataException


def pretty_table(input_list):
    """
    Метод возвращает строку с таблицей в удобочитаемом виде
    :param input_list: Список со словарями, в которых ключом является заголовок
    столбца, значением - значение ячейки
    :return:  Строка или исключение, если входные данные невалидны
    """
    if not input_list:
        return None

    format_item = "  {:%s%d}  "
    header = input_list.pop(0)
    header_spec = [len(h_name) for h_name in header]
    for row in input_list:
        for idx, value in enumerate(row):
            try:
                header_spec[idx] = max(header_spec[idx], len(str(value)))
            except IndexError:
                raise InvalidDataException

    count_dash = sum([header_len + 4 + 1 for header_len in header_spec]) + 1
    result = []
    result += ['-' * count_dash + '\n', ]
    result += ['|',
               '|'.join([(format_item % (
                   '^',
                   header_spec[idx])).format(h_name)
                         for idx, h_name in enumerate(header)]),
               '|\n']
    for row in input_list:
        result += ['|', '|'.join([
            (format_item % ('>' if value is not None and (
                        isinstance(value, int) or value.isdigit()) else '<',
                            header_spec[idx])).format(value) for idx, value in
            enumerate(row)]), '|\n']
    result += ['-' * count_dash + '\n']
    return ''.join(result)
