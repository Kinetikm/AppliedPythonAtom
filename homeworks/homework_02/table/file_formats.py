"""
Методы для определения формата файла и считывания данных
"""

import json
import csv


def read_tsv(f_name: str, f_encoding: str):
    """
    Считывает файл в формате tsv
    :param f_name: имя файла
    :param f_encoding: кодировка
    :return: заголовки и содержимое файла, tuple или None
    """
    headers = None
    content = []

    with open(f_name, encoding=f_encoding) as f:
        try:
            data = csv.reader(f, delimiter="\t")
        except csv.Error:
            return None, []

        # получение заголовков и данных
        for line in data:
            if headers:
                # проверка заголовков (лучше когда тут только чтение)
                if len(headers) < len(line):
                    return None, []
                content.append(dict(zip(headers, line)))
            else:
                headers = line

    # tsv без заголовка не считаем валидным
    if not headers:
        return None, []

    return headers, content


def read_json(f_name: str, f_encoding: str):
    """
    Считывает файл в формате json
    :param f_name: имя файла
    :param f_encoding: кодировка
    :return: заголовки и содержимое файла, tuple или None
    """
    try:
        with open(f_name, encoding=f_encoding) as f:
            content = json.load(f)
    except json.JSONDecodeError:
        return None, []

    # пустой json не считаем валидным
    if len(content) < 1:
        return None, []

    headers = list(content[0].keys())

    return headers, content


formats = {
    'json': read_json,
    'tsv': read_tsv,
}


def read_file_content(f_name: str, f_encoding: str) -> tuple:
    """
    Функция получения формата файла
    :param f_name: имя файла для проверки
    :param f_encoding: кодировка файла
    :return: заголовки и содержимое файла, tuple или None
    """
    for f_format, func in formats.items():
        headers, content = func(f_name=f_name, f_encoding=f_encoding)
        if headers:
            return headers, content
    raise TypeError("Не удалось получить содержимое файла")
