#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    stack = ['.']
    for bracket in input_string:
        if bracket == '(' or bracket == '{' or bracket == '[':
            stack.append(bracket)
        if bracket == ')':
            if stack[-1] != '(':
                return False
            if stack[-1] == '(':
                stack.pop()
        if bracket == '}':
            if stack[-1] != '{':
                return False
            if stack[-1] == '{':
                stack.pop()
        if bracket == ']':
            if stack[-1] != '[':
                return False
            if stack[-1] == '[':
                stack.pop()
    return stack == ['.']


print(is_bracket_correct(''))
