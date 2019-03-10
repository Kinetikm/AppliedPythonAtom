#!/usr/bin/env python
# coding: utf-8


def encodingIdentifier(filename):
    encodings = ["utf8", "utf16", "cp1251"]
    for enc in encodings:
        try:
            with open(file=filename, mode="r", encoding=enc) as f:
                f.readline()
                return enc
        except UnicodeError:
            continue
    raise UnicodeError
