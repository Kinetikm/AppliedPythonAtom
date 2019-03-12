def open_file(f):
    try:
        file = open(f)
        return True
    except:
        return False
