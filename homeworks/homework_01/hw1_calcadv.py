#!/usr/bin/env python
# coding: utf-8


def advanced_calculator(input_string):
    s = input_string.strip()
    if s == '':
        return None
    i = 0
    while i < len(s):
        if s[i] not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '.', ',', ')', '(', '-', '+', '*', '/']:
            return None
    for x in ['**', '*/', '/*', '//', '*+', '+*', '/+', '+/', '*-', '-*', '/-', '-/']:
        if x in s:
            return None
    for x in ['++', '--', '-+', '+-']:
        while x in s:
            l = l.replace("--", "+")
            l = l.replace("++", "+")
            l = l.replace("+-", "-")
            l = l.replace("-+", "-")
    if s[0] == '-' or s[0] == '+':
        s = "0" + s
    s = s.replace("(", " ( ")
    s = s.replace(")", " ) ")
    s = s.replace("+", " + ")
    s = s.replace("-", " - ")
    s = s.replace("*", " * ")
    s = s.replace("/", " / ")
    s = s.strip()
    try:
        return eval(s)
    except:
        return None
