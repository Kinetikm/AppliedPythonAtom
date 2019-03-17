import csv
import json

def jsonpars(filename, correct_encoding):
    with open(filename,'r',encoding=correct_encoding) as f:
        raws = f.read()
    raws = json.loads(raws)
    keys = list()
    out =list()
    for key in raws[0]:
        keys.append(key)
    out.append(keys)
    for dicts in raws:
        tmp = list()
        for key in keys:
            tmp.append(dicts[key])
        out.append(tmp)
        tmp.clear
    return out
        



def tsvpars(filename, correct_encoding):
    with open(filename,'r',encoding=correct_encoding) as f:
        reader = csv.reader(f, delimiter='\t')
        out = list()
        for row in reader:
            out.append(row)
    return out
