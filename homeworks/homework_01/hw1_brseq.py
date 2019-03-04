#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    dic = {')': '(', ']': '[', '}': '{'}
    stek = []
    for c in input_string:
        if c in dic.values():
            stek.append(c)
        elif c in dic.keys() and stek == []:
            return False
        elif c in dic.keys() and stek[-1] == dic[c]:
            stek.pop()
        elif c in dic.keys() and stek[-1] != dic[c]:
            return False
    return stek == []
