import json


def check_utf8(filename):
    try:
        f = open(filename, encoding="utf8")
        f.read()
        f.seek(0)
    except UnicodeError:
        return 0
    except FileNotFoundError:
        raise FileNotFoundError("file not exists")
    return f


def check_utf16(filename):
    try:
        f = open(filename, encoding='utf16')
        f.read()
        f.seek(0)
    except UnicodeError:
        return 0
    except FileNotFoundError:
        raise FileNotFoundError("file not exists")
    return f


def check_cp1251(filename):
    try:
        f = open(filename, encoding='cp1251')
        f.read()
        f.seek(0)
    except UnicodeError:
        return 0
    except FileNotFoundError:
        raise FileNotFoundError
    return f


def check_encording(filename):
    try:
        f1 = check_utf8(filename)
        f2 = check_utf16(filename)
        f3 = check_cp1251(filename)
        if f1:
            return f1, "utf8"
        elif f2:
            return f2, "utf16"
        elif f3:
            return f3, "cp1251"
        else:
            print("Error")
            raise UnicodeError
    except TypeError:
        raise FileNotFoundError
