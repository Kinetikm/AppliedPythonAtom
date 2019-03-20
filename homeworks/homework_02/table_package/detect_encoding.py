#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def detect_enc(filename):
    enc_list = ["utf8", "cp1251",  "utf16"]
    encoding = 'undefined'
    for x in enc_list:
        try:
            with open(filename, "r", encoding=x) as f:
                f.read(2)
                encoding = x
                break
        except UnicodeError:
            continue
    return encoding
