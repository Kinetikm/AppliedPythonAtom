#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    while '()' in input_string or '[]' in input_string or '{}' in input_string:
        input_string = input_string.replace('()', '')
        input_string = input_string.replace('[]', '')
        input_string = input_string.replace('{}', '')
    return not input_string
