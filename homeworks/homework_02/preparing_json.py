import json


def preparing_json(file, enc):
    Lst = []
    with open(file, encoding=enc):
        f = json.load(file)
        Lst.append(f[0].keys())
        for s in f:
            Lst.append(s.values())
        return Lst
