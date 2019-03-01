#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    i = 0
    index1 = 0 # счетчик, отвечающй за ()
    index2 = 0 # счетчик, отвечающй за []
    index3 = 0 # счетчик, отвечающй за {}
    while i < len(input_string):
        if input_string[i] == '(':
            index1 += 1
        elif input_string[i] == ')':
            index1 -= 1
        elif input_string[i] == '[':
            index2 += 1
        elif input_string[i] == ']':
            index2 -= 1
        elif input_string[i] == '{':
            index3 += 1
        elif input_string[i] == '}':
            index3 -= 1
        if index1 < 0 or index2 < 0 or index3 < 0:
            break
        i += 1
    if index1 == 0 and index2 == 0 and index3 == 0:
        return 1
    else:
        return 0
