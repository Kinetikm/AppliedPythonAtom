import json
from printing import *


def print_json(filename, enc):
    s = list()
    with open(filename, encoding=enc) as file:
        try:
            sr = json.load(file)
            s.append(list(sr[0].keys()))
            for i in sr:
                if list(i.keys()) != s[0]:
                    raise KeyError
                s.append(list(i.values()))
        except (KeyError, json.JSONDecodeError):
            raise ValueError("Формат не валиден")
        except IndexError:
            raise RuntimeError("Формат не валиден")
    print_file(s)