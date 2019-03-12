import sys
import json
from parser import jsonpars
from parser import tsvpars
from output import output


if __name__ == "__main__":
    filename = sys.argv[1]
    try:
        open(filename, "r")
    except:
        print("Файл не валиден")
        sys.exit()

    encoding = ["utf-8", "cp1251", "utf-16"]
    correct_encoding = ""
    for enc in encoding:
        try:
            open(filename, encoding=enc).read()
        except (UnicodeDecodeError, LookupError):
            pass
        else:
            correct_encoding = enc
            break

    if correct_encoding == "":
        print("Формат не валиден")
        sys.exit()

    with open(filename, "r", encoding=correct_encoding) as f:
        try:
            text = f.read()
            if text.find("{") == -1:
                c = "tsv"
            else:
                c = "json"
        except:
            c = "tsv"

    try:

        if c == "json":
            output(jsonpars(filename, correct_encoding))
        if c == "tsv":
            output(tsvpars(filename, correct_encoding))
    except:
        print("Формат не валиден")
        sys.exit()
