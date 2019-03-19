#!/usr/bin/env python
# coding: utf-8


import json
from pechat import *


def print_json(filename, enc):
    text = list()
    with open(filename, encoding=enc) as file:
        try:
            sr = json.load(file)
            text.append(list(sr[0].keys()))
            for i in sr:
                if list(i.keys()) != s[0]:
                    raise KeyError
                text.append(list(i.values()))
        except (KeyError, json.JSONDecodeError):
            raise ValueError("Формат не валиден")
        except IndexError:
            raise RuntimeError("Формат не валиден")

    print_file(text)
