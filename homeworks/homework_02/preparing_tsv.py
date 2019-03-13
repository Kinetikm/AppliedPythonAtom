import csv


def preparing_tsv(file, enc):
    Lst = []
    with open(file, encoding=enc):
        f = csv.reader(file, delimiter="\t")
        for s in f:
            Lst.append(s)
        return Lst
