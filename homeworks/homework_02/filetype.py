import json
import csv


def check_json(file, enc):
    with open(file, encoding=enc) as f:
        try:
            content = json.load(f)
        except json.JSONDecodeError:
            f.close()
            return False
        f.close()
        return True


def check_tsv(file, enc):
    with open(file, encoding=enc) as f:
        content = csv.reader(f, delimiter="\t")
        for str in content:
            if len(str) == 0:
                f.close()
                return False
        f.close()
        return True


def format_of_file(f, enc):
    if check_json(f, enc):
        return 'json'
    elif check_tsv(f, enc):
        return 'tsv'
    else:
        return 'another'
