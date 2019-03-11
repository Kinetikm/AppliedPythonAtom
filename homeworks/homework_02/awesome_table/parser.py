import json
import csv

from .errors import UnsupportedFormatException


__all__ = ['parse_file']


def _json_parser(file):
    pos = file.tell()
    try:
        j_list = json.load(file)
        header = list(j_list[0])
        if not header:
            raise UnsupportedFormatException
        body = []
        for row in j_list:
            body.append([row[h_name] for h_name in header])
        return [header] + body
    except json.JSONDecodeError:
        file.seek(pos)
        return None
    except (KeyError, IndexError):
        raise UnsupportedFormatException


def _tsv_parser(file):
    pos = file.tell()
    res = list(csv.reader(file, delimiter='\t'))
    if res:
        row_len = len(res[0])
        if row_len == 0 or any(map(lambda row: len(row) - row_len, res)):
            file.seek(pos)
            return None
        return res
    file.seek(pos)
    return None


FORMATS = {
    'json': _json_parser,
    'tsv': _tsv_parser
}


def parse_file(file, file_format=None):
    """
    Метод читающий таблицу из файла для поддерживаемых форматов.
    :param file: Файл для чтения
    :param file_format: Формат данных. Если не указан, перебирает все
    поддерживаемые форматы
    :return: Список словарей, в которых ключем является заголовок,
    а значением - значение ячейки таблицы, либо исключение,
    если формат не поддерживается или имеет невалидную структуру
    """
    if file_format is None:
        file_format = FORMATS.keys()
    elif not isinstance(file_format, str):
        raise UnsupportedFormatException
    else:
        file_format = [file_format]

    for parser in file_format:
        try:
            res = FORMATS[parser](file)
        except ValueError:
            raise UnsupportedFormatException
        if res is not None:
            return res
    raise UnsupportedFormatException
