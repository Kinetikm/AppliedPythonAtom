"""
Методы для форматированной печати на экран
"""

from json_file.utilities import read_json
from tsv_file.utilities import read_tsv

formats = {
    'json': read_json,
    'tsv': read_tsv,
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
