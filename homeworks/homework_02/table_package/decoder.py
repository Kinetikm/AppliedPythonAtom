import codecs


def check_codec(filename):
    codec_list = ["utf8", "utf16", "cp1251"]
    for cdc in codec_list:
        try:
            f = codecs.open(filename, encoding=cdc, errors='strict')
            for _ in f:
                pass
        except UnicodeDecodeError:
            continue
        except UnicodeError:
            continue
        return cdc
    return None
