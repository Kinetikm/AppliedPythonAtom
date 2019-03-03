#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    stack = []
    i = 0
    while i < len(input_string):
        if input_string[i] == '}':
            if len(stack) == 0:
                return False
            if stack[len(stack)-1] == '{':
                stack.pop()
            else:
                return False
        elif input_string[i] == ']':
            if len(stack) == 0:
                return False
            if stack[len(stack)-1] == '[':
                stack.pop()
            else:
                return False
        elif input_string[i] == ')':
            if len(stack) == 0:
                return False
            if stack[len(stack)-1] == '(':
                stack.pop()
            else:
                return False
        else:
            stack.append(input_string[i])
        i += 1
    if stack:
        return False
    else:
        return True
    raise NotImplementedError
