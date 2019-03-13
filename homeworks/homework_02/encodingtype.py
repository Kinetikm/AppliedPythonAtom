def encoding_of_file(file):
    encodings = ['cp1251', 'utf8', 'utf16']
    for e in encodings:
        try:
            with open(file, encoding=e) as f:
                f.read(1)
        except UnicodeError:
            f.close()
            continue
        f.close()
        return e
    return 'another'
