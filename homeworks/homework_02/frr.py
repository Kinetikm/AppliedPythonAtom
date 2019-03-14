import codecs


def check_encoding(filename):
    res = 0
    encoding_list = ["utf8", "utf16", "cp1251"]
    for enc in encoding_list:
        try:
            f = codecs.open(filename, encoding=enc, errors='strict')
            for _ in f:
                pass
        except UnicodeDecodeError:
            continue
        except UnicodeError:
            continue
        except ValueError:
            continue
        except FileNotFoundError:
            print("Файл не валиден")
            break
        res = enc
    if res == 0:
        print("Формат не валиден2")
    return res
