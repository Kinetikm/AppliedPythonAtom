from .errors import UnsupportedCharsetException


__all__ = ['open_file']


def utf8_open(filename, ctx=False, **kwargs):
    """
    Метод, открывающий файл в кодировке utf8. Если попытка чтения файла
    оказывается удачной возвращает файл или флаг удачности выбора кодировки
    :param filename: Имя файла для открытия
    :param ctx: Флаг, указывающий на то, необходимо ли возвращать файл
    :param kwargs: Флаги, передающиеся в open
    :return: True или открытый файл, если успешно чтение, иначе None
    """
    try:
        f = open(filename, encoding='utf8', **kwargs)
        f.readline()
        if ctx:
            f.seek(0)
            return f
        f.close()
        return True
    except UnicodeDecodeError:
        f.close()
        return None


def utf16_open(filename, ctx=False, **kwargs):
    """
        Метод, открывающий файл в кодировке utf16. Если попытка чтения файла
        оказывается удачной возвращает файл или флаг удачности выбора кодировки
        :param filename: Имя файла для открытия
        :param ctx: Флаг, указывающий на то, необходимо ли возвращать файл
        :param kwargs: Флаги, передающиеся в open
        :return: True или открытый файл, если успешно чтение, иначе None
        """
    try:
        f = open(filename, encoding='utf16', **kwargs)
        f.readline()
        if ctx:
            f.seek(0)
            return f
        f.close()
        return True
    except (UnicodeDecodeError, UnicodeError):
        f.close()
        return None


def cp1251_open(filename, ctx=False, **kwargs):
    """
        Метод, открывающий файл в кодировке cp1251. Если попытка чтения файла
        оказывается удачной возвращает файл или флаг удачности выбора кодировки
        :param filename: Имя файла для открытия
        :param ctx: Флаг, указывающий на то, необходимо ли возвращать файл
        :param kwargs: Флаги, передающиеся в open
        :return: True или открытый файл, если успешно чтение, иначе None
        """
    try:
        f = open(filename, encoding='cp1251', **kwargs)
        f.readline()
        if ctx:
            f.seek(0)
            return f
        f.close()
        return True
    except UnicodeDecodeError:
        f.close()
        return None


FORMATS = {
    'utf8': utf8_open,
    'utf16': utf16_open,
    'cp1251': cp1251_open
}


class open_file(object):
    """
    Контекст менеджер, позволяющий открывать поддерживаемые кодировки
    без указания расширения. Если кодировка не поддерживается бросает ислючение
    """
    def __init__(self, filename, encoding=None, **kwargs):
        self.filename = filename
        self.kwargs = kwargs
        if encoding is None:
            self.charsets = FORMATS.keys()
        elif not isinstance(encoding, str) or FORMATS.get(encoding) is None:
            raise UnsupportedCharsetException
        else:
            self.charsets = [encoding]

    def __enter__(self):
        for charset in self.charsets:
            res = FORMATS[charset](self.filename, ctx=True, **self.kwargs)
            if res:
                self.open_file = res
                return self.open_file
        raise UnsupportedCharsetException

    def __exit__(self, *args):
        self.open_file.close()
