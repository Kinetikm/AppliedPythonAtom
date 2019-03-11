"""
Методы для определения формата файла
"""

from json_file.utilities import check_json
from tsv_file.utilities import check_tsv


formats = {
    'json': check_json,
    'tsv': check_tsv,
}


def get_format(f_name: str, f_encoding: str):
    """
    Функция получения формата файла
    :param f_name: имя файла для проверки
    :param f_encoding: кодировка файла
    :return: формат файла или None
    """
    for f_format, func in formats.items():
        if func(f_name=f_name, f_encoding=f_encoding):
            return f_format
    return None
