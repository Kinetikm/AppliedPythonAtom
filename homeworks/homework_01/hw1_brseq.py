#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    result = True
    i = 1
    for symbol in input_string[:len(input_string) // 2]:
        if symbol == '(':
            if ')' != input_string[len(input_string) - i]:
                result = False
        elif symbol == "[":
            if ']' != input_string[len(input_string) - i]:
                result = False
        elif symbol == '{':
            if "}" != input_string[len(input_string) - i]:
                result = False
        else:
            return False
        i += 1
    return result
