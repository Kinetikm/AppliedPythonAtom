"""
Методы для работы с tsv
"""

import csv


def check_tsv(f_name: str, f_encoding: str) -> bool:
    """Проверка на формат tsv"""
    try:
        with open(f_name, encoding=f_encoding) as f:
            csv.reader(f, delimiter="\t")
            return True
    except csv.Error:
        return False


def read_tsv(f):
    """
    Считывает файл в формате tsv
    :param f: объекта файла
    :return: tuple(заголовки, содержимое) или tuple(None, None)
    """
    try:
        data = csv.reader(f, delimiter="\t")
    except csv.Error:
        return None, None

    headers = None
    content = []

    # получение заголовков и данных
    for line in data:
        if headers:
            # проверка заголовков (лучше когда тут только чтение)
            if len(headers) < len(line):
                return None, None
            content.append(dict(zip(headers, line)))
        else:
            headers = line

    # tsv без заголовка не считаем валидным
    if not headers:
        return None, None

    return headers, content
