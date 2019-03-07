#!/usr/bin/env python
# coding: utf-8


pairs_1 = {'(': ')', '[': ']', '{': '}'}
pairs_2 = {')': '(', ']': '[', '}': '{'}


def is_bracket_correct(string):
    stack = []
    for symbol in string:
        if symbol in pairs_1.keys():
            stack.append(symbol)
        elif symbol in pairs_1.values():
            if len(stack) == 0:
                return False
            if not(stack.pop() == pairs_2.get(str(symbol))):
                return False
    return True
