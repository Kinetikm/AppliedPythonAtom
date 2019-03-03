#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    d = dict([("{", "}"), ("(", ")"), ("[", "]")])
    d_reverse = dict([("}", "{"), (")", "("), ("]", "[")])
    stack = []
    for item in input_string:
        if d.get(item) is None:
            if len(stack) == 0:
                return False
            if stack[-1] == d_reverse.get(item):
                stack.pop(-1)
                continue
            return False
        stack.append(item)
    if len(stack) == 0:
        return True
    return False
