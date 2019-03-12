encod = ['utf8', 'cp1251', 'utf16', 'ASCII']


def find_encode(f):
    for enc in encod:
        try:
            open(f, encoding=enc).read(1)
            return enc
        except:
            continue
    return None
