#!/usr/bin/env python
# coding: utf-8


pairs = {')': '(', '}': '{', ']': '['}


def is_bracket_correct(input_string):
    stack = []
    for element in input_string:
        if element in pairs:
            if not len(stack) or stack.pop() != pairs[element]:
                return False
        else:
            stack.append(element)
    return True
