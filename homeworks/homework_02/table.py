#!/usr/bin/env python
# coding: utf-8



from sys import argv
from proverka_kodirovki import *
from json import *
from tsv import *

if __name__ == '__main__':
    filename = argv[1]

    try:
        filename = argv[1]
        enc = get_kod(filename)
        try:
            print_json(filename, enc)
        except (ValueError, RuntimeError):
            print_tsv(filename, enc)
    except (FileNotFoundError, IndexError):
        print("Файл не валиден")
    except (ValueError, RuntimeError):
        print("Формат не валиден")
