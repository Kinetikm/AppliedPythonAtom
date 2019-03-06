#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    for i in range(len(input_string)):
        if (input_string[i] == '(' and input_string[- (i + 1)] == ')') or (
                input_string[i] == '[' and input_string[- (i + 1)] == ']') or (
                input_string[i] == '{' and input_string[- (i + 1)] == '}'):
            return True
        else:
            return False
