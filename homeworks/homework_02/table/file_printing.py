"""
Модуль содержащий методы для форматированной печати на экран
"""

import json
import csv


def _read_json(f):
    """
    Считывает файл в формате json
    :param f: объекта файла
    :return: tuple(заголовки, содержимое) или tuple(None, None)
    """
    try:
        data = json.load(f)
    except json.JSONDecodeError:
        return None, None

    # пустой json не считаем валидным
    if len(data) < 1:
        return None, None

    headers = data[0].keys()

    # проверка заголовков
    for item in data:
        if len(headers) < len(item.keys()):
            return None, None

    return headers, data


def _read_tsv(f):
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
            # проверка заголовков
            if len(headers) < len(line):
                return None, None
            content.append(dict(zip(headers, line)))
        else:
            headers = line

    # tsv без заголовка не считаем валидным
    if not headers:
        return None, None

    return headers, content


formats = {
    'json': _read_json,
    'tsv': _read_tsv,
}


def _calculate_len(headers: list, content: list):
    """
    Расчёт максимальной длины для каждого столбца
    :param headers: список заголовком
    :param content: список содержимого
    :return: словарь длин
    """
    headers_len = {header: len(header) for header in headers}
    for line in content:
        for header in headers:
            temp = line.get(header)
            # проверка что заголовок есть в строке
            if temp is None:
                return None
            temp = len(str(temp))
            if temp > headers_len[header]:
                headers_len[header] = temp
    return headers_len


def print_table(f_name: str, f_encoding: str, f_format: str) -> None:
    """
    Функция отрисовки данных файла в виде таблицы
    :param f_name: имя файла
    :param f_encoding: кодировка
    :param f_format: формат
    """
    # получение содержимого файлов
    # лучше не читать весь файл сразу
    with open(f_name, encoding=f_encoding) as f:
        headers, content = formats[f_format](f)
        if not headers:
            print("Формат не валиден")
            # raise ValueError("Формат не валиден")
            return None

    # расчёт длин столбцов и итоговой длины
    headers_len = _calculate_len(headers=headers, content=content)
    if headers_len is None:
        print("Формат не валиден")
        # raise ValueError("Формат не валиден")
        return None

    total_len = 1 + len(headers) * 5 + sum(headers_len.values())

    # печать заголовков
    print('-' * total_len)
    full_header = '|'
    for header, length in headers_len.items():
        header_line = '  {:^' + str(length) + '}  |'
        full_header += header_line.format(header)
    print(full_header)

    # печать тела
    if len(content):
        full_content = ''
        for item in content:
            full_content += '\n|' if full_content else '|'
            for header, line in item.items():
                content_line = '  {:>' if str(line).isdigit() else '  {:'
                content_line += str(headers_len[header]) + '}  |'
                full_content += content_line.format(line)
        print(full_content)
    print('-' * total_len)
