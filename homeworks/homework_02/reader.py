def read(file):
    heandle = open(file, "r", encoding="utf-16")
    try:
        return heandle.read()
    except UnicodeError:
        heandle = open(file, "r", encoding="utf-8")
        try:
            return heandle.read()
        except UnicodeError:
            heandle = open(file, "r", encoding="cp1251")
            try:
                return heandle.read()
            except:
                raise ValueError
