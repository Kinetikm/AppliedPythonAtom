"""
Методы для определения кодировки файла

альтернативные варианты:
    import chardet
    chardet.detect(rawdata)

    from bs4 import UnicodeDammit
    dammit = UnicodeDammit(rawdata)
"""

encodings = [
    'utf8',
    'utf16',
    'cp1251',
]


def get_charset(f_name: str):
    """
    Функция получения кодировки файла
    :param f_name: имя файла для проверки
    :return: кодировка файла (в пригодном для open формате) или None
    """
    # пытаемся определить кодировку
    for enc in encodings:
        try:
            with open(f_name, encoding=enc) as f:
                f.read()
            return enc
        except UnicodeError:
            pass
    return None  # не удалось определить
