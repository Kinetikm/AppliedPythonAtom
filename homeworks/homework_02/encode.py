def check_encoding(file_name):
    encode = ['utf-8', 'utf-16', 'cp1251']
    for enc in encode:
        try:
            with open(file_name, encoding=enc) as f:
                f.read()
            return enc
        except UnicodeError:
            pass
    raise UnicodeError("Не определена кодировка")
