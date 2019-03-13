def is_utf8(f_name):
    try:
        with open(f_name, encoding='utf8') as f:
            f.read(1)
    except UnicodeError:
        return False
    return True


def is_cp1251(f_name):
    try:
        with open(f_name, encoding='cp1251') as f:
            f.read(1)
    except UnicodeError:
        return False
    return True


def is_utf16(f_name):
    try:
        with open(f_name, encoding='utf16') as f:
             f.read(1)
    except UnicodeError:
        return False
    return True


def define_encoding(f_name):
    if is_utf8(f_name):
        return 'utf8'
    elif is_utf16(f_name):
        return 'utf16'
    elif is_cp1251(f_name):
        return 'cp1251'
    else:
        return None
