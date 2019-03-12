"""
Методы для форматированной печати на экран
"""

from .file_formats import read_file_content


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
                raise AttributeError("Строка не содержит нужного заголовка")
            temp = len(str(temp))
            if temp > headers_len[header]:
                headers_len[header] = temp
    return headers_len


def print_table(f_name: str, f_encoding: str) -> None:
    """
    Функция отрисовки данных файла в виде таблицы
    :param f_name: имя файла
    :param f_encoding: кодировка
    """
    # получение содержимого файлов
    # лучше не читать весь файл сразу
    headers, content = read_file_content(f_name=f_name, f_encoding=f_encoding)

    # проверка заголовков
    for item in content:
        if len(headers) < len(item.keys()):
            raise AttributeError("В заголовке недостаточно столбцов")

    # расчёт длин столбцов и итоговой длины
    headers_len = _calculate_len(headers=headers, content=content)

    total_len = 1 + len(headers) * 5 + sum(headers_len.values())

    # печать заголовков
    print('-' * total_len)
    full_header = '|'
    for header, length in headers_len.items():
        header_line = '  {:^' + str(length) + '}  |'
        full_header += header_line.format(header)
    print(full_header)

    # печать тела
    if content:
        full_content = ''
        for item in content:
            full_content += '\n|' if full_content else '|'
            for header, line in item.items():
                # выравнивание последнего столбца по правому краю
                content_line = '  {:>' if header == headers[-1] else '  {:'
                content_line += str(headers_len[header]) + '}  |'
                full_content += content_line.format(line)
        print(full_content)
    print('-' * total_len)
