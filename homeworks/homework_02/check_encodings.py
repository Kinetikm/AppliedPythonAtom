Available_encodings = ['utf8', 'utf16', 'cp1251']


def get_encoding(filename):
    for enc in Available_encodings:
        try:
            with open(filename, 'r', encoding=enc) as file:
                file.readlines()
                return enc
        except UnicodeError:
            continue
    print("Формат не валиден")
