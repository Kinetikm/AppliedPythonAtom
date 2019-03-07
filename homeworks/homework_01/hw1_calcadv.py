#!/usr/bin/env python
# coding: utf-8


def advanced_calculator(input_string):
    s = input_string.strip()
    if s == '':
        return None
    s = s.replace(" ", "")
    i = 0
    while i < len(s):
        if s[i] not in ["0", "1", "2", "3", "4", "5",\
                "6", "7", "8", "9", ".", ",", ")",\
                        "(", "-", "+", "*", "/"]:
            return None
        i += 1
    for x in ['**', '*/', '/*', '//', '*+', '+*',\
              '/+', '+/', '*-', '-*', '/-', '-/']:
        if x in s:
            return None
    s = s.replace("--", "+")
    s = s.replace("++", "+")
    s = s.replace("+-", "-")
    s = s.replace("-+", "-")
    if s[0] == '-':
        s = "0" + s
    if s[0] == '+':
        s = s[1::]
    try:
        return float(eval(s))
    except:
        return None
