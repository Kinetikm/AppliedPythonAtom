import json
import csv

from .errors import UnsupportedFormatException


__all__ = ['parse_file']


def _json_parser(file):
    pos = file.tell()
    try:
        return json.load(file)
    except json.JSONDecodeError:
        file.seek(pos)
        return None


def _tsv_parser(file):
    pos = file.tell()
    res = list(csv.DictReader(file, delimiter='\t'))
    if res:
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
