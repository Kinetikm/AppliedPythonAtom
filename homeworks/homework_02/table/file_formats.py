"""
Модуль содержащий методы для определения формата файла
"""

import json
import csv


def _check_json(f_name: str, f_encoding: str) -> bool:
    """Проверка на формат json"""
    try:
        with open(f_name, encoding=f_encoding) as f:
            json.load(f)
            return True
    except json.JSONDecodeError:
        return False


def _check_tsv(f_name: str, f_encoding: str) -> bool:
    """Проверка на формат tsv"""
    try:
        with open(f_name, encoding=f_encoding) as f:
            csv.reader(f, delimiter="\t")
            return True
    except csv.Error:
        return False


formats = {
    'json': _check_json,
    'tsv': _check_tsv,
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
