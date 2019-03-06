#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    l = []
    for a in input_string:
        if a == '(' or a == '{' or a == '[':
            l.append(a)
        if a == ')':
            if len(l) == 0:
                return False
            if l[len(l) - 1] == '(':
                l.pop()
            else:
                return False
        if a == ']':
            if len(l) == 0:
                return False
            if l[len(l) - 1] == '[':
                l.pop()
            else:
                return False
        if a == '}':
            if len(l) == 0:
                return False
            if l[len(l) - 1] == '{':
                l.pop()
            else:
                return False
    if l == []:
        return True
    else:
        return False

