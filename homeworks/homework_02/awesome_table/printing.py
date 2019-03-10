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
    header = {h_name: {'count': len(h_name)} for h_name in input_list[0]}
    for row in input_list:
        for h_name, value in row.items():
            try:
                header[h_name]['count'] = max(header[h_name]['count'],
                                              len(str(value)))
            except KeyError:
                raise InvalidDataException

    format_item = "  {:%s%d}  "
    for h_name, spec in header.items():
        spec['format_col'] = format_item % ('<', spec['count'])
    count_dash = sum([spec['count'] + 4 + 1 for spec in header.values()]) + 1
    result = []
    result += ['-' * count_dash + '\n']
    result += [
        "|",
        "|".join([(format_item % (
            '^',
            header[h_name]['count'])).format(h_name)
                  for h_name in input_list[0]]),
        "|\n"]
    for row in input_list:
        result += [
            "|",
            "|".join([(format_item % (
                '>' if isinstance(value, int) or value.isdigit() else '<',
                header[h_name]['count'])).format(value)
                      for h_name, value in row.items()]), "|\n"]
    result += '-' * count_dash
    return ''.join(result)
