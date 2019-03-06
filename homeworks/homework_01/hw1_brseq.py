#!/usr/bin/env python
# coding: utf-8


def rev(char):
    if char == ')':
        return '('
    elif char == ']':
        return '['
    elif char == '}':
        return '{'
    elif char == '(':
        return ')'
    elif char == '[':
        return ']'
    elif char == '{':
        return '}'


def is_bracket_correct(input_string):
    if len(input_string) % 2 != 0:
        return False
    else:
        while len(input_string) != 0:
            i = 0
            while input_string[i] != ')'\
                    and input_string[i] != ']'\
                    and input_string[i] != '}':
                i += 1
                if i > len(input_string)-1:
                    return False
            if input_string[0] == (')' or ']' or '}'):
                return False
            if input_string[i-1] == rev(input_string[i]):
                if len(input_string) > 2:
                    if i > 1:
                        input_string = input_string[:i-1]+input_string[i+1:]
                    else:
                        input_string = input_string[i+1:]
                else:
                    input_string = ''
            else:
                return False
        return True
