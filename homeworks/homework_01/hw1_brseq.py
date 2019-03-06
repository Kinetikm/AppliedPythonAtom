#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    if (len(input_string)) % 2 != 0:
        return False
    b = len(input_string) / 2
    a = ['()', "[]", "{}"]
    for i in range(int(b)):
        for j in a:
            while j in input_string:
                input_string = input_string.replace(j, "")
    if input_string == "":
        return True
    else:
        return False
